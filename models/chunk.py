from dataclasses import dataclass


@dataclass
class Chunk:
    """
    Represents one chunk of source code.
    """

    chunk_id: int

    content: str

    path: str

    extension: str

    type: str | None = None

    name: str | None = None

    start_char: int | None = None

    end_char: int | None = None

    start_line: int | None = None

    end_line: int | None = None
    
    hash: str | None = None
    
    def to_metadata(self):
        metadata = {
            "path": self.path,
            "extension": self.extension,
            "hash": self.hash
        }

        if self.type:
            metadata["type"] = self.type

        if self.name:
            metadata["name"] = self.name

        if self.start_line is not None:
            metadata["start_line"] = self.start_line

        if self.end_line is not None:
            metadata["end_line"] = self.end_line

        if self.start_char is not None:
            metadata["start_char"] = self.start_char

        if self.end_char is not None:
            metadata["end_char"] = self.end_char

        return metadata