# Three classes every week

Each Jekacode week is **three live classes**, not five random days. Homework sits between them.

**Student how-to (install Ollama, get Gemini/Grok keys, Gradio):** [HOW_TO.md](HOW_TO.md)

Every week **README** starts with: what we achieve · tools · how to · what happens behind the scenes. Code is commented for novices.

**Length:** about 2 hours 15 minutes per class (adjust if your cohort is shorter).  
**Room kit:** VS Code, Ollama (Week 1+), Gemini + optional Grok keys from Week 3, projector for [visuals/](../visuals/).

Every week has exactly three notebooks: **`day1.ipynb`** (theory) · **`day2.ipynb`** (lab) · **`day3.ipynb`** (project).

```
Class 1 — SEE IT     pictures, stories, architecture, live demo
Class 2 — TYPE IT    lab notebook, every line explained, errors welcome
Class 3 — SHIP IT    user story + project + copy into projects/ + git
```

Students should leave Class 3 with a file in `projects/YOUR_NAME/weekXX/` and (from Week 1) know they will later **push** and optionally **open a PR** ([fork_push_pr.md](fork_push_pr.md)).

---

## Week 1 — Introduction to AI & AI Engineering

**User story:** *As a first-time student, I want to see AI answer me on my laptop and know how that is different from chatting on a website, so I understand the job I am training for.*

### Class 1 — See it (ideas + Ollama)

- Open [visuals/how-ai-works.html](../visuals/how-ai-works.html) on the projector
- Open [visuals/software-vs-ai.html](../visuals/software-vs-ai.html) — **trade-off table**
- Words: AI · machine learning · generative AI · LLM · parameters (knobs, not magic)
- Live: `ollama run llama3.2` — same question a student would type into ChatGPT
- Contrast: **normal way** (type into a website) vs **engineering way** (your app will call a model)
- Notebook: `week01-intro-to-ai/day1.ipynb`
- Exit ticket: “AI is the field. Generative AI creates. LLMs talk. Engineers build apps.”

### Class 2 — Type it (prompts + first Python)

- Weak vs strong prompt ([visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html))
- `day2.ipynb` — 10 problems, one African problem, five validation questions
- First `print` cells; read an error together
- Homework: install leftovers from [setup/](../setup/README.md)

### Class 3 — Ship it (use-case explorer + Git)

- Ollama or Gemini: `day3.ipynb`
- Fill `projects/YOUR_NAME/week01/` with the use-case one-pager
- Teacher demos **fork** (even if they only screenshot it)
- Challenge: “If Gemini had your school database, what would you build?” (save for Week 6)

**Project:** AI Use Case Explorer  

---

## Week 2 — Python for AI

**User story:** *As a beginner, I want a tiny programme that turns scores into a report, because later user input → AI → output is the same shape.*

### Class 1 — See it
- Recipe metaphor; boxes (variables); lockers (lists); forms (dicts)
- Architecture: Input → Process → Output vs User → Model → UI
- `day1.ipynb`

### Class 2 — Type it
- `day2.ipynb` line by line: `def`, `if`, `for`, `f-string`
- Break a cell on purpose; read the traceback

### Class 3 — Ship it
- Run `student_analyzer.py`
- Add a fourth student + Pass/Resit
- Copy to `projects/YOUR_NAME/week02/`
- `git add` / `commit` practice (push if fork exists)

**Project:** Student Performance Analyzer  

---

## Week 3 — LLMs, APIs, Hugging Face

**User story:** *As a builder, I want my Python file to send text to Gemini, DeepSeek, or Ollama, so I am not stuck inside a chat website.*

### Class 1 — See it
- Waiter metaphor (API)
- [visuals/api-architecture.html](../visuals/api-architecture.html)
- Hugging Face hub tour ([setup/06_huggingface.md](../setup/06_huggingface.md))
- Keys in `.env` — never WhatsApp a key

### Class 2 — Type it
- `day1.ipynb` — `ask()` with `provider="gemini"` then `"ollama"`
- Each line of `jekacode/ai.py` header comments
- Tokens / cost in one slide (keep prompts short)

### Class 3 — Ship it
- `day2.ipynb` writing assistant
- Optional: Hugging Face `provider="huggingface"`
- Push week 3 folder; mention PR title format

**Project:** AI Writing Assistant  

---

## Week 4 — Screens: Streamlit, Gradio, HTML chatbot

**User story:** *As a JSS student, I want a chat window that looks like a real product (not a notebook), so I believe I can ship.*

### Class 1 — See it
- Frontend vs backend in one picture
- Streamlit vs Gradio vs **real HTML/CSS/JS** — trade-offs
- [visuals/ui-choices.html](../visuals/ui-choices.html)

### Class 2 — Type it
- `streamlit run week04-ai-apps/hello.py`
- `python week04-ai-apps/gradio_chat.py`
- Walk `html-chatbot/` **every file, every line** (`EXPLAINED.md`)

### Class 3 — Ship it
- Study Assistant **or** HTML chatbot **or** Gradio
- Copy to projects; screenshot; `git push`; optional PR

