import streamlit as st
from ui.theme import toggle_theme
from ui.components import divider


def render_header():
    """
    Render the application's top bar.
    """

    left, right = st.columns([6, 1])

    with left:

        st.markdown(
            """
<div style="display:flex; align-items:baseline; gap:0.6rem;">
    <span style="font-size:1.8rem; font-weight:700;">🚀 RepoMind</span>
    <span class="rm-badge">v1.1</span>
</div>
<div style="color:var(--rm-text-secondary); font-size:0.95rem; margin-top:0.15rem;">
    AI-powered repository assistant &mdash; RAG · Sentence Transformers · ChromaDB · Gemini
</div>
""",
            unsafe_allow_html=True
        )

    with right:

        icon = "🌙" if st.session_state.theme == "light" else "☀️"

        st.markdown('<div class="rm-theme-toggle">', unsafe_allow_html=True)

        if st.button(icon, key="theme_toggle"):
            toggle_theme()
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.is_indexed:

        st.markdown(
            f'<div style="margin-top:0.5rem;">'
            f'<span class="rm-badge">📂 {st.session_state.repo_name}</span>'
            f'&nbsp;&nbsp;'
            f'<span class="rm-badge">'
            f'{st.session_state.index_stats["files"]} files · '
            f'{st.session_state.index_stats["chunks"]} chunks'
            f'</span></div>',
            unsafe_allow_html=True
        )

    st.divider()
