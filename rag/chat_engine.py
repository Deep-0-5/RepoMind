from rag.retriever import Retriever
from rag.context_builder import ContextBuilder
from rag.generator import GeminiGenerator


class ChatEngine:
    """
    Coordinates the complete RAG pipeline.
    """

    def __init__(self):

        self.retriever = Retriever()

        self.context_builder = ContextBuilder()

        self.generator = GeminiGenerator()

    def ask(self, question, history=None):
        """
        Runs the full RAG pipeline for a question.

        Args:
            question: The user's question.
            history: Optional list of previous message dicts
                     [{"role": "user"/"assistant", "content": "..."}].

        Returns:
            tuple: (answer_text, retrieved_chunks)
        """

        if not question.strip():
            raise ValueError(
                "Question cannot be empty."
            )

        chunks = self.retriever.retrieve(question)

        context = self.context_builder.build_context(chunks)

        answer = self.generator.generate(
            question,
            context,
            history=history
        )

        return answer, chunks