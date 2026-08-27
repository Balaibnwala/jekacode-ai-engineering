# Week 6 — Document Assistant / RAG (sample)

**Student:** solarinayo

## What I built

Q&A on `knowledge/school-handbook.md`. Chunk → rank by overlapping words → `ask()` with “only this context.”

## Who it helps

Parents who ask about transcripts and assembly — answers should come from the handbook, not a guessed fee.

## How to run it

```bash
streamlit run week06-rag/document_assistant.py
python week06-rag/gradio_app.py
```

## What was hard

The model invented a sports levy when I asked a fee that is **not** in the file. After a stronger system prompt it said it could not find it.

## What I would improve

Smaller chunks. Never paste real student data.

## Hallucination probe

| Question | Expected | What I got |
|---|---|---|
| How do I request a transcript? | From the handbook | Used the chunk (pass) |
| Secret 2099 sports levy in naira? | “Cannot find it” | First run invented ₦5,000 (fail) · second run refused (pass) |
