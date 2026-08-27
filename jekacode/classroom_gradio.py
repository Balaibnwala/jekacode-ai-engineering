# --- Why this file exists ---
# Gradio builds a website from a Python function. You do not write HTML here.
# launch() is reused by week05–week12 gradio_app.py files.

# How to run from the course root (venv on):
#     python week05-prompt-engineering/gradio_app.py
# Keys / Ollama: guides/HOW_TO.md
# Behind the scenes: Gradio starts a local server → browser is frontend →
# reply() calls ask() → second hop to Gemini/Grok/Ollama.

from __future__ import annotations

import sys
from pathlib import Path

# This file lives in the jekacode package, so the course root is one folder up.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import gradio as gr  # draws the UI
from jekacode.ai import ask  # talks to Gemini / Grok / DeepSeek / Ollama


def launch(title: str, system: str, placeholder: str = "Type a question…") -> None:
    """Open a local web page with a text box, a model picker, and an answer box."""

    def reply(message: str, provider: str) -> str:
        # Called when the student clicks Submit.
        if not (message or "").strip():
            return "Type something first. Empty prompts still cost latency."
        # system= is the job description. message= is today's question.
        return ask(message, provider=provider, system=system)

    demo = gr.Interface(
        fn=reply,  # which Python function to run
        inputs=[
            gr.Textbox(label="Your text", lines=6, placeholder=placeholder),
            gr.Dropdown(
                ["gemini", "grok", "deepseek", "ollama"],
                value="gemini",
                label="Model (kitchen)",
            ),
        ],
        outputs=gr.Textbox(label="Model reply", lines=14),
        title=title,
        description="Jekacode Gradio UI. Same ask() as the notebooks. See guides/HOW_TO.md",
    )
    demo.launch()
