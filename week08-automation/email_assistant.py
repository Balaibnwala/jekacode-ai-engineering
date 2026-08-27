"""AI Email Assistant — Week 8 Python path (n8n is the optional visual twin).

What we achieve
    Paste a message → model prints LABEL then a draft. A human still sends.
    Never auto-refund. Test inconsistency: same mail, two LABELs?

How to run
    streamlit run week08-automation/email_assistant.py
Gradio twin
    python week08-automation/gradio_app.py
n8n
    Import n8n-email-assistant.json if you installed n8n (guides/HOW_TO.md section 11).
Keys
    guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st  # the form
from jekacode.ai import ask  # one HTTP hop to the model
from jekacode.ui import banner

# First line is structured on purpose so a later automation node can filter.
SYSTEM = (
    "You are a support assistant for African SMEs. "
    "First line: LABEL: QUESTION|COMPLAINT|PRAISE|SPAM. "
    "Then a draft reply a human can edit. Never send; humans send."
)

banner(st, "AI Email Assistant", "New message → classify → draft → human review")

incoming = st.text_area("Paste an email", height=220)
provider = st.selectbox("Model", ["gemini", "grok", "deepseek", "ollama"])
if st.button("Process") and incoming:
    # One ask(): classify + draft together. Trigger was the button click.
    st.write(ask(incoming, provider=provider, system=SYSTEM))
