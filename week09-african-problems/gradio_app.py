"""Week 9 Gradio — local-language notice (text). YarnGPT is for voice later.

How to run:
    python week09-african-problems/gradio_app.py
Terminal twin: python interesting-projects/yarngpt-voice-notice/make_notice.py
YarnGPT models: https://huggingface.co/saheedniyi/YarnGPT
Keys: guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 9 · Local language notice (Gradio)",
    system=(
        "Write short school or community notices. "
        "If asked for Yoruba, Igbo, Hausa, or Pidgin, write in that language. "
        "Add [check with a speaker] if you are unsure. Under 80 words."
    ),
    placeholder="English notice: Assembly moved to 8:15am tomorrow. Translate to Yoruba.",
)
