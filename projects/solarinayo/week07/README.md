# Week 7 — Research Assistant (sample)

**Student:** solarinayo

## What I built

An agent loop: outline tasks (LLM) → search the Jekacode handbook (Python) → report with “what we still don’t know.”

## Who it helps

A parent who wants a short briefing on the programme, not a fake citation.

## How to run it

```bash
streamlit run week07-agents/research_assistant.py
python week07-agents/gradio_app.py
```

## What was hard

Run 2 produced a different outline (**inconsistency**). I fixed headings in the system prompt.

## What I would improve

A second tool: `notes_search` for JAMB facts. Log every tool result in the README.

## Where AI sits

`outline()` and the final report. `search_handbook()` is deterministic Python.
