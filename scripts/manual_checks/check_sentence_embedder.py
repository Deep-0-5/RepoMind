from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

embedder = SentenceTransformerEmbedder()

embedding = embedder.embed_text(
    "Hello World"
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])