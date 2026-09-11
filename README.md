# Homework 01 - Baseline "Chat with Documents" App

A small local RAG app I built with Python, ChromaDB, and Ollama. It does
all 5 steps of naive RAG - ingest, chunk, embed, retrieve, generate - and
you can ask it questions about the docs in `data/` right in the terminal.

---

## 1. How to Run It

### you need

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) installed (using this instead of Poetry,
  `uv run` does basically the same thing as `poetry run`)
- Ollama running, with these 2 models pulled:
  ```bash
  ollama pull nomic-embed-text   # for embeddings
  ollama pull gemma4             # for generating answers
  ```

> note: the assignment said to use `llama3.2` for generation, i used
> `gemma4` instead since i already had it on my machine. if you want to
> match the assignment exactly, run `ollama pull llama3.2` and change
> `GEN_MODEL = 'llama3.2'` in `app/config.py`.

### quickstart

```bash
cd basic_rag
uv sync                              # installs everything

uv run python demo_vector_check.py   # step 4 - just checks the vector store works
uv run python main.py                # starts the actual chat
```

first time you run `main.py` it notices the chroma collection is empty and
builds the index for you (loads the docs, chunks them, embeds them, saves
them), then the chat starts. type a question, it shows you the chunks it
found plus the answer, type `exit` or `quit` whenever youre done.

if you change your docs or the chunk settings and want a fresh index, just
delete the `chroma_db/` folder and run `main.py` again.

---

## 2. What I Chose and Why

### chunking

- what i used: fixed-size chunks, cutting every 800 characters with 160
  characters of overlap. see `app/chunking.py`.
- why: my docs are short IT support guides, so 800 chars usually fits a
  step or two without going over the embedding model's limit, and the
  overlap means a step is less likely to get cut right in half. its the
  simplest option that fit my docs ok. tried a smarter splitter too, check
  `docs/CHUNKING_COMPARISON.md` for that (bonus).

### embedding model and vector db

- embedding model: `nomic-embed-text` through Ollama, runs local, makes
  768-number vectors, pretty lightweight.
- vector db: ChromaDB, using its `PersistentClient` so it just saves to a
  folder (`chroma_db/`) — no docker or server needed for this part.
- generation model: `gemma4` through Ollama. the prompt in
  `app/generator.py` tells it to only answer from the chunks it got, and
  to say it doesnt know if the chunks dont have the answer.

---

## 3. How the Project is Laid Out

```
basic_rag/
├── app/
│   ├── config.py           # all the settings live here (models, chunk size, top_k...)
│   ├── ingestion.py        # loads the .txt files and builds the chroma index
│   ├── chunking.py         # the fixed-size splitter i actually use
│   ├── chunking_recursive.py # bonus - a different splitter, just for comparing
│   ├── embeddings.py       # turns text into vectors using ollama
│   ├── vector_store.py     # talks to chroma (save + search)
│   ├── vector_store_qdrant.py # bonus - same thing but for qdrant
│   ├── retriever.py        # question -> embedding -> top chunks + how close the match was
│   ├── generator.py        # builds the prompt and asks the llm
│   └── pipeline.py         # glues retriever + generator together, handles no-match too
├── data/                   # my 10 IT support docs (.txt)
├── chroma_db/              # where chroma saves stuff (not in git, gets rebuilt)
├── qdrant_storage/         # same but for qdrant (bonus only, also not in git)
├── docker-compose.yml      # bonus - spins up qdrant for the db comparison
├── demo_vector_check.py    # step 4 - quick check the vector store actually works
├── compare_chunking.py     # bonus - fixed-size vs recursive
├── compare_vector_dbs.py   # bonus - chroma vs qdrant
├── main.py                 # the actual chat loop
├── docs/
│   ├── TESTLOG.md          # step 7 - 5 test questions, what got retrieved, what it answered
│   ├── REFLECTION.md       # step 8 - my writeup
│   ├── CHUNKING_COMPARISON.md  # bonus writeup
│   └── VECTOR_DB_COMPARISON.md # bonus writeup
├── pyproject.toml          # dependencies
└── README.md               # youre reading it
```

quick map of which file does which RAG step:

| Step     | File                              |
|----------|------------------------------------|
| Ingest   | `app/ingestion.py`               |
| Chunk    | `app/chunking.py`                |
| Embed    | `app/embeddings.py`              |
| Store    | `app/vector_store.py`            |
| Retrieve | `app/retriever.py`               |
| Generate | `app/generator.py`               |
| it together | `app/pipeline.py`, `main.py` |

---

## 4. What Im Submitting

- all the code (`app/`, `main.py`, `demo_vector_check.py`)
- this README
- `docs/TESTLOG.md` - the 5 test questions from step 7
- `docs/REFLECTION.md` - the writeup from step 8

---

## 5. Bonus Stuff I Did

- **show the chunks before the answer** - `main.py` and
  `demo_vector_check.py` both print what got retrieved before showing the
  answer, so you can see where it came from.
- **say "cant find it" instead of guessing** - `app/retriever.py` now also
  gives back how close the best match was, and `app/pipeline.py` just
  skips the llm and says it cant find it if nothing is close enough
  (cutoff is `config.NO_MATCH_DISTANCE_THRESHOLD = 0.75`). see Q5 in
  `docs/TESTLOG.md` for this in action.
- **tried 2 chunking methods** - `compare_chunking.py` runs my fixed-size
  splitter against a recursive one (`app/chunking_recursive.py`) on all 10
  docs. writeup in `docs/CHUNKING_COMPARISON.md`.
- **tried 2 vector databases** - `compare_vector_dbs.py` puts the same
  chunks into both ChromaDB and a local Qdrant and compares what comes
  back. you need `docker compose up -d` running first (qdrant runs on
  `localhost:6343`, not the usual 6333, cause that port was already taken
  by something else on my machine). writeup in
  `docs/VECTOR_DB_COMPARISON.md`.