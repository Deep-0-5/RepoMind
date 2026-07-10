import streamlit as st


def chat_message(role: str, message: str):
    """
    Render a single chat turn.

    - User turns render as a compact bubble, right-aligned — same
      pattern as any modern chat app.
    - Assistant turns render as plain left-aligned text with a small
      role label instead of a boxed bubble, so a long answer reads
      like an actual AI response rather than being squeezed into a
      chat-log row. This also sidesteps Streamlit's default avatar
      icons, which render as jarring red/orange circles in dark mode.
    """

    if role == "user":
        st.markdown(
            '<div class="rm-chat-turn">'
            '<div class="rm-chat-user-row">'
            '<div class="rm-chat-user-bubble">',
            unsafe_allow_html=True
        )
        st.markdown(message)
        st.markdown('</div></div></div>', unsafe_allow_html=True)

    else:
        st.markdown(
            '<div class="rm-chat-turn">'
            '<div class="rm-chat-assistant-row">'
            '<div class="rm-chat-assistant-wrap">'
            '<div class="rm-chat-role-label">'
            '<span class="rm-chat-role-mark">R</span>RepoMind'
            '</div>'
            '<div class="rm-chat-assistant-body">',
            unsafe_allow_html=True
        )
        st.markdown(message)
        st.markdown('</div></div></div></div>', unsafe_allow_html=True)
