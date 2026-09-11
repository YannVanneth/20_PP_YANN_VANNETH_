import uuid
from typing import Dict, List

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app import config

_ID_NAMESPACE = uuid.UUID("12345678-1234-5678-1234-567812345678")


def get_qdrant_client() -> QdrantClient:
    return QdrantClient(url=config.QDRANT_URL)


def get_or_create_collection(client: QdrantClient = None) -> QdrantClient:
    client = client or get_qdrant_client()
    if not client.collection_exists(config.QDRANT_COLLECTION_NAME):
        client.create_collection(
            collection_name=config.QDRANT_COLLECTION_NAME,
            vectors_config=VectorParams(size=config.EMBEDDING_DIM, distance=Distance.COSINE),
        )
    return client


def _point_id(chunk_id: str) -> str:
    return str(uuid.uuid5(_ID_NAMESPACE, chunk_id))


def upsert(ids: List[str], texts: List[str], embeddings: List[List[float]], metadatas: List[Dict]) -> None:
    client = get_or_create_collection()
    points = [
        PointStruct(
            id=_point_id(chunk_id),
            vector=embedding,
            payload={"chunk_id": chunk_id, "text": text, **metadata},
        )
        for chunk_id, text, embedding, metadata in zip(ids, texts, embeddings, metadatas)
    ]
    client.upsert(collection_name=config.QDRANT_COLLECTION_NAME, points=points)


def search_by_embedding(query_embedding: List[float], top_k: int = config.RETRIEVER_TOP_K):
    client = get_qdrant_client()
    result = client.query_points(
        collection_name=config.QDRANT_COLLECTION_NAME,
        query=query_embedding,
        limit=top_k,
    )
    return result.points
