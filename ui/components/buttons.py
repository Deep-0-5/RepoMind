import streamlit as st


def primary_button(
    label: str,
    key: str | None = None,
    disabled: bool = False
) -> bool:
    """Render a primary button."""

    return st.button(
        label,
        key=key,
        use_container_width=True,
        disabled=disabled
    )


def secondary_button(
    label: str,
    key: str | None = None,
    disabled: bool = False
) -> bool:
    """Render a secondary button."""

    return st.button(
        label,
        key=key,
        type="secondary",
        use_container_width=True,
        disabled=disabled
    )