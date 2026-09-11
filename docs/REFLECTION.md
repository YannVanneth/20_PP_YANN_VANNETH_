# Reflection

Building this project step by step really helped me understand how RAG
actually works, not just the theory.

The retrieval part worked best for me. I used nomic-embed-text for
embeddings and ChromaDB to store and search them, and honestly for almost
every question that was in my docs it found the right file first try.
Distance score was like 0.33 for a good match.

Chunking was harder than I thought it'd be. I just cut text every 800
characters with some overlap, simple but it doesn't really understand the
document structure. One time the app skipped "Step 3" of a guide cause
that chunk wasnt in the top 3 results, overlap helped a bit but not fully.

If I improve this later I'd try a chunk splitter that actually looks at
headings/steps instead of just character count. Also thought about adding
a rule where if nothing matches close enough, just tell the user "not
found" instead of the model guessing — I actually added that already,
check TESTLOG.md for it.
