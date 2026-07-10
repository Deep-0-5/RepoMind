import streamlit as st


def render_footer():

    st.divider()

    st.markdown(
        '<div class="rm-footer">RepoMind &middot; Streamlit &middot; Gemini &middot; '
        'Sentence Transformers &middot; ChromaDB</div>',
        unsafe_allow_html=True
    )
