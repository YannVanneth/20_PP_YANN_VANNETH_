# Vector DB Comparison

Put the same 42 chunks into ChromaDB (what app uses) and Qdrant (just for
this test), then asked both the same 5 questions from my test log.

run it: `docker compose up -d` then `uv run python compare_vector_dbs.py`

## setup

chroma - no setup at all, just a python lib that saves to a file

qdrant - needed docker, a compose file, had to pick the vector size +
distance type myself, and had to convert my string ids into uuids since
qdrant doesnt take plain text ids. also had a port conflict with another
project so i used 6343 instead of the default 6333

chroma was way faster to get going. qdrant took more work but its a real
server, which is useful if this app ever needs to scale up later.

## results

both returned the exact same source doc, in the same order, for all 5
questions. the numbers arent directly comparable (chroma = lower is
better, qdrant = higher is better) but the ranking matches either way. the
pytorch question (not in my docs) was clearly seperated from the real
ones on both dbs.
