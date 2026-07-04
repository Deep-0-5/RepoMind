from pathlib import Path
import os

class RepositoryParser:
    """Scans a repository and collects supported source files."""

    def __init__(self):
        self.ignored_directories = {
            ".git",
            ".github",
            "node_modules",
            "venv",
            "__pycache__",
            "dist",
            "build"
        }

        self.supported_extensions = {
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".java",
            ".cpp",
            ".c",
            ".cs",
            ".go",
            ".rs",
            ".md"
        }

    def parse_repository(self, repository_path):
        files_metadata = []

        for root, dirs, files in os.walk(repository_path):

            # Ignore unnecessary directories
            dirs[:] = [
                directory
                for directory in dirs
                if not self.should_ignore_directory(directory)
            ]

            # Process every file
            for file in files:
                file_path = Path(root) / file

                # Skip unsupported file types
                if not self.is_supported_file(file_path):
                    continue

                # Collect file metadata
                file_info = {
                    "path": str(file_path),
                    "extension": file_path.suffix,
                    "size": file_path.stat().st_size
                }

                files_metadata.append(file_info)

        return files_metadata

    def is_supported_file(self, file_path):
        file = Path(file_path)

        extension = file.suffix

        return extension in self.supported_extensions

    def should_ignore_directory(self, directory_name):
        return directory_name in self.ignored_directories