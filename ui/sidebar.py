import streamlit as st
from pathlib import Path

from ui.components import (
    section_label,
    secondary_button,
    primary_button,
    metric_card,
    repository_card,
    repository_card_empty,
    error,
    success,
    divider,
)
from ui.state import get_indexer, start_new_conversation, switch_conversation
from repository.clone_repo import RepositoryCloner


def render_sidebar():

    with st.sidebar:

        _render_brand()

        _render_chat_history()

        divider(subtle=True)

        section_label("Repository")

        _render_source_tabs()

        divider(subtle=True)

        section_label("Statistics")

        col1, col2 = st.columns(2)

        with col1:
            metric_card(
                "Files",
                st.session_state.index_stats["files"]
            )

        with col2:
            metric_card(
                "Chunks",
                st.session_state.index_stats["chunks"]
            )


def _render_brand():
    """Compact wordmark at the top of the sidebar."""

    st.markdown(
        """
<div class="rm-brand">
    <div class="rm-brand-mark">R</div>
    <div class="rm-brand-name">RepoMind</div>
</div>
""",
        unsafe_allow_html=True
    )


def _render_chat_history():
    """
    Renders a "New Chat" button plus the list of saved
    conversations, similar to a typical chat-app sidebar.
    """

    st.markdown('<div class="rm-primary-btn">', unsafe_allow_html=True)

    if primary_button("+  New Chat", key="new_chat"):
        start_new_conversation()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    conversations = st.session_state.conversations

    if not conversations:
        return

    section_label("Chats")

    for conversation in conversations[:15]:

        is_active = (
            conversation["id"] == st.session_state.active_conversation_id
        )

        css_class = (
            "rm-history-item-active" if is_active else "rm-history-item"
        )

        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)

        if secondary_button(
            conversation["title"],
            key=f"conv_{conversation['id']}"
        ):
            switch_conversation(conversation["id"])
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)


def _render_source_tabs():
    """
    A compact two-tab segmented control for choosing between a local
    folder and a GitHub URL, styled to look like a native tab group
    rather than a radio input.
    """

    if "repo_source_tab" not in st.session_state:
        st.session_state.repo_source_tab = "local"

    tab_col1, tab_col2 = st.columns(2)

    with tab_col1:
        active = st.session_state.repo_source_tab == "local"
        st.markdown(
            f'<div class="{"rm-tab-active" if active else "rm-tab"}">',
            unsafe_allow_html=True
        )
        if st.button("Local", key="tab_local", use_container_width=True):
            st.session_state.repo_source_tab = "local"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_col2:
        active = st.session_state.repo_source_tab == "github"
        st.markdown(
            f'<div class="{"rm-tab-active" if active else "rm-tab"}">',
            unsafe_allow_html=True
        )
        if st.button("GitHub", key="tab_github", use_container_width=True):
            st.session_state.repo_source_tab = "github"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.repo_source_tab == "local":
        _render_local_repository()
    else:
        _render_github_repository()

    divider(subtle=True)

    if st.session_state.is_indexed:
        repository_card(
            name=st.session_state.repo_name,
            path=st.session_state.repo_path,
            status="Ready"
        )
    else:
        repository_card_empty("No repository indexed yet.")


def _render_local_repository():
    """
    Lets the user point at a local folder on disk and index it.
    """

    path_input = st.text_input(
        "Local Repository Path",
        value=st.session_state.repo_path or "",
        placeholder="/path/to/your/repository",
        label_visibility="collapsed"
    )

    st.markdown('<div class="rm-primary-btn">', unsafe_allow_html=True)

    clicked = primary_button("Index Repository", key="index_local")

    st.markdown('</div>', unsafe_allow_html=True)

    if clicked:
        _handle_index_request(path_input)


def _render_github_repository():
    """
    Lets the user paste a GitHub URL, clones it, then indexes it.
    """

    github_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/owner/repo",
        label_visibility="collapsed"
    )

    st.markdown('<div class="rm-primary-btn">', unsafe_allow_html=True)

    clicked = primary_button("Clone & Index Repository", key="index_github")

    st.markdown('</div>', unsafe_allow_html=True)

    if clicked:

        cloner = RepositoryCloner()

        if not cloner.validate_url(github_url):
            error("Invalid GitHub repository URL.")
            return

        repo_name = cloner.get_repo_name(github_url)

        with st.spinner(f"Cloning {repo_name}..."):
            cloned = cloner.clone_repository(github_url)

        if not cloned:
            error("Failed to clone repository.")
            return

        local_path = str(
            Path("data") / "repositories" / repo_name
        )

        _handle_index_request(local_path)


def _handle_index_request(path_str: str):
    """
    Validates the given path and runs indexing against it,
    updating session state with the results.
    """

    if not path_str or not path_str.strip():
        error("Please provide a repository path.")
        return

    repo_path = Path(path_str.strip())

    if not repo_path.exists() or not repo_path.is_dir():
        error(f"Path not found: {repo_path}")
        return

    indexer = get_indexer()

    with st.spinner(f"Indexing {repo_path.name}..."):

        try:
            stats = indexer.index_repository(str(repo_path))

        except Exception as e:
            error(f"Indexing failed: {e}")
            return

    st.session_state.repo_path = str(repo_path)
    st.session_state.repo_name = repo_path.name
    st.session_state.is_indexed = True
    st.session_state.index_stats = {
        "files": stats["files_scanned"],
        "chunks": stats["total_chunks"]
    }

    success(f"Indexed {repo_path.name}: {stats['total_chunks']} chunks stored.")

    st.rerun()
