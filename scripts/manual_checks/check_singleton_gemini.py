from embeddings.gemini_embedder import GeminiEmbedder

embedder1 = GeminiEmbedder()
embedder2 = GeminiEmbedder()

print(embedder1 is embedder2)
print(embedder1.client is embedder2.client)
