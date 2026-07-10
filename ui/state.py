import streamlit as st

from indexing.repository_indexer import RepositoryIndexer
from rag.chat_engine import ChatEngine
from utils import chat_store


@st.cache_resource(show_spinner=False)
def get_indexer() -> RepositoryIndexer:
    """
    Returns a single cached RepositoryIndexer instance.
    st.cache_resource ensures this is built once per app process
    and reused across every rerun, instead of rebuilt on every click.
    """

    return RepositoryIndexer()


@st.cache_resource(show_spinner=False)
def get_chat_engine() -> ChatEngine:
    """
    Returns a single cached ChatEngine instance.
    """

    return ChatEngine()


def init_session_state():
    """
    Initializes every session-state key the app relies on.

    Safe to call on every rerun -- each key is only set to its
    default the first time it's missing, so existing values
    (chat history, indexed repo, etc.) are never overwritten.
    """

    if "conversations" not in st.session_state:
        st.session_state.conversations = chat_store.load_conversations()

    defaults = {
        # Which repository is currently loaded
        "repo_path": None,
        "repo_name": None,

        # Indexing status
        "is_indexed": False,
        "index_stats": {
            "files": 0,
            "chunks": 0
        },

        # Appearance
        "theme": "light",

        # Active conversation
        "active_conversation_id": None,
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value

    if st.session_state.active_conversation_id is None:
        _ensure_active_conversation()


def _ensure_active_conversation():
    """
    Makes sure there is always an active conversation to write into.
    Reuses the most recent one if it exists, otherwise creates one.
    """

    if st.session_state.conversations:
        st.session_state.active_conversation_id = (
            st.session_state.conversations[0]["id"]
        )
    else:
        start_new_conversation()


def get_active_conversation() -> dict | None:
    """
    Returns the currently active conversation dict, or None.
    """

    for conversation in st.session_state.conversations:

        if conversation["id"] == st.session_state.active_conversation_id:
            return conversation

    return None


def start_new_conversation():
    """
    Creates a fresh, empty conversation and makes it active.
    """

    conversation = chat_store.new_conversation(
        repo_name=st.session_state.get("repo_name")
    )

    st.session_state.conversations.insert(0, conversation)
    st.session_state.active_conversation_id = conversation["id"]

    chat_store.save_conversations(st.session_state.conversations)


def switch_conversation(conversation_id: str):
    """
    Makes an existing conversation the active one.
    """

    st.session_state.active_conversation_id = conversation_id


def add_message(role: str, content: str, sources: list | None = None):
    """
    Appends a message to the active conversation and persists it.
    """

    conversation = get_active_conversation()

    if conversation is None:
        return

    conversation["messages"].append(
        {"role": role, "content": content}
    )

    if sources is not None:
        conversation["sources"] = sources

    if conversation["title"] == "New Chat" and role == "user":
        conversation["title"] = chat_store.derive_title(content)

    chat_store.save_conversations(st.session_state.conversations)
