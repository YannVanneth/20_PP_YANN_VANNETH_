from typing import List
import ollama
from app import config

def generate_answer(question: str, chunks: List[str]) -> str:
    context = "\n\n---\n\n".join(chunks) if chunks else "No relevant context found."

    prompt = f"""Answer the question using only the provided context. If the context does not contain enough information, say that you cannot find the answer in the provided documents.

Context:
{context}

Question:
{question}

Answer:"""

    response = ollama.generate(
        model=config.GEN_MODEL,
        prompt=prompt,
        system=config.SYSTEM_PROMPT,
    )
    return response["response"]