**Projects:** Jekacode Study Assistant · Gradio chat · HTML/CSS chatbot  

---

## Week 5 — Prompt engineering vs “just asking”

**User story:** *As a shop owner, I want Instagram + email from one business description, and I want the AI to stop inventing prices.*

### Class 1 — See it
- [visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html) again, now with chaining
- Role, task, examples, constraints, format
- Normal chat: “write about my shop.” Engineered: role + audience + banned hallucinations

### Class 2 — Type it
- Weak vs strong in `day1.ipynb`
- Multi-step workflow (ideas → caption)

### Class 3 — Ship it
- `business_assistant.py` (Streamlit) or Gradio clone
- Add WhatsApp-angry-customer tab as stretch

**Project:** AI Business Assistant  

---

## Week 6 — RAG

**User story:** *As a parent, I want answers from the school handbook, not a confident guess.*

### Class 1 — See it
- Exam without textbook vs with textbook
- [visuals/rag-flow.html](../visuals/rag-flow.html)
- No cosine lecture

### Class 2 — Type it
- Chunk → keyword score → Gemini with “only this context”
- `day1.ipynb`

### Class 3 — Ship it
- `document_assistant.py` + `knowledge/` files
- Honest “I cannot find it” demo

**Project:** Chat With Your PDF / handbook  

---

## Week 7 — Agents

**User story:** *As a teacher, I want a research brief that used a notes tool, not a single chat bubble.*

### Class 1 — See it
- Chatbot vs agent vs workflow
- [visuals/agent-flow.html](../visuals/agent-flow.html)

### Class 2 — Type it
- Two Python tools; model chooses
- `day1.ipynb`

### Class 3 — Ship it
- `research_assistant.py`
- Stretch: one extra tool (word count, date)

**Project:** AI Research Assistant  

---

## Week 8 — Automation

**User story:** *As an SME, I want incoming messages classified and drafted, but a human still sends.*

### Class 1 — See it
- Trigger → AI → action
- n8n sketch vs Python
- Safety: no auto-send money

### Class 2 — Type it
- `email_assistant.py` + JSON import notes
- Risks of automation

### Class 3 — Ship it
- Pick one menu item; flowchart in README
- Push

**Project:** Email / support / content / leads / meeting notes  

---

## Week 9 — African problems + YarnGPT

**User story:** *As a community member, I want notices in Yoruba / Igbo / Hausa / Pidgin, including voice when the laptop allows.*

### Class 1 — See it
- Five problem questions (no “I want an AI app”)
- YarnGPT on Hugging Face: Nigerian-accented English + **YarnGPT-local** (Yoruba, Igbo, Hausa)
- Trade-off: Gemini text vs YarnGPT speech vs laptop GPU

### Class 2 — Type it
- Problem canvas
- `interesting-projects/yarngpt-voice-notice/` walkthrough
- Colab / Space for real audio; Gemini for text always

### Class 3 — Ship it
- Canvas + first MVP sketch
- Optional voice demo recording

**Project:** Problem → MVP · Voice notice stretch  

---

## Week 10 — Deploy + GitHub for real

**User story:** *As an auntie on WhatsApp, I want a link, not “it works on my laptop.”*

### Class 1 — See it
- Code → GitHub → Streamlit Cloud / HF Space / HTML host
- Secrets on the host, not in git
- Repeat [fork_push_pr.md](fork_push_pr.md) live

### Class 2 — Type it
- README, requirements, checklist
- Fix logo paths for cloud

### Class 3 — Ship it
- Live URL on a phone
- PR or tagged release of `projects/YOUR_NAME`

**Project:** Deployed app  

---

## Week 11 — Responsible AI

**User story:** *As a tester, I want to try to break the app so we know the limits before demo day.*

### Class 1 — See it
- Hallucination, bias, injection, privacy
- Live “break a student app”

### Class 2 — Type it
- Test battery in notebook
- Guardrail system prompt

### Class 3 — Ship it
- `evaluation_report.md` filled with evidence

**Project:** Evaluation report  

---

## Week 12 — Capstone

**User story:** *As a hiring manager / teacher, I want an 8-question story and a working demo.*

### Class 1 — See it
- Demo rubric; portfolio minimum
- Career honesty (glue models ≠ trained GPT from scratch)

### Class 2 — Type it
- README hints; presentation.md
- Rehearse 6 minutes

### Class 3 — Ship it
- Demo day · PRs welcome · sleep

**Project:** Capstone + presentation  

---

## Teacher rhythm (same every week)

1. Before Class 1: open the week’s **visual HTML** yourself  
2. Class 1: projector, no one left behind on vocabulary  
3. Class 2: you type first 5 minutes, they type the rest  
4. Class 3: user story on the board; git at the end even if messy  

Ollama is the safety net when APIs fail. Gemini is the quality net when laptops are weak. Hugging Face is the African model shelf (YarnGPT). Gradio is the fastest UI. HTML is the “this looks like a company” UI.
