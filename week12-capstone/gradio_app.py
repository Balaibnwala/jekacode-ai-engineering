"""Week 12 Gradio — spare demo UI if your capstone is not Gradio yet.

How to run:
    python week12-capstone/gradio_app.py
Capstone still lives in projects/YOUR_NAME/capstone/
Keys: guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 12 · Capstone spare demo",
    system=(
        "You help a student demo their Jekacode capstone. "
        "Ask them where AI sits, what stays Python, and how they tested hallucination and latency. "
        "Do not claim they trained GPT."
    ),
    placeholder="In one paragraph: my capstone helps ___ by ___. AI sits in ___.",
)
