from processing.chunkers.base_chunker import BaseChunker
from processing.chunkers.generic_chunker import GenericChunker
import ast
from models.chunk import Chunk
from utils.hash_utils import generate_hash
from utils.logger import setup_logger


logger = setup_logger(__name__)


class PythonChunker(BaseChunker):
    """Chunks Python files using the AST."""

    def __init__(self):
        self._fallback = GenericChunker()

    def chunk(self, text, metadata):

        try:
            tree = ast.parse(text)
        except SyntaxError as e:
            logger.warning(
                f"SyntaxError in {metadata['path']}: {e}. "
                "Falling back to GenericChunker."
            )
            return self._fallback.chunk(text, metadata)

        chunks = []
        chunk_id = 1

        # Collect spans of all function/class definitions
        # so we can extract module-level code that falls outside them.
        definition_spans = []

        # Walk the full AST tree to capture nested definitions
        for node in ast.walk(tree):

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                chunk_type = "function"

            elif isinstance(node, ast.ClassDef):
                chunk_type = "class"

            else:
                continue

            source = ast.get_source_segment(text, node)

            if not source:
                continue

            definition_spans.append(
                (node.lineno, node.end_lineno)
            )

            chunk = Chunk(
                chunk_id=chunk_id,
                type=chunk_type,
                name=node.name,
                content=source,
                path=metadata["path"],
                extension=metadata["extension"],
                start_line=node.lineno,
                end_line=node.end_lineno,
                hash=generate_hash(source)
            )

            chunks.append(chunk)
            chunk_id += 1

        # Capture module-level code (imports, constants, globals)
        module_lines = self._extract_module_level_code(
            text, definition_spans
        )

        if module_lines.strip():

            chunk = Chunk(
                chunk_id=chunk_id,
                type="module",
                name="module_level",
                content=module_lines,
                path=metadata["path"],
                extension=metadata["extension"],
                start_line=1,
                end_line=None,
                hash=generate_hash(module_lines)
            )

            chunks.append(chunk)

        return chunks

    def _extract_module_level_code(self, text, definition_spans):
        """
        Extracts lines that are NOT part of any function/class definition.
        This captures imports, constants, module docstrings, and global
        assignments that would otherwise be lost.
        """

        lines = text.splitlines(keepends=True)
        definition_line_set = set()

        for start, end in definition_spans:
            if start and end:
                for line_num in range(start, end + 1):
                    definition_line_set.add(line_num)

        module_lines = []

        for i, line in enumerate(lines, start=1):
            if i not in definition_line_set:
                module_lines.append(line)

        return "".join(module_lines)