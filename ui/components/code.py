import streamlit as st


def code_block(
    code: str,
    language: str = "python"
):
    """Display syntax highlighted code."""

    st.code(
        code,
        language=language
    )