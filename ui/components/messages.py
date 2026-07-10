import html
import streamlit as st


def info(message: str):
    """Render an info message."""
    st.info(message)


def success(message: str):
    """Render a success message."""
    st.success(message)


def warning(message: str):
    """Render a warning message."""
    st.warning(message)


def error(message: str):
    """Render an error message."""
    st.error(message)


def empty_state(
    title: str,
    message: str,
    icon: str = ""
):
    """Render a calm, centered empty state — used before any content exists."""

    body_html = message.strip().replace("\n\n", "<br><br>").replace("\n", "<br>")
    title_html = f"{icon}  {html.escape(title)}" if icon else html.escape(title)

    st.markdown(
        f"""
<div class="rm-empty-state">
    <div class="rm-empty-state-title">{title_html}</div>
    <div class="rm-empty-state-body">{body_html}</div>
</div>
""",
        unsafe_allow_html=True
    )


def loading_card(message: str):
    """Display loading spinner."""

    with st.spinner(message):
        pass
