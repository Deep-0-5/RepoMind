import streamlit as st


def metric_card(
    label: str,
    value,
    delta=None
):
    """Render a metric card (plain, neutral — no accent coloring)."""

    st.metric(
        label=label,
        value=value,
        delta=delta
    )


def status_badge(
    status: str,
    color: str = "green"
):
    """Display a status pill with a small colored dot (no emoji)."""

    valid_colors = {"green", "yellow", "red", "gray"}
    dot_color = color if color in valid_colors else "gray"

    st.markdown(
        f"""
<span class="rm-status-pill">
    <span class="rm-status-dot rm-status-dot--{dot_color}"></span>{status}
</span>
""",
        unsafe_allow_html=True
    )
