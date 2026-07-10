from processing.chunkers.generic_chunker import GenericChunker


def _metadata(size):
    return {"path": "README.md", "extension": ".md", "size": size}


def test_short_text_produces_a_single_chunk():
    chunker = GenericChunker(chunk_size=1000, overlap=200)
    text = "A" * 500

    chunks = chunker.chunk(text, _metadata(len(text)))

    assert len(chunks) == 1
    assert chunks[0].content == text
    assert chunks[0].start_char == 0
    assert chunks[0].end_char == 500


def test_long_text_is_split_with_overlap():
    chunker = GenericChunker(chunk_size=1000, overlap=200)
    text = "A" * 2500

    chunks = chunker.chunk(text, _metadata(len(text)))

    # step size is chunk_size - overlap = 800, so ceil(2500 / 800) = 4 chunks
    assert len(chunks) == 4

    # consecutive chunks overlap by exactly `overlap` characters
    assert chunks[1].start_char == chunks[0].start_char + 800
    assert chunks[0].end_char - chunks[1].start_char == 200


def test_each_chunk_gets_a_stable_sha256_hash():
    chunker = GenericChunker(chunk_size=1000, overlap=200)
    text = "A" * 500

    first_run = chunker.chunk(text, _metadata(len(text)))
    second_run = chunker.chunk(text, _metadata(len(text)))

    assert first_run[0].hash == second_run[0].hash
    assert len(first_run[0].hash) == 64
