from typing import List, Tuple
from app import config
from app.embeddings import embed_query
from app.vector_store import search_by_embedding

def retrieve(question: str, top_k: int = config.RETRIEVER_TOP_K) -> Tuple[List[str], float]:
    query_embedding = embed_query(question)
    results = search_by_embedding(query_embedding, top_k=top_k)

    if results and results.get("documents") and results["documents"][0]:
        chunks = results["documents"][0]
        best_distance = min(results["distances"][0])
        return chunks, best_distance
    return [], float("inf")
