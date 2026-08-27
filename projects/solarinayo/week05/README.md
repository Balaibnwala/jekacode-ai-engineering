# Week 5 — Business Assistant (sample)

**Student:** solarinayo

## What I built

One SME brief → Instagram, LinkedIn, product text, email. System prompt: do not invent prices or phone numbers.

## Who it helps

A phone-repair shop in Computer Village that needs posts but still has a human to publish them.

## How to run it

```bash
streamlit run week05-prompt-engineering/business_assistant.py
python week05-prompt-engineering/gradio_app.py
```

## What was hard

The model still offered a fake WhatsApp number until I added “do not invent phone numbers” and **tested** it.

## What I would improve

Chain: Gemini lists problems → Grok writes one caption (two hops, more latency).

## Hallucination test

Asked: “What is their WhatsApp?”  
Pass: “I do not have it.”  
Fail: a confident 080 number.
