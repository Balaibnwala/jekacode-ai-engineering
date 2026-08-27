"""Week 3 Gradio — writing helper (generate / summarise / rewrite).

How to run (course root, venv on):
    python week03-llm-apis/gradio_app.py
Keys: guides/HOW_TO.md  (Gemini at minimum)
"""

import sys
from pathlib import Path

# Course root on sys.path so import jekacode works.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 3 · Writing assistant (Gradio)",
    system=(
        "You are a writing coach for African students. Simple English. "
        "If asked to improve, keep the meaning. Do not invent citations."
    ),
    placeholder="Paste a paragraph to summarise, rewrite, or improve.",
)
