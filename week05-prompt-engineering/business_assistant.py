"""AI Business Assistant — Week 5 project.

What we achieve
    One SME description in. Four drafts out (Instagram, LinkedIn, product text, email).
    A human still posts. The model must not invent prices or phone numbers.

How to run (course root, venv on)
    streamlit run week05-prompt-engineering/business_assistant.py
How to get keys
    guides/HOW_TO.md  (Gemini, Grok, Ollama)
Gradio twin
    python week05-prompt-engineering/gradio_app.py
"""

# sys = Python's system toolbox. We need it to change where imports are found.
import sys

# Path = folders that work the same on Mac and Windows.
from pathlib import Path

# __file__ is this .py file. .parents[1] is the course root (where jekacode/ lives).
# append() adds that folder to the import search list.
sys.path.append(str(Path(__file__).resolve().parents[1]))

# streamlit draws a website from Python. We nickname it st.
import streamlit as st

# ask() is one door to Gemini / Grok / DeepSeek / Ollama.
from jekacode.ai import ask

# banner paints the Jekacode logo + navy/green title.
from jekacode.ui import banner

# SYSTEM is a system prompt: standing orders on every button.
# Constraints fight hallucination (fake naira, fake WhatsApp numbers).
SYSTEM = (
    "You are a practical marketing assistant for Nigerian and African small businesses. "
    "Simple English. No fake American slang. Do not invent prices or phone numbers."
)

# layout="wide" uses more of the screen. Call banner before other widgets.
banner(st, "AI Business Assistant", "One business. Four useful drafts. Human still posts them.", layout="wide")

# text_input = one line. The return value is a string (maybe empty).
kind = st.text_input("What business is this?", placeholder="Phone repair shop in Computer Village")

# text_area = many lines for a longer offer description.
offer = st.text_area("What do they sell or do?", placeholder="Screen replacement, battery, software")

# selectbox = dropdown. The chosen string is passed to ask(provider=...).
provider = st.selectbox("Model", ["gemini", "grok", "deepseek", "ollama"])

# Button click AND a non-empty kind. Empty business name would waste API calls (cost + latency).
if st.button("Generate pack") and kind:
    # f-string stitches the two boxes into one brief for all four asks.
    brief = f"Business: {kind}\nOffer: {offer}"
    # columns(2) = two side-by-side panels.
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Instagram")
        # Each ask() is a separate inference = separate latency and a separate chance to hallucinate.
        st.write(ask(f"Write 1 Instagram post with 5 hashtags.\n{brief}", provider=provider, system=SYSTEM))
        st.subheader("LinkedIn")
        st.write(ask(f"Write a short LinkedIn post for this SME.\n{brief}", provider=provider, system=SYSTEM))
    with cols[1]:
        st.subheader("Product description")
        st.write(ask(f"Write a 80-word product/service description.\n{brief}", provider=provider, system=SYSTEM))
        st.subheader("Email")
        st.write(ask(f"Write a polite marketing email under 120 words.\n{brief}", provider=provider, system=SYSTEM))
