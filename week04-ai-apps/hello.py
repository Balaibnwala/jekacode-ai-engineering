"""Week 4 — smallest Streamlit screen.

What this file is for
---------------------
Prove that Python can draw a website. No AI yet.

How to run (course root, venv on)
    streamlit run week04-ai-apps/hello.py
"""

# sys = system tools. We need it to add the course folder to Python's search list.
import sys

# Path lets us find folders on Mac and Windows the same way.
from pathlib import Path

# __file__ is "this hello.py file". .parent is week04-ai-apps. .parents[1] is the course root.
sys.path.append(str(Path(__file__).resolve().parents[1]))

# streamlit is a library that turns Python into a small website. We nickname it st.
import streamlit as st

# banner draws the Jekacode logo + title using official navy/green.
from jekacode.ui import banner

# This must be early: it sets the browser tab title and shows the logo.
banner(st, "Hello from Jekacode")

# text_input draws a box. The student's typing is stored in the variable name.
name = st.text_input("What is your name?")

# If the box is not empty, show a green success message.
if name:
    st.success(f"Welcome {name}. You just built a screen with Python.")
