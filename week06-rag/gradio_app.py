"""Week 6 Gradio — paste handbook text, ask a question (tiny RAG in one box).

How to run:
    python week06-rag/gradio_app.py
Full Streamlit RAG (chunk + rank): document_assistant.py
Keys: guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 6 · Document Q&A (Gradio)",
    system=(
        "You answer ONLY from the text the user pastes. "
        "If the answer is not there, say you cannot find it. Do not hallucinate fees."
    ),
    placeholder="Paste handbook text, then your question underneath.",
)
