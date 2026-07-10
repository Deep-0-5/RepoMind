import streamlit as st

from ui.components import (
    divider,
    empty_state,
    section_title,
    chat_message,
    source_card,
    error,
)
from ui.state import get_chat_engine, get_active_conversation, add_message


def render_chat():

    section_title("Ask RepoMind")

    conversation = get_active_conversation()
    messages = conversation["messages"] if conversation else []

    chat_container = st.container(height=460, border=True)

    with chat_container:

        if messages:

            for turn in messages:
                chat_message(turn["role"], turn["content"])

        else:

            empty_state(
                "Ready to chat",
                """
Select or index a repository first.

Then ask questions like:

• Explain this project
• Where is login implemented?
• Summarize the repository
• Find API endpoints
"""
            )

    divider(subtle=True)

    section_title("Source Files")

    sources = conversation.get("sources", []) if conversation else []

    if sources:

        for source in sources:
            source_card(
                source.get("path", "unknown"),
                score=source.get("score")
            )

    else:
        st.markdown(
            '<div class="rm-source-empty">No sources retrieved yet.</div>',
            unsafe_allow_html=True
        )

    prompt = st.chat_input(
        "Ask anything about your repository..."
        if st.session_state.is_indexed
        else "Index a repository first to start chatting",
        disabled=not st.session_state.is_indexed
    )

    if prompt:
        _handle_ask(prompt)
        st.rerun()


def _handle_ask(question: str):
    """
    Runs the question through the RAG pipeline and
    appends the exchange to the active conversation.
    """

    chat_engine = get_chat_engine()
    conversation = get_active_conversation()

    add_message("user", question)

    # Build conversation history for context-aware answers
    history = []
    if conversation and conversation.get("messages"):
        # Include last 10 messages (5 turns) for context
        recent = conversation["messages"][-10:]
        history = [
            {"role": m["role"], "content": m["content"]}
            for m in recent
        ]

    with st.spinner("Thinking..."):

        try:
            answer, sources = chat_engine.ask(
                question, history=history
            )

        except Exception as e:
            error(f"Something went wrong: {e}")
            add_message(
                "assistant",
                "Sorry, I ran into an error answering that. Please try again."
            )
            return

    add_message("assistant", answer, sources=sources)
