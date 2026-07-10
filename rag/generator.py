from utils.config import LLM_MODEL
from rag.prompts import SYSTEM_PROMPT

from utils.logger import setup_logger
from utils.ApplicationResources import ResourceManager


logger = setup_logger(__name__)


class GeminiGenerator:
    """
    Generates answers using Gemini.
    """

    def __init__(self):

        self.client = (
            ResourceManager.get_gemini_client()
        )

    def generate(self, question, context, history=None):
        """
        Generate an answer using the RAG pipeline.

        Args:
            question: The user's question.
            context: The retrieved repository context.
            history: Optional list of previous conversation turns
                     [{"role": "user"/"assistant", "content": "..."}].
        """

        # Build conversation history section
        history_section = ""

        if history:
            history_section = "\n# Conversation History\n\n"

            for msg in history:
                role = msg["role"].capitalize()
                history_section += f"**{role}:** {msg['content']}\n\n"

        prompt = f"""
{SYSTEM_PROMPT}

{context}

{history_section}
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