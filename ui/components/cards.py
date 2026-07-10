import html
import streamlit as st


def repository_card(
    name: str,
    path: str = "",
    status: str = "Ready"
):
    """
    Compact repository summary card: name, path, and a status pill.
    Used in the sidebar once a repository has been indexed.
    """

    safe_name = html.escape(name)
    safe_path = html.escape(path)

    st.markdown(
        f"""
<div class="rm-repo-card">
    <div class="rm-repo-card-name">{safe_name}</div>
    <div class="rm-repo-card-path">{safe_path}</div>
    <div class="rm-status-pill">
        <span class="rm-status-dot rm-status-dot--green"></span>{status}
    </div>
</div>
""",
        unsafe_allow_html=True
    )


def repository_card_empty(message: str = "No repository indexed yet."):
    """Placeholder shown before any repository has been indexed."""

    st.markdown(
        f'<div class="rm-repo-card-empty">{html.escape(message)}</div>',
        unsafe_allow_html=True
    )


def source_card(
    filename: str,
    score: float | None = None
):
    """Display a single retrieved source file, with an optional similarity score."""

    safe_name = html.escape(filename)
    score_html = f'<span class="rm-source-score">{score:.0%} match</span>' if score is not None else ""

    st.markdown(
        f"""
<div class="rm-source-item">
    <span class="rm-source-name">{safe_name}</span>
    {score_html}
</div>
""",
        unsafe_allow_html=True
    )
