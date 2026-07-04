from google import genai

from embeddings.base_embedder import BaseEmbedder
from utils.config import GEMINI_API_KEY, EMBEDDING_MODEL


class GeminiEmbedder(BaseEmbedder):
    """Embedding provider using Google's GenAI SDK."""

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def embed_text(self, text: str) -> list[float]:

        if not text.strip():
            raise ValueError("Input text cannot be empty.")

        try:
            response = self.client.models.embed_content(
                model=EMBEDDING_MODEL,
                contents=text,
            )

            return response.embeddings[0].values

        except Exception as e:
            print(f"Embedding Error: {e}")
            return None