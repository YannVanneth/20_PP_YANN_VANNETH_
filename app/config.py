from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# models we using
EMBEDDING_MODEL = 'nomic-embed-text'
GEN_MODEL = 'gemma4'

# how we cut up the text
CHUNK_SIZE = 800
CHUNK_OVERLAP = 160

# where stuff gets saved
DATA_DIR = str(BASE_DIR / 'data')
COLLECTION_NAME = 'documents'
CHROMA_DIR = str(BASE_DIR / 'chroma_db')

# qdrant stuff (just for the bonus comparison)
QDRANT_URL = 'http://localhost:6343'
QDRANT_COLLECTION_NAME = 'documents'
EMBEDDING_DIM = 768

# how many chunks to grab
RETRIEVER_TOP_K = 3

# bonus: if the closest match we find is still farther than this, just
# tell the user we cant find it instead of letting the llm guess.
# got this number by testing some real questions - stuff that was
# actually in my docs scored 0.57 or lower, random off topic stuff
# scored 0.80 or higher, so 0.75 sits right in the middle
NO_MATCH_DISTANCE_THRESHOLD = 0.75

# system prompt for the model
SYSTEM_PROMPT = "You are a helpful assistant."