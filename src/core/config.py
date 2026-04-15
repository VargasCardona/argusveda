from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

CHROMA_PATH = BASE_DIR / "vectorstore" / "chroma_db"
STORE_PATH = BASE_DIR / "vectorstore" / "parent_store"
DATA_PATH = BASE_DIR / "src" / "data"
OUTPUT_DIR = BASE_DIR / "output"

NETWORK_SCAN_RANGE = "192.168.1.0/24"

CHILD_SPLITTER_CHUNK_SIZE = 200
PARENT_SPLITTER_CHUNK_SIZE = 1500

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
