from typing import List
from app import config


def chunk_text(
    text: str,
    chunk_size: int = config.CHUNK_SIZE,
    chunk_overlap: int = config.CHUNK_OVERLAP,
) -> List[str]:
    if not text or not text.strip():
        return []

    step = max(1, chunk_size - chunk_overlap)
    chunks = []

    for start in range(0, len(text), step):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        if len(text) <= end:
            break

    return chunks