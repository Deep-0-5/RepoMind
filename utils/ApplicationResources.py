import chromadb
import os
from typing import Optional
from google import genai
from sentence_transformers import SentenceTransformer

from utils.config import (
    GEMINI_API_KEY,
    SENTENCE_TRANSFORMER_MODEL,
    CHROMA_DB_PATH,
    COLLECTION_NAME,
)

from utils.logger import setup_logger


logger = setup_logger(__name__)


class ResourceManager:
    """
    Manages shared heavyweight resources used across the application.
    """
    def __new__(cls):
        raise TypeError(
            "ResourceManager cannot be instantiated."
        )
    
    _sentence_transformer: Optional[SentenceTransformer] = None
    _gemini_client: Optional[genai.Client] = None
    _chroma_client: Optional[chromadb.PersistentClient] = None
    _chroma_collection = None

    @classmethod
    def get_sentence_transformer(cls):

        if cls._sentence_transformer is None:

            logger.info(
                f"Loading Sentence Transformer: {SENTENCE_TRANSFORMER_MODEL}"
            )

            cls._sentence_transformer = SentenceTransformer(
                SENTENCE_TRANSFORMER_MODEL
            )

            logger.info(
                "Sentence Transformer loaded successfully."
            )

        return cls._sentence_transformer

    @classmethod
    def get_gemini_client(cls):

        if cls._gemini_client is None:

            logger.info(
                "Initializing Gemini Client..."
            )

            cls._gemini_client = genai.Client(
                api_key=GEMINI_API_KEY
            )

            logger.info(
                "Gemini Client initialized successfully."
            )

        return cls._gemini_client

    @classmethod
    def get_chroma_client(cls):

        if cls._chroma_client is None:

            logger.info(
                "Initializing ChromaDB Client..."
            )

            # Create the directory if it doesn't exist
            os.makedirs(CHROMA_DB_PATH, exist_ok=True)

            cls._chroma_client = chromadb.PersistentClient(
                path=CHROMA_DB_PATH
            )

        return cls._chroma_client

    @classmethod
    def get_chroma_collection(cls):

        if cls._chroma_collection is None:

            logger.info(
                f"Opening ChromaDB Collection: {COLLECTION_NAME}"
            )

            client = cls.get_chroma_client()

            cls._chroma_collection = (
                client.get_or_create_collection(
                    name=COLLECTION_NAME
                )
            )

        return cls._chroma_collection