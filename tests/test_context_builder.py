from rag.retriever import Retriever
from rag.context_builder import ContextBuilder

retriever = Retriever()
builder = ContextBuilder()

chunks = retriever.retrieve(
    "How do users login?"
)

context = builder.build_context(chunks)

print(context)