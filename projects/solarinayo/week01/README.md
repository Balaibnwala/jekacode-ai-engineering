# Week 1 — AI Use Case Explorer (sample)

**Student:** solarinayo

## What I built

A one-page use case: **WAEC topic explainer for SS2**. A student types a topic. An LLM writes a short explanation they can screenshot. Ordinary code would still store the topic list. AI only writes the explanation.

## Who it helps

SS2 students in Lagos public schools who have notes but no teacher time after 2pm.

## How to run it

This week is a design + first model reply (no app yet). From the course root:

```bash
# Optional: talk to Ollama (no key) or Gemini (needs .env)
# See week01-intro-to-ai/day3.ipynb
```

## What was hard

Knowing what must stay **ordinary Python** (the student name, the class) versus what the model is allowed to invent (the explanation).

## What I would improve

A Gradio box in Week 4. A handbook in Week 6 so it does not hallucinate WAEC facts.

## Five validation questions

| Question | My answer |
|---|---|
| Who? | SS2 science students, mostly Android phones, sometimes no data |
| How often? | Every week before a test |
| Current fix | Copy notes from the board / WhatsApp group |
| Why not enough | Notes are long; nobody explains in 12-year-old English |
| Can AI help? | Yes for *explaining*. No for *marking the exam* |

## First model I tried

- Provider: Ollama `llama3.2` (then Gemini Flash when I got a key)
- Prompt: “Explain photosynthesis like I am 12. Four sentences. Nigerian farm example if useful.”
- Latency: about 2–8 seconds on my laptop (Ollama cold start was slower)

## Where AI sits

Only in the explanation. Pass/fail of a real test must never go through an LLM.
