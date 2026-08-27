"""Jekacode AI Study Assistant — Week 4 Streamlit project.

What we achieve
    A student types a topic. Gemini or Grok (or Ollama) explains, summarises,
    writes a quiz, or builds a study plan.

How to run
    streamlit run week04-ai-apps/study_assistant.py
How to get keys / Ollama
    guides/HOW_TO.md
"""

import sys
from pathlib import Path

# Add the course root so Python can find the jekacode package.
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st  # website widgets (tabs, buttons, boxes)
from jekacode.ai import ask  # send text to an LLM and get text back
from jekacode.ui import banner  # Jekacode logo + navy/green title

# TEACHER is a system prompt: standing orders for every button in this app.
TEACHER = (
    "You are a patient Jekacode tutor for African secondary and university students. "
    "Use simple English. Give Nigerian examples when they help. "
    "Never pretend to know a fact you are unsure about."
)

# layout="wide" uses more of the screen. banner must run before other Streamlit widgets.
banner(
    st,
    "Jekacode AI Study Assistant",
    "Explain · Summarize · Quiz · Study plan  ·  Gemini, Grok, Ollama",
    layout="wide",
)

# sidebar = the left column. selectbox = a dropdown. The choice is a string we pass to ask().
provider = st.sidebar.selectbox("Model", ["gemini", "grok", "deepseek", "ollama"])

# tabs() returns four containers. We fill each with its own inputs.
explain, summarize, quiz, plan = st.tabs(["Explain", "Summarize", "Quiz", "Study plan"])

with explain:
    topic = st.text_input("What topic is confusing?", placeholder="Photosynthesis")
    level = st.selectbox("Student level", ["JSS", "SSS / WAEC", "University beginner"])
    # key="ex" keeps this button unique from the other tabs' buttons.
    if st.button("Explain it", key="ex") and topic:
        # f-string inserts the student's words into the prompt.
        st.write(ask(f"Explain {topic} for a {level} student in 180 words.", provider=provider, system=TEACHER))

with summarize:
    notes = st.text_area("Paste notes or a page of text", height=200)
    if st.button("Summarize", key="sum") and notes:
        st.write(ask(f"Summarize these notes as 7 bullets and 1 exam tip:\n{notes}", provider=provider, system=TEACHER))

with quiz:
    subject = st.text_input("Subject and topic", placeholder="SS2 Government — federalism")
    n = st.slider("How many questions?", 3, 8, 5)
    if st.button("Make a quiz", key="quiz") and subject:
        st.write(ask(f"Create {n} short-answer quiz questions on {subject} with answers at the end.", provider=provider, system=TEACHER))

with plan:
    goal = st.text_input("What are you preparing for?", placeholder="JAMB Biology in 14 days")
    minutes = st.number_input("Minutes per day", min_value=20, max_value=180, value=45)
    if st.button("Build my plan", key="plan") and goal:
        st.write(ask(f"Make a realistic study plan. Goal: {goal}. Daily time: {minutes} minutes. Use a table.", provider=provider, system=TEACHER))
