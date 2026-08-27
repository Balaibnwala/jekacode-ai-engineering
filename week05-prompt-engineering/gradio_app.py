"""Week 5 Gradio UI — same brain as the Streamlit business assistant.

What we achieve: a webpage with a box + model picker, no HTML file.
How to run (course root, venv on):
    python week05-prompt-engineering/gradio_app.py
Keys / Ollama: guides/HOW_TO.md
"""

# sys + Path: teach Python where the course root is.
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

# launch() lives in jekacode/classroom_gradio.py — shared Gradio form for many weeks.
from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 5 · Business drafts (Gradio)",
    # system= standing orders. Constraints reduce hallucinated prices.
    system=(
        "You help Nigerian SMEs. Simple English. Do not invent prices or phone numbers. "
        "If the user names a business, write Instagram, LinkedIn, a product blurb, and an email."
    ),
    placeholder="Phone repair shop in Computer Village. We replace screens.",
)
