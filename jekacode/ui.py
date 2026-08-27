"""Tiny Streamlit chrome so every classroom app looks like Jekacode.

import story: banner() is called first in each Streamlit app.
It sets the tab title, shows the official logo, and the navy/green heading.
"""

from __future__ import annotations

from .brand import LOGO  # path to assets/jekacode-logo.png


def banner(st, title: str, caption: str | None = None, layout: str = "centered") -> None:
    """st is the streamlit module. We pass it in so this file does not import Streamlit twice."""
    options = {"page_title": title, "layout": layout}
    if LOGO.exists():
        options["page_icon"] = str(LOGO)  # favicon in the browser tab
    st.set_page_config(**options)  # must run before other Streamlit widgets
    if LOGO.exists():
        st.image(str(LOGO), width=220)
    st.title(title)
    if caption:
        st.caption(caption)
