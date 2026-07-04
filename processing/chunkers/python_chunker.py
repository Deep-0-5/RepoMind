from processing.chunkers.base_chunker import BaseChunker
import ast


class PythonChunker(BaseChunker):
    """Chunks Python files using the AST."""

    def chunk(self, text, metadata):
        chunks = []

        tree = ast.parse(text)

        chunk_id = 1

        for node in tree.body:

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                chunk_type = "function"

            elif isinstance(node, ast.ClassDef):
               chunk_type = "class"

            else:
               continue

            source = ast.get_source_segment(text, node)

            chunk = {
                "chunk_id": chunk_id,
                "type": chunk_type,
                "name": node.name,
                "content": source,
                "path": metadata["path"],
                "extension": metadata["extension"],
                "start_line": node.lineno,
                "end_line": node.end_lineno
            }

            chunks.append(chunk)

            chunk_id += 1

        return chunks