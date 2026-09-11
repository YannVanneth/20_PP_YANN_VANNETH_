import time

from app.chunking import chunk_text
from app.embeddings import embed_query, embed_texts
from app.ingestion import load_documents
from app.vector_store import search_by_embedding as chroma_search
from app.vector_store_qdrant import search_by_embedding as qdrant_search
from app.vector_store_qdrant import upsert as qdrant_upsert

QUESTIONS = [
    "How do I configure VPN access for remote workers?",
    "What should I do if I have forgotten my PIN?",
    "How do I set up a conference call on Cisco Webex?",
    "What are the steps to create a backup of important files?",
    "What is the best way to train a neural network in PyTorch?",
]


def build_qdrant_index() -> int:
    documents = load_documents()
    ids, texts, metadatas = [], [], []
    for filename, doc_text in documents:
        for i, chunk in enumerate(chunk_text(doc_text)):
            ids.append(f"{filename}::{i}")
            texts.append(chunk)
            metadatas.append({"source": filename, "chunk_index": i})

    embeddings = embed_texts(texts)
    qdrant_upsert(ids=ids, texts=texts, embeddings=embeddings, metadatas=metadatas)
    return len(texts)


def main() -> None:
    print("Building Qdrant index from the same chunks used by Chroma...")
    start = time.perf_counter()
    n = build_qdrant_index()
    print(f"Indexed {n} chunks into Qdrant in {time.perf_counter() - start:.1f}s\n")

    for question in QUESTIONS:
        print(f"=== {question} ===")
        query_embedding = embed_query(question)

        chroma_results = chroma_search(query_embedding, top_k=3)
        print("Chroma  :", [
            f"{m.get('source')} (dist={d:.4f})"
            for m, d in zip(chroma_results["metadatas"][0], chroma_results["distances"][0])
        ])

        qdrant_results = qdrant_search(query_embedding, top_k=3)
        print("Qdrant  :", [
            f"{p.payload.get('source')} (score={p.score:.4f})"
            for p in qdrant_results
        ])
        print()


if __name__ == "__main__":
    main()
