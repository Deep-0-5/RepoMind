from rag.retriever import Retriever
from rag.context_builder import ContextBuilder
from rag.generator import GeminiGenerator

retriever = Retriever()
builder = ContextBuilder()
generator = GeminiGenerator()

question = "How does user login work?"

chunks = retriever.retrieve(question)

context = builder.build_context(chunks)

answer = generator.generate(question, context)

print(answer)