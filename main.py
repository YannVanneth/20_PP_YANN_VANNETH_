from app.pipeline import Pipeline

EXIT_COMMANDS = {"exit", "quit"}
CHUNK_PREVIEW_CHARS = 400

def print_chunks(chunks) -> None:
    if not chunks:
        print("\n[no chunks retrieved]\n")
        return

    print("\n----- Retrieved chunks -----")
    for i, chunk in enumerate(chunks, 1):
        preview = chunk if len(chunk) <= CHUNK_PREVIEW_CHARS else chunk[:CHUNK_PREVIEW_CHARS] + " ..."
        print(f"Chunk {i}:\n{preview}\n")
    print("---------------------------\n")


def main() -> None:
    print("Local RAG - Chat with your documents")
    print("Ask a question about the documents in data/. Type 'exit' or 'quit' to leave.\n")

    rag = Pipeline()

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not question:
            continue
        if question.lower() in EXIT_COMMANDS:
            print("Goodbye!")
            break

        chunks, answer = rag.ask_with_context(question)
        print_chunks(chunks)
        print(f"Assistant: {answer}\n")


if __name__ == "__main__":
    main()
