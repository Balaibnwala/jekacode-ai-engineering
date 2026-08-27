# MODULE 11 — Responsible AI, Evaluation & AI Safety

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Hallucination, inconsistency, bias, prompt injection, privacy. Timed eval. Ship an Evaluation Report with **numbers**.

**Tools:** Gemini (and Grok). Gradio sandbox: `python week11-responsible-ai/gradio_app.py`.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) · [../guides/TEST_ALL_MODELS.md](../guides/TEST_ALL_MODELS.md).

**What goes on behind the scenes:** System prompts are still text. Guardrails = policy + tests, not a force field. `ask_timed` is `ask()` plus `time.perf_counter()`.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. Responsible AI
2. Bias
3. Hallucinations and misinformation
4. Privacy
5. Prompt injection
6. Evaluation
7. Testing apps
8. Monitoring
9. Cost and **latency**/performance
10. Safer systems

## Tasks

- Risks
- Hallucination tests
- Safety checklist
- Eval criteria
- Document limits

## Labs

- Different inputs
- Score quality
- Guardrails
- Structured outputs
- Tiny eval set

## Project

**AI Evaluation Report** — accuracy, reliability (inconsistency), safety, cost, UX, limits.

[../guides/TEST_ALL_MODELS.md](../guides/TEST_ALL_MODELS.md) · `evaluation_report.md`

Submit: `projects/YOUR_NAME/week11/` · [PR guide](../guides/fork_push_pr.md)
