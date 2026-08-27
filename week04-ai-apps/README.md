# MODULE 4 — Building AI Applications & User Interfaces

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Frontend vs backend. Run **Gradio**, Streamlit, and the HTML chat. Know why a spinner exists (**latency**). Ship a Study Assistant.

**Tools:** Same keys as Week 3. Gradio is already in `requirements.txt`.

**How to:**
```bash
python week04-ai-apps/gradio_chat.py
streamlit run week04-ai-apps/study_assistant.py
python week04-ai-apps/html-chatbot/server.py
```
Keys: [../guides/HOW_TO.md](../guides/HOW_TO.md) sections 6–8.

**What goes on behind the scenes:** Browser → your Python → `ask()` → Gemini/Grok/Ollama. Three hops. `import gradio as gr` draws boxes so you do not write CSS today.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`. Every `.py` is commented.

## Outline

1. AI application development
2. Frontend vs backend
3. Gradio / Streamlit / HTML
4. Collecting user input
5. Displaying AI responses
6. Connecting UI to Gemini or Grok
7. Basic design (Jekacode navy/green)
8. Share locally (intro to deploy)

## Tasks

- Design an interface
- Form that accepts input
- Connect a model
- Improve usability

## Labs

- First Gradio or Streamlit app
- Text in/out
- Connect API
- Chatbot UI (HTML)
- Share on localhost

## Project

**AI Study Assistant** — explain, summarise, quiz, study plan. Stretch: HTML chatbot or Gradio.

[../visuals/ui-choices.html](../visuals/ui-choices.html) · `html-chatbot/` · `gradio_chat.py` · `study_assistant.py`

Submit: `projects/YOUR_NAME/week04/` · [PR guide](../guides/fork_push_pr.md)
