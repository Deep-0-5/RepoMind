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

    def ask(self, question):
        
        if not question.strip():
            raise ValueError(
                "Question cannot be empty."
            )


        chunks = self.retriever.retrieve(question)

        context = self.context_builder.build_context(chunks)

        answer = self.generator.generate(
            question,
            context
        )

        return answer