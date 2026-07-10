import streamlit as st
from pathlib import Path


STYLES_PATH = Path(__file__).parent / "assets" / "styles.css"

LIGHT_VARS = """
:root {
    --rm-bg: #ffffff;
    --rm-surface: #f9fafb;
    --rm-surface-hover: #f3f4f6;
    --rm-sidebar-bg: #fafafa;
    --rm-text: #18181b;
    --rm-text-secondary: #71717a;
    --rm-text-tertiary: #a1a1aa;
    --rm-border: #e4e4e7;
    --rm-border-strong: #d4d4d8;
    --rm-accent: #2563eb;
    --rm-accent-hover: #1d4ed8;
    --rm-accent-soft: #eff6ff;
    --rm-success: #16a34a;
    --rm-success-soft: #f0fdf4;
    --rm-error: #dc2626;
    --rm-error-soft: #fef2f2;
    --rm-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
    --rm-shadow-md: 0 2px 8px rgba(16, 24, 40, 0.06);
}
"""

DARK_VARS = """
:root {
    --rm-bg: #0a0a0b;
    --rm-surface: #151517;
    --rm-surface-hover: #1c1c1f;
    --rm-sidebar-bg: #0d0d0f;
    --rm-text: #e4e4e7;
    --rm-text-secondary: #a1a1aa;
    --rm-text-tertiary: #71717a;
    --rm-border: #26262a;
    --rm-border-strong: #333338;
    --rm-accent: #3b82f6;
    --rm-accent-hover: #60a5fa;
    --rm-accent-soft: #12233f;
    --rm-success: #22c55e;
    --rm-success-soft: #052e16;
    --rm-error: #ef4444;
    --rm-error-soft: #2a0f0f;
    --rm-shadow: 0 1px 2px rgba(0, 0, 0, 0.24);
    --rm-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.32);
}
"""


def apply_theme():
    """
    Injects the design-system CSS, using the variable block that
    matches the currently selected theme (light/dark).
    """

    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    variables = (
        DARK_VARS
        if st.session_state.theme == "dark"
        else LIGHT_VARS
    )

    css = STYLES_PATH.read_text()

    st.markdown(
        f"<style>{variables}\n{css}</style>",
        unsafe_allow_html=True
    )


def toggle_theme():
    """
    Flips between light and dark theme.
    """

    st.session_state.theme = (
        "light" if st.session_state.theme == "dark" else "dark"
    )
