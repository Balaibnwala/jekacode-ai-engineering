# MODULE 3 — Large Language Models & AI APIs

Official Jekacode format: **Outline · Tasks · Labs · Project**.  
**Three class files:** `day1.ipynb` (theory) · `day2.ipynb` (lab) · `day3.ipynb` (project).

Dictionary: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md) · Test models: [../guides/TEST_ALL_MODELS.md](../guides/TEST_ALL_MODELS.md)

## This week — novice guide

**What we want to achieve:** Explain API, key, token, context window, **latency**, **hallucination**, **inconsistency**. Call Gemini (and Grok if you have a key). Ship a Writing Assistant.

**Tools:** `.env` with `GEMINI_API_KEY`. Optional `GROK_API_KEY`, Ollama, DeepSeek.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) sections 1–4. Gradio writing box: `python week03-llm-apis/gradio_app.py`. Test kit: [../setup/test_all_models.ipynb](../setup/test_all_models.ipynb).

**What goes on behind the scenes:** Python **POSTs JSON** to an **endpoint**. The vendor runs inference and returns tokens. You wait (latency) and may pay for tokens. Ollama is the same idea on `localhost:11434`.

**Imports you will see:** `ask` (one door), `ask_timed` (stopwatch), `dotenv` (load `.env`).

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. What LLMs are
2. Gemini, Grok, GPT/Claude (names), open-source via Ollama
3. What an API is
4. API keys and .env
5. Python requests
6. System vs user prompts
7. Tokens, context windows, cost
8. Limitations: hallucination, inconsistency, latency

## Tasks

- Compare three models (Gemini, Grok, Ollama or DeepSeek)
- Prompts for summarise / generate / Q&A
- Estimate cost of an app (order of magnitude)
- Strengths and weaknesses table

## Labs

- Set up Gemini and optional Grok keys
- .env secrets
- First API call
- Short conversation
- Experiment with prompts and models
- Latency with ask_timed()

## Project

**AI Writing Assistant** — generate, summarise, rewrite, improve.

## Class files

| File | Class | What it is |
|---|---|---|
| `day1.ipynb` | 1 See it | Theory + terms |
| `day2.ipynb` | 2 Type it | Guided lab |
| `day3.ipynb` | 3 Ship it | Mini/capstone work for this week |

Test kit: [../setup/test_all_models.ipynb](../setup/test_all_models.ipynb) · [../visuals/latency.html](../visuals/latency.html) · [../visuals/api-architecture.html](../visuals/api-architecture.html)

Copy finished work into `projects/YOUR_NAME/week03/` and [open a PR](../guides/fork_push_pr.md) if asked.
