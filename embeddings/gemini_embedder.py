import time

from embeddings.base_embedder import BaseEmbedder

from utils.config import EMBEDDING_MODEL
from utils.logger import setup_logger
from utils.ApplicationResources import ResourceManager


logger = setup_logger(__name__)


class GeminiEmbedder(BaseEmbedder):
    """
    Embedding provider using Google's GenAI SDK.
    """

    def __init__(self):

        self.client = (
            ResourceManager.get_gemini_client()
        )

    def embed_text(self, text: str) -> list[float] | None:

        if not text.strip():
            raise ValueError(
                "Input text cannot be empty."
            )

        max_retries = 5

        for attempt in range(max_retries):

            try:

                response = self.client.models.embed_content(
                    model=EMBEDDING_MODEL,
                    contents=text,
                )

                return response.embeddings[0].values

            except Exception as e:

                wait_time = 2 ** attempt

                logger.warning(
                    f"Embedding failed (Attempt {attempt + 1}/{max_retries}). "
                    f"Retrying in {wait_time} seconds..."
                )

                logger.error(str(e))

                if attempt == max_retries - 1:

                    logger.error(
                        "Maximum retry attempts reached."
                    )

                    return None

                time.sleep(wait_time)

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Embed multiple texts using Gemini's batch embedding.
        Falls back to sequential calls if batch fails.
        """

        if not texts:
            return []

        cleaned = [t if t.strip() else " " for t in texts]

        max_retries = 5

        for attempt in range(max_retries):

            try:

                response = self.client.models.embed_content(
                    model=EMBEDDING_MODEL,
                    contents=cleaned,
                )

                return [
                    e.values for e in response.embeddings
                ]

            except Exception as e:

                wait_time = 2 ** attempt

                logger.warning(
                    f"Batch embedding failed (Attempt {attempt + 1}/{max_retries}). "
                    f"Retrying in {wait_time} seconds..."
                )

                logger.error(str(e))

                if attempt == max_retries - 1:

                    logger.warning(
                        "Batch embedding exhausted retries. "
                        "Falling back to sequential embedding."
                    )

                    results = []
                    for text in cleaned:
                        emb = self.embed_text(text)
                        if emb is not None:
                            results.append(emb)
                        else:
                            results.append([])
                    return results

                time.sleep(wait_time)

        return []