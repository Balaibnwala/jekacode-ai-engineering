"""Week 8 Gradio — classify + draft (human still sends).

How to run:
    python week08-automation/gradio_app.py
n8n optional: see guides/HOW_TO.md section 11
Keys: guides/HOW_TO.md
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jekacode.classroom_gradio import launch

launch(
    title="Jekacode · Week 8 · Email brain (Gradio)",
    system=(
        "First line: LABEL: QUESTION|COMPLAINT|PRAISE|SPAM. "
        "Then a calm draft. Never promise refunds. A human will send the mail."
    ),
    placeholder="Paste an angry or confused customer email.",
)
