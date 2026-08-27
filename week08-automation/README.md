# MODULE 8 — AI Automation & Multi-Step Workflows

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Trigger → AI → human. Classify email. Never auto-send money. Optional n8n.

**Tools:** Gemini/Grok. Gradio, Streamlit, optional n8n.

**How to:**
```bash
python week08-automation/gradio_app.py
streamlit run week08-automation/email_assistant.py
```
n8n: [../guides/HOW_TO.md](../guides/HOW_TO.md) section 11.

**What goes on behind the scenes:** A trigger starts the recipe. AI is one node. Human clicks Send. Wrong LABEL at scale is how automation hurts people — Week 11 scores this.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. AI automation
2. Trigger / action
3. Multi-step workflows
4. External services
5. No-code / low-code
6. n8n
7. APIs + models + automation
8. Business automations
9. Risks (auto-send, hallucination in email)

## Tasks

- Repetitive tasks to automate
- Workflow for an SME
- Flowchart
- Manual vs AI
- Risks

## Labs

- n8n intro
- First workflow
- Connect a model
- Process incoming info
- Multi-step

## Project

Choose one: customer support · email · leads · content · meeting summary.



Submit: `projects/YOUR_NAME/week08/` · [PR guide](../guides/fork_push_pr.md)
