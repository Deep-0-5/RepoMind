from pathlib import Path


class FileReader:
    """Reads source code files safely."""

    def read_file(self, file_path):
        """
        Reads a file and returns its contents.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except UnicodeDecodeError:
            return None

        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None