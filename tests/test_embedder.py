from embeddings.embedding_manager import EmbeddingManager

manager = EmbeddingManager()

embedder = manager.get_embedder()

code = """
def login():
    print("Hello")
"""

embedding = embedder.embed_text(code)

print(type(embedding))
print(len(embedding))
print(embedding[:10])