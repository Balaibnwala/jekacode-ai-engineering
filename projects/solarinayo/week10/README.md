# Week 10 — Deploy notes (sample)

**Student:** solarinayo

## What I built

A checklist for putting the Study Assistant (Week 4) on a public URL. Secrets stay on the host, not in git.

## Who it helps

Auntie on WhatsApp who will not install Python.

## How to run it (local first)

```bash
python week10-deploy/gradio_app.py
streamlit run week04-ai-apps/study_assistant.py
```

## What was hard

Almost committed `.env`. `git status` saved me. Cloud cannot see laptop Ollama — need Gemini or Grok in Secrets.

## What I would improve

A fallback: if Gemini 429s, switch dropdown to Grok.

## Deploy checklist

| Item | Sample |
|---|---|
| App name | Jekacode Study Assistant |
| GitHub | `projects/solarinayo/` (this folder) |
| Live URL | *paste after you deploy* (Streamlit Cloud or HF Space) |
| Tester should try | Explain photosynthesis · switch model · phone data |
| First break | Logo 404 until I used the repo `assets/` path |
| Phone latency | *measure with a stopwatch* (cold start is slow) |

**Secrets on the host (names only):** `GEMINI_API_KEY` — never paste the value in this README.
