from typing import List
from . import config

def recursive_chunk_text(text: str, chunk_size: int = config.CHUNK_SIZE) -> List[str]:
    if not text or not text.strip():
        return []

    SEPARATORS = ["\n\n", "\n", ". ", " ", ""]

    pieces = [text.strip()]

    for separator in SEPARATORS:
        new_pieces = []
        for piece in pieces:
            if len(piece) <= chunk_size:
                new_pieces.append(piece)
                continue

            parts = piece.split(separator) if separator else list(piece)
            for part in parts:
                part = part.strip()
                if part:
                    new_pieces.append(part)
        pieces = new_pieces

    return pieces
