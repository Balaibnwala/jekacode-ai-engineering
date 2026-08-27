"""Talk to classroom models: Gemini, Grok, DeepSeek, Ollama, Hugging Face.

Line-by-line story (read this once):

1. load_dotenv()        — read secrets from the .env file so keys are not in the code
2. ask("...")           — one door for students; pick a provider
3. ask_ollama           — your laptop, no internet key (Ollama must be running)
4. ask_gemini           — Google AI Studio (Gemini)
5. ask_grok             — xAI Grok
6. ask_deepseek         — DeepSeek
7. ask_huggingface      — optional HF token

User story: As a beginner, I want one function named ask() so I do not copy-paste HTTP code every week.
"""

from __future__ import annotations  # lets us write str | None on older Python

import os  # read environment variables (the keys from .env)
import time  # stopwatch for latency (ask_timed)
from typing import Any, Literal  # Literal = only these provider names are allowed

import requests  # HTTP — how we talk to Gemini, Grok, Ollama
from dotenv import load_dotenv  # reads the .env file into os.environ

load_dotenv()  # run once at import: keys are available, never committed to GitHub

Provider = Literal["gemini", "grok", "deepseek", "ollama", "huggingface"]

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
GROK_MODEL = os.getenv("GROK_MODEL", "grok-3-mini")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
HF_MODEL = os.getenv("HF_MODEL", "HuggingFaceH4/zephyr-7b-beta")
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
GROK_URL = "https://api.x.ai/v1/chat/completions"


