"""Week 10 Gradio — practise the UI you might put on a Hugging Face Space.

How to run locally:
    python week10-deploy/gradio_app.py
How to deploy: guides/HOW_TO.md section 12 (HF Space, SDK=Gradio, Secrets=GEMINI_API_KEY)
Keys: never commit .env
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 10 · Deployable Gradio",
    system=(
        "You are a Jekacode tutor. Short answers. If you lack a fact, say so. "
        "This app is meant to run on a public URL — no secrets in the reply."
    ),
    placeholder="Explain what a cold start is, like I am 12.",
)
