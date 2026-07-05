from dotenv import load_dotenv
import os

load_dotenv()

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")

# Retrieval Configuration
TOP_K = 5

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Database
CHROMA_DB_PATH = "data/chroma_db"
COLLECTION_NAME = "repository_chunks"