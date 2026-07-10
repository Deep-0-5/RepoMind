from dotenv import load_dotenv
import os

load_dotenv()

# Gemini Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
LLM_MODEL = os.getenv("LLM_MODEL")

if not GEMINI_API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY environment variable is missing. "
        "Please specify it in your .env file."
    )

if not LLM_MODEL:
    raise EnvironmentError(
        "LLM_MODEL environment variable is missing. "
        "Please specify it in your .env file."
    )

EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER",
    "gemini"
)

if EMBEDDING_PROVIDER.lower() == "gemini" and not EMBEDDING_MODEL:
    raise EnvironmentError(
        "EMBEDDING_MODEL environment variable is missing "
        "but EMBEDDING_PROVIDER is set to 'gemini'."
    )

SENTENCE_TRANSFORMER_MODEL = os.getenv(
    "SENTENCE_TRANSFORMER_MODEL",
    "BAAI/bge-small-en-v1.5"
)

# Retrieval Configuration
TOP_K = 5

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Vector Database
CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "data/chroma_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "repository_chunks"
)