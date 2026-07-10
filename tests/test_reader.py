from repository.file_reader import FileReader


def test_read_file_returns_contents(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("print('hello')")

    reader = FileReader()

    assert reader.read_file(str(file_path)) == "print('hello')"


def test_read_file_returns_none_for_missing_file():
    reader = FileReader()

    assert reader.read_file("this/path/does/not/exist.py") is None


def test_read_file_returns_none_for_invalid_utf8(tmp_path):
    file_path = tmp_path / "binary.py"
    file_path.write_bytes(b"\xff\xfe\x00\x01")

    reader = FileReader()

    assert reader.read_file(str(file_path)) is None
