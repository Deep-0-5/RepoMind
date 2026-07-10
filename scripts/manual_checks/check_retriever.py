from rag.retriever import Retriever

retriever = Retriever()

chunks = retriever.retrieve(
    "How do users login?",
    top_k=3
)

for chunk in chunks:

    print("=" * 60)

    print(f"Score : {chunk['score']:.4f}")
    print(f"File  : {chunk['path']}")
    print(f"Type  : {chunk['type']}")
    print(f"Name  : {chunk['name']}")

    print()

    print(chunk["content"][:300])