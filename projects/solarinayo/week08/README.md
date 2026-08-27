# Week 8 — Email / support automation (sample)

**Student:** solarinayo

## What I built

Paste a customer email → first line `LABEL:` → draft reply. Human still sends. No auto-refunds.

## Who it helps

A small Lagos fintech / POS support desk.

## How to run it

```bash
streamlit run week08-automation/email_assistant.py
python week08-automation/gradio_app.py
```

Optional n8n: import `week08-automation/n8n-email-assistant.json` if installed.

## What was hard

The same angry email labelled COMPLAINT then SPAM on a rerun. Automation would hide real complaints.

## What I would improve

Ten-email test table. Never auto-send.

## Flowchart

```
Trigger (paste) → ask() classify + draft → human clicks Send
```

## Risks

Hallucinated refund · wrong LABEL · latency if thirty students hit Gemini at once (429).
