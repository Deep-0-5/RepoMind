EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".tsx": "tsx",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
    ".md": "markdown",
}


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

            # Use the correct syntax highlighting based on file extension
            language = EXTENSION_TO_LANGUAGE.get(
                chunk.get("extension", ""),
                ""
            )

            context += f"```{language}\n"

            context += chunk["content"]

            context += "\n```\n\n"

            context += "---\n\n"

        return context