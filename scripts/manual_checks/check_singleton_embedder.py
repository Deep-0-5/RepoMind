from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

embedder1 = SentenceTransformerEmbedder()
embedder2 = SentenceTransformerEmbedder()

print(embedder1 is embedder2)
print(embedder1.model is embedder2.model)