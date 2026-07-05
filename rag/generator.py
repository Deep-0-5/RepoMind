from google import genai
from utils.config import GEMINI_API_KEY, LLM_MODEL
from rag.prompts import SYSTEM_PROMPT
from utils.logger import setup_logger

logger = setup_logger(__name__)

class GeminiGenerator:
    """
    Generates answers using Gemini.
    """

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, question, context):

        prompt = f"""
    {SYSTEM_PROMPT}

    {context}

    # User Question

    {question}
    """

        try:

            response = self.client.models.generate_content(
                model=LLM_MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            logger.error(
                f"Failed to generate response: {e}"
            )

            return "Unable to generate a response."