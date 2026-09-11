from typing import List
import ollama
from . import config


def embed_texts(texts: List[str]) -> List[List[float]]:
    """turns a bunch of text chunks into vectors using ollama"""
    if not texts:
        return []
    response = ollama.embed(
        model=config.EMBEDDING_MODEL,
        input=texts,
    )
    return response.embeddings


def embed_query(query: str) -> List[float]:
    """same thing but for just one question, not a whole list"""
    response = ollama.embed(
        model=config.EMBEDDING_MODEL,
        input=query,
    )
    return response.embeddings[0]