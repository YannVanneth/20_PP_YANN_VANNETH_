from app.embeddings import embed_query
from app.vector_store import search_by_embedding

TEST_QUESTION = "How do I configure VPN access for remote workers?"
TOP_K = 3


def main() -> None:
    print(f"Test question: {TEST_QUESTION}\n")

    query_embedding = embed_query(TEST_QUESTION)
    results = search_by_embedding(query_embedding, top_k=TOP_K)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for rank, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances), 1):
        print(f"Chunk {rank}  (distance={dist:.4f})")
        print(f"source: {meta.get('source')}   chunk_index: {meta.get('chunk_index')}")
        print(doc)
        print()


if __name__ == "__main__":
    main()