def _require(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value or value.startswith("paste_your_"):
        raise ValueError(
            f"Missing {name}. Copy .env.example to .env and paste your key. "
            "Setup guide: setup/04_api_keys.md"
        )
    return value


def ask_gemini(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """Cloud Gemini. Needs GEMINI_API_KEY."""
    key = _require("GEMINI_API_KEY")
    chosen = model or GEMINI_MODEL
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{chosen}:generateContent?key={key}"
    )
    text = prompt if not system else f"{system}\n\nUser:\n{prompt}"
    response = requests.post(
        url,
        json={"contents": [{"parts": [{"text": text}]}]},
        timeout=90,
    )
    if response.status_code != 200:
        raise RuntimeError(f"Gemini error {response.status_code}: {response.text[:400]}")
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as error:
        raise RuntimeError(f"Unexpected Gemini response: {data}") from error


def _openai_style_chat(
    url: str,
    key: str,
    model: str,
    prompt: str,
    system: str | None,
    label: str,
) -> str:
    """Shared request shape used by DeepSeek and Grok (Chat Completions API)."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": model, "messages": messages},
        timeout=90,
    )
    if response.status_code != 200:
        raise RuntimeError(f"{label} error {response.status_code}: {response.text[:400]}")
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as error:
        raise RuntimeError(f"Unexpected {label} response: {data}") from error


def ask_grok(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """xAI Grok. Needs GROK_API_KEY from https://console.x.ai"""
    key = _require("GROK_API_KEY")
    return _openai_style_chat(
        GROK_URL, key, model or GROK_MODEL, prompt, system, "Grok"
    )


def ask_deepseek(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """DeepSeek API. Needs DEEPSEEK_API_KEY."""
    key = _require("DEEPSEEK_API_KEY")
    return _openai_style_chat(
        DEEPSEEK_URL, key, model or DEEPSEEK_MODEL, prompt, system, "DeepSeek"
    )


def ask_ollama(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """Local model on your computer. Install Ollama first (setup/05_ollama.md)."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        response = requests.post(
            OLLAMA_URL,
            json={"model": model or OLLAMA_MODEL, "messages": messages, "stream": False},
            timeout=180,
        )
    except requests.ConnectionError as error:
        raise RuntimeError(
            "Ollama is not running. Install from https://ollama.com then run: ollama run llama3.2"
        ) from error
    if response.status_code != 200:
        raise RuntimeError(f"Ollama error {response.status_code}: {response.text[:400]}")
    data = response.json()
    if "message" in data and "content" in data["message"]:
        return data["message"]["content"]
    raise RuntimeError(f"Unexpected Ollama response: {data}")


def ask_huggingface(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """Hugging Face Inference. Needs HF_TOKEN from https://huggingface.co/settings/tokens"""
    token = _require("HF_TOKEN")
    chosen = model or HF_MODEL
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={"model": chosen, "messages": messages, "max_tokens": 400},
        timeout=120,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"Hugging Face error {response.status_code}: {response.text[:400]}\n"
            "Browse models at https://huggingface.co/models — or use provider='ollama'."
        )
    return response.json()["choices"][0]["message"]["content"]


def ask(prompt: str, provider: Provider = "gemini", system: str | None = None) -> str:
    """One door for students. provider picks the kitchen; system= is the job description."""
    if provider == "gemini":
        return ask_gemini(prompt, system=system)
    if provider == "grok":
        return ask_grok(prompt, system=system)
    if provider == "deepseek":
        return ask_deepseek(prompt, system=system)
    if provider == "ollama":
        return ask_ollama(prompt, system=system)
    if provider == "huggingface":
        return ask_huggingface(prompt, system=system)
    raise ValueError("provider must be gemini, grok, deepseek, ollama, or huggingface")


def ask_timed(
    prompt: str,
    provider: Provider = "gemini",
    system: str | None = None,
) -> dict[str, Any]:
    """Same as ask(), plus latency (how long you waited, in milliseconds).

    Behind the scenes: time.perf_counter() starts, ask() runs, we subtract and × 1000.
    """
    started = time.perf_counter()
    error = None
    text = ""
    try:
        text = ask(prompt, provider=provider, system=system)
    except Exception as exc:  # noqa: BLE001 — we want the timing even on failure
        error = str(exc)
    elapsed_ms = round((time.perf_counter() - started) * 1000, 1)
    return {
        "provider": provider,
        "text": text,
        "latency_ms": elapsed_ms,
        "ok": error is None,
        "error": error,
    }


def chat(
    messages: list[dict[str, str]],
    provider: Provider = "gemini",
    system: str | None = None,
) -> str:
    """Continue a conversation. messages: [{role, content}, ...]"""
    if provider == "ollama":
        payload = list(messages)
        if system:
            payload = [{"role": "system", "content": system}, *payload]
        response = requests.post(
            OLLAMA_URL,
            json={"model": OLLAMA_MODEL, "messages": payload, "stream": False},
            timeout=180,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

    if provider == "huggingface":
        last = messages[-1]["content"] if messages else ""
        return ask_huggingface(last, system=system)

    if provider in ("deepseek", "grok"):
        if provider == "deepseek":
            key = _require("DEEPSEEK_API_KEY")
            url, model, label = DEEPSEEK_URL, DEEPSEEK_MODEL, "DeepSeek"
        else:
            key = _require("GROK_API_KEY")
            url, model, label = GROK_URL, GROK_MODEL, "Grok"
        payload_messages = []
        if system:
            payload_messages.append({"role": "system", "content": system})
        payload_messages.extend(messages)
        response = requests.post(
            url,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={"model": model, "messages": payload_messages},
            timeout=90,
        )
        if response.status_code != 200:
            raise RuntimeError(f"{label} error {response.status_code}: {response.text[:400]}")
        return response.json()["choices"][0]["message"]["content"]

    key = _require("GEMINI_API_KEY")
    contents = []
    if system:
        contents.append({"role": "user", "parts": [{"text": f"System instructions:\n{system}"}]})
        contents.append({"role": "model", "parts": [{"text": "Understood. I will follow these instructions."}]})
    for message in messages:
        role = "user" if message["role"] == "user" else "model"
        contents.append({"role": role, "parts": [{"text": message["content"]}]})
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={key}"
    )
    response = requests.post(url, json={"contents": contents}, timeout=90)
    if response.status_code != 200:
        raise RuntimeError(f"Gemini error {response.status_code}: {response.text[:400]}")
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
