import json
import uuid
from datetime import datetime
from pathlib import Path

from utils.logger import setup_logger


logger = setup_logger(__name__)

STORE_PATH = Path("data") / "chat_sessions.json"


def _ensure_store_exists():

    STORE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not STORE_PATH.exists():
        STORE_PATH.write_text(
            json.dumps({"conversations": []}, indent=2)
        )


def load_conversations() -> list[dict]:
    """
    Loads every saved conversation from disk, most recent first.
    Returns an empty list if nothing has been saved yet.
    """

    _ensure_store_exists()

    try:
        data = json.loads(STORE_PATH.read_text())
        return data.get("conversations", [])

    except Exception as e:
        logger.error(f"Failed to load chat sessions: {e}")
        return []


def save_conversations(conversations: list[dict]):
    """
    Persists the full conversation list to disk.
    """

    _ensure_store_exists()

    try:
        STORE_PATH.write_text(
            json.dumps({"conversations": conversations}, indent=2)
        )

    except Exception as e:
        logger.error(f"Failed to save chat sessions: {e}")


def new_conversation(repo_name: str | None = None) -> dict:
    """
    Builds a blank conversation record.
    """

    return {
        "id": str(uuid.uuid4()),
        "title": "New Chat",
        "created_at": datetime.now().isoformat(),
        "repo_name": repo_name,
        "messages": [],
        "sources": [],
    }


def derive_title(question: str, max_length: int = 40) -> str:
    """
    Turns the first question of a conversation into a short title.
    """

    question = question.strip().replace("\n", " ")

    if len(question) <= max_length:
        return question

    return question[:max_length].rstrip() + "..."
