import streamlit as st

from ui.header import render_header
from ui.sidebar import render_sidebar
from ui.chat import render_chat
from ui.footer import render_footer
from ui.state import init_session_state
from ui.theme import apply_theme


st.set_page_config(
    page_title="RepoMind",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():

    init_session_state()

    apply_theme()

    render_header()

    render_sidebar()

    render_chat()

    render_footer()


if __name__ == "__main__":
    main()