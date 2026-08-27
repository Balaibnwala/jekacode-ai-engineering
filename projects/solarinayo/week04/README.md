# Week 4 — Study Assistant (sample)

**Student:** solarinayo

## What I built

A study assistant with four jobs: explain, summarise, quiz, study plan. I ran **Streamlit** and also opened **Gradio** and the **HTML chat** so I know the three UI choices.

## Who it helps

The SS2 student from Week 1 — needs a screenshot-friendly explanation.

## How to run it

From the course root, `(.venv)` on:

```bash
streamlit run week04-ai-apps/study_assistant.py
python week04-ai-apps/gradio_chat.py
python week04-ai-apps/html-chatbot/server.py
```

HTML chat: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## What was hard

Clicking Explain twice while it said nothing — I paid two latencies. The HTML “Thinking…” bubble is there for that reason.

## What I would improve

A Pidgin tab. Deploy in Week 10.

## User story

As an SS2 student I want an explanation I can screenshot.

## Where AI sits

Only inside `ask()`. Tabs and buttons are ordinary Python.
