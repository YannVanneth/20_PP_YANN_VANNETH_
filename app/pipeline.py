from typing import List, Optional, Tuple
from app import config
from app.retriever import retrieve
from app.generator import generate_answer
from app.ingestion import build_index
from app.vector_store import get_collection

class Pipeline:
    def __init__(self, auto_index: bool = True):
        self.collection = get_collection()
        if auto_index and self.collection.count() == 0:
            print("Chroma collection is empty. Building index from data directory...")
            self.index()

    def index(self, dir_path: Optional[str] = None):
        if dir_path:
            return build_index(dir_path)
        return build_index()

    def ask_with_context(
        self, question: str, top_k: Optional[int] = None
    ) -> Tuple[List[str], str]:
        chunks, best_distance = retrieve(question, top_k=top_k) if top_k else retrieve(question)
        if not chunks or best_distance > config.NO_MATCH_DISTANCE_THRESHOLD:
            return chunks, "I could not find this in your documents."
        answer = generate_answer(question, chunks)
        return chunks, answer

    def ask(self, question: str, top_k: Optional[int] = None) -> str:
        _, answer = self.ask_with_context(question, top_k=top_k)
        return answer