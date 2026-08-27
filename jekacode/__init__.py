"""Shared helpers for the Jekacode AI Engineering programme."""

from .ai import (
    ask,
    ask_deepseek,
    ask_gemini,
    ask_grok,
    ask_huggingface,
    ask_ollama,
    ask_timed,
    chat,
)
from .brand import GREEN, LOGO, NAVY

__all__ = [
    "ask",
    "ask_gemini",
    "ask_grok",
    "ask_deepseek",
    "ask_ollama",
    "ask_huggingface",
    "ask_timed",
    "chat",
    "NAVY",
    "GREEN",
    "LOGO",
]
