from app.chunking import chunk_text
from app.chunking_recursive import recursive_chunk_text
from app.ingestion import load_documents

STEP_PROBLEM_FILE = "006_Creating_a_Backup_of_Important_Files.txt"
STEP_PROBLEM_HEADING = "Step 3: Connect Your Backup Device"
STEP_PROBLEM_BODY = "connect it to your computer"


def stats(chunks):
    if not chunks:
        return {"count": 0, "avg": 0, "min": 0, "max": 0}
    lengths = [len(c) for c in chunks]
    return {
        "count": len(chunks),
        "avg": round(sum(lengths) / len(lengths), 1),
        "min": min(lengths),
        "max": max(lengths),
    }


def main() -> None:
    documents = load_documents()

    print(f"{'Document':<55} {'Fixed-size':<22} {'Recursive':<22}")
    print("-" * 100)

    totals = {"fixed": [], "recursive": []}
    step_problem_doc_chunks = None

    for filename, text in documents:
        fixed_chunks = chunk_text(text)
        recursive_chunks = recursive_chunk_text(text)

        f_stats = stats(fixed_chunks)
        r_stats = stats(recursive_chunks)
        totals["fixed"].append(f_stats["count"])
        totals["recursive"].append(r_stats["count"])

        print(
            f"{filename:<55} "
            f"n={f_stats['count']:<3} avg={f_stats['avg']:<7} "
            f"n={r_stats['count']:<3} avg={r_stats['avg']:<7}"
        )

        if filename == STEP_PROBLEM_FILE:
            step_problem_doc_chunks = (fixed_chunks, recursive_chunks)

    print("-" * 100)
    print(f"Total chunks -> fixed-size: {sum(totals['fixed'])}, recursive: {sum(totals['recursive'])}")

    if step_problem_doc_chunks:
        print(f"\n--- Step 3 heading+body co-location check on {STEP_PROBLEM_FILE} ---")
        fixed_chunks, recursive_chunks = step_problem_doc_chunks

        def co_located(chunks):
            return any(STEP_PROBLEM_HEADING in c and STEP_PROBLEM_BODY in c for c in chunks)

        print(f"Fixed-size:  heading + body text in the SAME chunk? {co_located(fixed_chunks)}")
        print(f"Recursive:   heading + body text in the SAME chunk? {co_located(recursive_chunks)}")

        print("\nRecursive chunks touching 'Step 3' (showing fragmentation):")
        for c in recursive_chunks:
            if "Step 3" in c or STEP_PROBLEM_BODY in c:
                print(f"  - {c!r}")


if __name__ == "__main__":
    main()
