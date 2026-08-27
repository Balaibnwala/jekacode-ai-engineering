# Step 4 — Ollama first (AI on your laptop)

**Full novice walkthrough (install + Python + errors):** [../guides/HOW_TO.md](../guides/HOW_TO.md) section 1.

This is the **instant gratification** start: you talk to a model **before** cloud keys.

Ollama is a free app. It downloads a small open-source model onto your computer. No OpenAI. No OpenRouter.

## Why start here?

| Path | Needs internet key? | Good for |
|---|---|---|
| **Ollama** | No (after download) | First wow, privacy, class demo if Wi‑Fi dies |
| Gemini | Yes (free AI Studio) | Strong answers, Week 3+ |
| DeepSeek | Yes | Compare with Gemini |
| Hugging Face | Optional token | Finding African models, YarnGPT, Spaces |

**Trade-off:** Ollama on a weak laptop is slower and less smart than Gemini. That is OK. You are learning the *pipe*, not winning a leaderboard.

## Install

1. Open [https://ollama.com](https://ollama.com)
2. Download for Mac or Windows
3. Install. On Windows you may need **Run as administrator**

## First chat in Terminal

**Mac:** Terminal · **Windows:** PowerShell or Command Prompt

```bash
ollama run llama3.2
```

Small machine? Try:

```bash
ollama run llama3.2:1b
```

Do **not** start with a 70B model. It will freeze a normal laptop.

If it fails, open a **second** terminal and run `ollama serve`, then try `ollama run llama3.2` again.

Type: `Explain Jekacode like I am 12.` Then `/bye` to quit.

## From Python (Week 1 Class 3 / Week 3)

Ollama listens on your machine like a tiny restaurant:

```
Your notebook  →  http://localhost:11434  →  llama3.2  →  reply
```

After setup, `from jekacode.ai import ask` then `ask("Hello", provider="ollama")`.

## If your computer cannot run it

Use Google Colab (free Google account) as backup later. Classroom default remains Gemini once keys exist.

Next: [04_api_keys.md](04_api_keys.md) (can wait until Week 3) or [06_huggingface.md](06_huggingface.md).
