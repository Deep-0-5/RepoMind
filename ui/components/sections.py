import streamlit as st


def section_title(
    title: str,
    icon: str = ""
):
    """Render a section title. Icon is optional and kept subtle."""

    if icon:
        st.subheader(f"{icon}  {title}")
    else:
        st.subheader(title)


def section_label(text: str):
    """Small uppercase label used to head sidebar sections."""

    st.markdown(
        f'<div class="rm-section-label">{text}</div>',
        unsafe_allow_html=True
    )


def divider(subtle: bool = False):
    """Render a divider. `subtle=True` gives a thinner, low-emphasis rule."""

    if subtle:
        st.markdown('<hr class="rm-divider-subtle" />', unsafe_allow_html=True)
    else:
        st.divider()
