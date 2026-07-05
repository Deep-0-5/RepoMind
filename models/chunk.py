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
    
    start_char: int | None = None

    end_char: int | None = None

    start_line: int | None = None

    end_line: int | None = None
    
    def to_metadata(self):
        metadata = {
            "path": self.path,
            "extension": self.extension
        }

        if self.type:
            metadata["type"] = self.type

        if self.name:
            metadata["name"] = self.name

        return metadata