from repository.parser import RepositoryParser


def test_supported_extensions_are_accepted():
    parser = RepositoryParser()

    assert parser.is_supported_file("app.py")
    assert parser.is_supported_file("README.md")
    assert parser.is_supported_file("main.go")


def test_unsupported_extensions_are_rejected():
    parser = RepositoryParser()

    assert not parser.is_supported_file("image.png")
    assert not parser.is_supported_file("video.mp4")


def test_ignored_directories_are_skipped():
    parser = RepositoryParser()

    assert parser.should_ignore_directory(".git")
    assert parser.should_ignore_directory("node_modules")
    assert not parser.should_ignore_directory("src")


def test_parse_repository_finds_only_supported_files(tmp_path):
    (tmp_path / "app.py").write_text("print('hi')")
    (tmp_path / "notes.txt").write_text("ignored extension")

    ignored_dir = tmp_path / "node_modules"
    ignored_dir.mkdir()
    (ignored_dir / "lib.py").write_text("ignored, wrong directory")

    parser = RepositoryParser()
    files = parser.parse_repository(str(tmp_path))

    paths = [f["path"] for f in files]

    assert any("app.py" in p for p in paths)
    assert not any("notes.txt" in p for p in paths)
    assert not any("node_modules" in p for p in paths)
