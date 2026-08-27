"""Week 7 Gradio — research-style report (agent flavour: admit unknowns).

How to run:
    python week07-agents/gradio_app.py
Full two-tool agent: streamlit run week07-agents/research_assistant.py
Keys: guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 7 · Research report (Gradio)",
    system=(
        "You are a research intern. Use headings: Goal, What we know, What we do not know, Next step. "
        "If you lack facts, say so. Do not invent citations."
    ),
    placeholder="Write a briefing on JAMB for a parent in 8 lines.",
)
