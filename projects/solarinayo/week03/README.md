# Week 3 — AI Writing Assistant (sample)

**Student:** solarinayo

## What I built

Four jobs on one paragraph: generate, summarise, rewrite, improve. I compared Gemini and Grok on the same Pidgin sentence.

## Who it helps

Students who draft WhatsApp English and need a cleaner version for school.

## How to run it

```bash
python week03-llm-apis/gradio_app.py
```

Or the notebook: `week03-llm-apis/day3.ipynb` (kernel = `.venv`).

Keys: `GEMINI_API_KEY` in the **course** `.env`. Never copy `.env` into this folder.

## What was hard

Grok returned a 401 until I matched `GROK_MODEL` to the name in the xAI dashboard. Latency on Gemini was ~800 ms; Ollama was slower on first call (cold start).

## What I would improve

A “do not change meaning” checkbox. Measure inconsistency: run improve three times.

## Test table (fill yours with real numbers)

| Provider | ok? | latency_ms | notes |
|---|---|---|---|
| gemini | yes | ~800 | default classroom |
| grok | skip if no key | — | compare tone |
| ollama | yes | ~4000 first time | no internet key |
