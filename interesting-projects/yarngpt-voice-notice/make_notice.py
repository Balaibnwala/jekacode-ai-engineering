"""Draft a school voice notice in a Nigerian language (text).

YarnGPT (Hugging Face) can turn similar text into speech in a Colab/Space.
This script is the part that always runs in a Jekacode classroom.

How to run (course root):
    python interesting-projects/yarngpt-voice-notice/make_notice.py
Gradio twin:
    python week09-african-problems/gradio_app.py
Keys: guides/HOW_TO.md
Models: https://huggingface.co/saheedniyi/YarnGPT-local
"""

import sys
from pathlib import Path

# This file sits two folders below the course root.
sys.path.append(str(Path(__file__).resolve().parents[2]))

from jekacode.ai import ask  # Gemini drafts text; YarnGPT is voice later

SYSTEM = (
    "You write short school PA announcements for Nigerian parents. "
    "If the user asks for Yoruba, Igbo, Hausa, or Pidgin, write in that language. "
    "Keep under 80 words. No Latin you did not mean. "
    "If you are unsure of a phrase, add [check with a speaker] on its own line."
)


def main() -> None:
    english = input("Notice in English: ").strip()  # input() = type in the terminal
    language = input("Language (Yoruba / Igbo / Hausa / Pidgin): ").strip()
    print(
        ask(
            f"Translate and polish this announcement into {language}:\n{english}",
            provider="gemini",
            system=SYSTEM,
        )
    )
    print("\nNext: paste into YarnGPT-local demo for voice if the teacher has Colab open.")
    print("Models: https://huggingface.co/saheedniyi/YarnGPT-local")


if __name__ == "__main__":
    main()
