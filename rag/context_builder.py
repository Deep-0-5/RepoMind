class ContextBuilder:
    """
    Builds repository context from retrieved chunks.
    """

    def build_context(self, retrieved_chunks):

        context = "# Repository Context\n\n"

        for index, chunk in enumerate(retrieved_chunks, start=1):

            context += f"## Chunk {index}\n\n"

            context += f"**File:** `{chunk['path']}`\n\n"

            context += f"**Type:** {chunk['type']}\n\n"

            context += f"**Name:** {chunk['name']}\n\n"

            context += f"**Similarity Score:** {chunk['score']:.4f}\n\n"

            context += "```python\n"

            context += chunk["content"]

            context += "\n```\n\n"

            context += "---\n\n"

        return context