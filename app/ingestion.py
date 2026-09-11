import mimetypes
import os
from typing import List, Tuple

from . import config
from .chunking import chunk_text
from .embeddings import embed_texts
from .vector_store import get_collection


def load_documents(dir_path: str = config.DATA_DIR) -> List[Tuple[str, str]]:
    if not os.path.exists(dir_path):
        raise FileNotFoundError(f"Data directory does not exist: {dir_path}")

    documents: List[Tuple[str, str]] = []

    for file_name in sorted(os.listdir(dir_path)):
        path = os.path.join(dir_path, file_name)

        if not os.path.isfile(path):
            continue

        file_type, _ = mimetypes.guess_type(path)

        if file_type == "text/plain" or file_name.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if content:
                    documents.append((file_name, content))
        else:
            print(f"Skipping {file_name} because file type is not supported")

    return documents


def build_index(dir_path: str = config.DATA_DIR) -> int:
    collection = get_collection()
    documents = load_documents(dir_path)

    ids, texts, metadatas = [], [], []
    for filename, doc_text in documents:
        chunks = chunk_text(doc_text)
        for i, chunk in enumerate(chunks):
            ids.append(f"{filename}::{i}")
            texts.append(chunk)
            metadatas.append({"source": filename, "chunk_index": i})

    if not texts:
        print("No document chunks found to index.")
        return 0

    embeddings = embed_texts(texts)
    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )
    print(f"Successfully indexed {len(texts)} chunks from {len(documents)} documents.")
    return len(texts)