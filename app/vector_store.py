from typing import List
import chromadb
from chromadb import Settings
from app import config

_CHROMA_SETTING = Settings(anonymized_telemetry=False)

def get_collection():
    client = chromadb.PersistentClient(path=config.CHROMA_DIR, settings=_CHROMA_SETTING)
    return client.get_or_create_collection(name=config.COLLECTION_NAME)

def search_by_embedding(query_embedding: List[float], top_k: int = config.RETRIEVER_TOP_K):
    collection = get_collection()
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )