from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import ROOT, code, header, md, note, week_readme, write_nb, write_text

week_readme(
    "week04-ai-apps",
    4,
    "Building AI Applications & Interfaces",
    "Until now the AI lived in a notebook. This week you give it a screen. Streamlit turns Python into a small website.",
    [
        "What a user interface is",
        "Text boxes, buttons, and tabs in Streamlit",
        "Connecting a screen to Gemini",
        "Why this feels like a real product",
    ],
    "Jekacode AI Study Assistant",
    [
        ("Day 1", "Streamlit hello world"),
        ("Day 2", "Inputs and outputs"),
        ("Day 3", "Connect Gemini"),
        ("Day 4", "Chat-style layout"),
        ("Day 5", "Study Assistant project"),
    ],
)

write_nb(
    ROOT / "week04-ai-apps/01_learn.ipynb",
    [
        md(header("WEEK 4", "Give your AI a screen", "Streamlit = Python that becomes a website.")),
        md(
            """## The jump

```
Python script
      ↓
User interface (what a person sees)
      ↓
User types a question
      ↓
Your app calls Gemini
      ↓
The screen shows the answer
```

You do **not** need HTML or CSS to start. Streamlit draws the page for you.

In a terminal, from this folder:

```bash
streamlit run hello.py
streamlit run study_assistant.py
```"""
        ),
        md(note("This is the magic week", 'Many students feel "oh, I can actually build AI products" when the browser opens.')),
        md("Open `hello.py` and `study_assistant.py` beside this notebook. The lab is running those files, not only cells."),
    ],
)

write_nb(
    ROOT / "week04-ai-apps/02_lab.ipynb",
    [
        md(header("WEEK 4 LAB", "Run the Study Assistant", "Terminal, not only Shift+Enter.")),
        md(
            """## Steps

1. Open VS Code Terminal.
2. Make sure `(.venv)` is active.
3. Run:

```bash
streamlit run week04-ai-apps/hello.py
```

4. Then:

```bash
streamlit run week04-ai-apps/study_assistant.py
```

5. Try all four tabs: Explain, Summarize, Quiz, Study plan.

## Challenge

Add a fifth tab: **Translate to simple Pidgin** (or your language). Copy `study_assistant.py` into `projects/YOUR_NAME/week04/` when it works."""
        ),
    ],
)

write_text(
    ROOT / "week04-ai-apps/hello.py",
    '''import streamlit as st

st.set_page_config(page_title="Jekacode Hello", page_icon="assets/jekacode-logo.png")
st.image("../assets/jekacode-logo.png", width=220)
st.title("Hello from Jekacode")
name = st.text_input("What is your name?")
if name:
    st.success(f"Welcome {name}. You just built a screen with Python.")
''',
)

write_text(
    ROOT / "week04-ai-apps/study_assistant.py",
    '''"""Jekacode AI Study Assistant — Week 4 project."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from jekacode.ai import ask

TEACHER = (
    "You are a patient Jekacode tutor for African secondary and university students. "
    "Use simple English. Give Nigerian examples when they help. "
    "Never pretend to know a fact you are unsure about."
)

st.set_page_config(page_title="Jekacode Study Assistant", layout="wide")
st.image("../assets/jekacode-logo.png", width=220)
st.title("Jekacode AI Study Assistant")
st.caption("Explain · Summarize · Quiz · Study plan  ·  Gemini")

provider = st.sidebar.selectbox("Model", ["gemini", "deepseek"])
explain, summarize, quiz, plan = st.tabs(["Explain", "Summarize", "Quiz", "Study plan"])

with explain:
    topic = st.text_input("What topic is confusing?", placeholder="Photosynthesis")
    level = st.selectbox("Student level", ["JSS", "SSS / WAEC", "University beginner"])
    if st.button("Explain it", key="ex") and topic:
        st.write(ask(f"Explain {topic} for a {level} student in 180 words.", provider=provider, system=TEACHER))

with summarize:
    notes = st.text_area("Paste notes or a page of text", height=200)
    if st.button("Summarize", key="sum") and notes:
        st.write(ask(f"Summarize these notes as 7 bullets and 1 exam tip:\\n{notes}", provider=provider, system=TEACHER))

with quiz:
    subject = st.text_input("Subject and topic", placeholder="SS2 Government — federalism")
    n = st.slider("How many questions?", 3, 8, 5)
    if st.button("Make a quiz", key="quiz") and subject:
        st.write(ask(f"Create {n} short-answer quiz questions on {subject} with answers at the end.", provider=provider, system=TEACHER))

with plan:
    goal = st.text_input("What are you preparing for?", placeholder="JAMB Biology in 14 days")
    minutes = st.number_input("Minutes per day", min_value=20, max_value=180, value=45)
    if st.button("Build my plan", key="plan") and goal:
        st.write(ask(f"Make a realistic study plan. Goal: {goal}. Daily time: {minutes} minutes. Use a table.", provider=provider, system=TEACHER))
''',
)

week_readme(
    "week05-prompt-engineering",
    5,
    "Prompt Engineering & AI Workflows",
    "Prompt engineering is not magic spells. It is writing a job description so clear that the model can succeed.",
    [
        "Role, task, examples, limits, output format",
        "System prompts you can reuse",
        "Prompt chaining (step 1 feeds step 2)",
        "Asking for structured output (labels, bullets, JSON-like blocks)",
    ],
    "AI Business Assistant",
    [
        ("Day 1", "Weak vs strong prompts"),
        ("Day 2", "Role + constraints"),
        ("Day 3", "Few-shot examples"),
        ("Day 4", "A 3-step workflow"),
        ("Day 5", "Business assistant app"),
    ],
)

write_nb(
    ROOT / "week05-prompt-engineering/01_learn.ipynb",
    [
        md(header("WEEK 5", "Teach the model how to behave", "Clear beats clever.")),
        md(
            """## Experiment, do not memorise

**Weak:** Write about Python.

**Better:** You are a Python instructor teaching absolute beginners. Explain Python using a simple Nigerian student example. Keep the explanation under 200 words.

Then add:

- **Role prompting** — who it is
- **Clear instructions** — the job
- **Examples** — "like this, not like that"
- **Constraints** — length, language, no slang if you do not want slang
- **Output format** — bullets, table, or labelled sections"""
        ),
        code(
            """from jekacode.ai import ask

weak = ask("Write about Python.")
strong = ask(
    "You are a Python instructor teaching absolute beginners in Ibadan. "
    "Explain Python using a school result-sheet example. "
    "Under 200 words. End with one practice task.",
    system="Plain English. No buzzwords.",
)
print("WEAK\\n", weak)
print("\\nSTRONG\\n", strong)"""
        ),
        md("## A tiny workflow (chaining)"),
        code(
            """from jekacode.ai import ask

business = "A suya spot in Wuse, Abuja that also sells soft drinks"

ideas = ask(f"List 5 customer problems this business has: {business}", system="You help Nigerian SMEs.")
post = ask(f"Turn the strongest problem into one Instagram caption.\\nProblems:\\n{ideas}", system="Short, warm, no fake slang.")
print(ideas)
print("\\n---\\n")
print(post)"""
        ),
        md(note("Reliability", "If the answer is messy, ask for labelled sections. If it invents prices, tell it not to invent numbers.")),
    ],
)

write_nb(
    ROOT / "week05-prompt-engineering/02_lab.ipynb",
    [
        md(header("WEEK 5 LAB", "Run the Business Assistant", "One input, four useful outputs.")),
        md(
            """```bash
streamlit run week05-prompt-engineering/business_assistant.py
```

Challenge: add a fifth output — a polite WhatsApp reply to an angry customer."""
        ),
    ],
)

write_text(
    ROOT / "week05-prompt-engineering/business_assistant.py",
    '''"""AI Business Assistant — Week 5 project."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from jekacode.ai import ask

SYSTEM = (
    "You are a practical marketing assistant for Nigerian and African small businesses. "
    "Simple English. No fake American slang. Do not invent prices or phone numbers."
)

st.set_page_config(page_title="Jekacode Business Assistant", layout="wide")
st.image("../assets/jekacode-logo.png", width=220)
st.title("AI Business Assistant")

kind = st.text_input("What business is this?", placeholder="Phone repair shop in Computer Village")
offer = st.text_area("What do they sell or do?", placeholder="Screen replacement, battery, software")
provider = st.selectbox("Model", ["gemini", "deepseek"])

if st.button("Generate pack") and kind:
    brief = f"Business: {kind}\\nOffer: {offer}"
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Instagram")
        st.write(ask(f"Write 1 Instagram post with 5 hashtags.\\n{brief}", provider=provider, system=SYSTEM))
        st.subheader("LinkedIn")
        st.write(ask(f"Write a short LinkedIn post for this SME.\\n{brief}", provider=provider, system=SYSTEM))
    with cols[1]:
        st.subheader("Product description")
        st.write(ask(f"Write a 80-word product/service description.\\n{brief}", provider=provider, system=SYSTEM))
        st.subheader("Email")
        st.write(ask(f"Write a polite marketing email under 120 words.\\n{brief}", provider=provider, system=SYSTEM))
''',
)

week_readme(
    "week06-rag",
    6,
    "RAG & Knowledge-Based AI",
    "Gemini is a smart student taking an exam without your school textbook. RAG gives the student the textbook.",
    [
        "Why models invent facts (hallucinations)",
        "Documents → chunks → search → answer",
        "Chat with a handbook PDF or markdown file",
        "When RAG is the right tool",
    ],
    "AI Document Assistant / Chat With Your PDF",
    [
        ("Day 1", "Hallucinations + analogy"),
        ("Day 2", "Split a document into chunks"),
        ("Day 3", "Find useful chunks"),
        ("Day 4", "Ask Gemini with those chunks"),
        ("Day 5", "Handbook assistant"),
    ],
)

write_nb(
    ROOT / "week06-rag/01_learn.ipynb",
    [
        md(header("WEEK 6", "Give the student the textbook", "No cosine formulas. Concept first.")),
        md(
            """## The analogy

ChatGPT-like models are smart students who read the public internet. They did **not** automatically read *your* school handbook.

If you ask "What is Greenfield's transcript fee process?" the model may **guess**. That guess is called a **hallucination**.

**RAG** means Retrieval-Augmented Generation:

```
User question
      ↓
Search your documents for useful pieces
      ↓
Send those pieces + the question to Gemini
      ↓
Generate an answer that can point at the text
```

We start with a simple search: shared words. (Later you will hear "embeddings" — that means search by *meaning*, not only matching words. You do not need the maths this week.)"""
        ),
        code(
            """from pathlib import Path

text = Path("../knowledge/school-handbook.md").read_text()
chunks = [p.strip() for p in text.split("##") if p.strip()]
print(f"{len(chunks)} chunks\\n")
print(chunks[0][:400])"""
        ),
        code(
            """question = "How do I ask for a transcript?"
words = set(question.lower().split())

def score(chunk):
    return sum(1 for w in words if w in chunk.lower())

ranked = sorted(chunks, key=score, reverse=True)
print("Best chunk:\\n")
print(ranked[0][:500])"""
        ),
        md("Now send the best chunk + the question to Gemini:"),
        code(
            """from jekacode.ai import ask

context = ranked[0]
answer = ask(
    f"Answer using ONLY this handbook text. If it is not there, say you cannot find it.\\n\\n"
    f"HANDBOOK:\\n{context}\\n\\nQUESTION: {question}",
    system="You are the school information desk.",
)
print(answer)"""
        ),
    ],
)

write_nb(
    ROOT / "week06-rag/02_lab.ipynb",
    [
        md(header("WEEK 6 LAB", "Chat with a document", "Use the Jekacode handbook or the school handbook.")),
        md(
            """```bash
streamlit run week06-rag/document_assistant.py
```

Upload is optional — the app already loads files in `knowledge/`.

Challenge: add a second document (your hostel rules, church programme, or shop policy) into `knowledge/` and ask questions that should *fail* if the text is missing. The honest "I cannot find it" is a feature."""
        ),
    ],
)

write_text(
    ROOT / "week06-rag/document_assistant.py",
    '''"""Chat with your documents — Week 6 RAG project (beginner retrieval)."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from pypdf import PdfReader
from jekacode.ai import ask

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"


def read_pdf(file) -> str:
    reader = PdfReader(file)
    return "\\n".join(page.extract_text() or "" for page in reader.pages)


def chunk_text(text: str, size: int = 500) -> list[str]:
    words = text.split()
    return [" ".join(words[i : i + size]) for i in range(0, len(words), size)]


def best_chunks(chunks: list[str], question: str, k: int = 3) -> str:
    q = set(question.lower().split())
    ranked = sorted(chunks, key=lambda c: sum(1 for w in q if w in c.lower()), reverse=True)
    return "\\n\\n---\\n\\n".join(ranked[:k])


st.set_page_config(page_title="Jekacode Document Assistant", layout="wide")
st.image("../assets/jekacode-logo.png", width=220)
st.title("Chat With Your Documents")
st.caption("Gemini is the student. Your file is the textbook.")

source = st.selectbox("Built-in document", ["school-handbook.md", "jekacode-handbook.md"])
upload = st.file_uploader("Or upload a PDF / TXT", type=["pdf", "txt", "md"])

if upload is not None:
    text = read_pdf(upload) if upload.name.endswith(".pdf") else upload.read().decode("utf-8", errors="ignore")
else:
    text = (KNOWLEDGE / source).read_text(encoding="utf-8")

chunks = chunk_text(text)
st.sidebar.write(f"Chunks: {len(chunks)}")
question = st.text_input("Ask a question", placeholder="How do I request a transcript?")
provider = st.sidebar.selectbox("Model", ["gemini", "deepseek"])

if st.button("Ask") and question:
    context = best_chunks(chunks, question)
    answer = ask(
        f"Use ONLY the context. If missing, say you cannot find it in the document.\\n\\nCONTEXT:\\n{context}\\n\\nQUESTION: {question}",
        provider=provider,
        system="You are a careful document assistant for Jekacode students.",
    )
    st.subheader("Answer")
    st.write(answer)
    with st.expander("Text I used"):
        st.write(context)
''',
)

week_readme(
    "week07-agents",
    7,
    "AI Agents & Tool Calling",
    "A chatbot answers. An agent has a goal and may use tools (calculator, notes, fake search) before it replies.",
    [
        "Agent vs chatbot vs workflow",
        "Tools as functions your code already knows how to run",
        "A simple think → tool → answer loop",
        "Keep to one agent and one or two tools",
    ],
    "AI Research Assistant",
    [
        ("Day 1", "What is an agent?"),
        ("Day 2", "Write two tools"),
        ("Day 3", "Let the model pick a tool"),
        ("Day 4", "Multi-step report"),
        ("Day 5", "Research assistant"),
    ],
)

write_nb(
    ROOT / "week07-agents/01_learn.ipynb",
    [
        md(header("WEEK 7", "One agent, a couple of tools", "Do not jump to multi-agent frameworks.")),
        md(
            """## Chatbot

```
Ask question → get answer
```

## Agent

```
Goal
  ↓
Think about what to do
  ↓
Use a tool (search, calculator, notes)
  ↓
Look at the result
  ↓
Maybe use another tool
  ↓
Return a finished result
```

A **tool** is just a Python function with a clear name. The model does not magically browse the whole internet in this classroom version. We give it small tools we control."""
        ),
        code(
            '''from jekacode.ai import ask

NOTES = {
    "jamb": "JAMB is the exam many Nigerian students take to enter university. English is compulsory.",
    "waec": "WAEC SSCE is a secondary school leaving exam used across West Africa.",
}


def notes_search(topic: str) -> str:
    topic = topic.lower()
    for key, value in NOTES.items():
        if key in topic:
            return value
    return "No local note found."


def word_count(text: str) -> str:
    return f"{len(text.split())} words"


goal = "Write a 6-line briefing on JAMB for a parent."
choice = ask(
    f"Goal: {goal}\\nTools: notes_search, word_count.\\nReply with ONLY the tool name and the input, like notes_search:jamb",
    system="You pick tools. Be short.",
)
print("Model chose:", choice)

if "notes_search" in choice:
    info = notes_search(choice.split(":")[-1])
else:
    info = "No tool used."

report = ask(f"Goal: {goal}\\nTool result: {info}\\nWrite the briefing.", system="Clear. No fluff.")
print(report)
print(word_count(report))'''
        ),
        md(note("Stay simple", "One agent. One or two tools. No AutoGen, no CrewAI this week.")),
    ],
)

write_nb(
    ROOT / "week07-agents/02_lab.ipynb",
    [
        md(header("WEEK 7 LAB", "Research Assistant", "Topic in. Structured report out.")),
        md(
            """```bash
streamlit run week07-agents/research_assistant.py
```

The agent may look up a tiny local knowledge file, then write a report. Replace the knowledge with facts about *your* community problem."""
        ),
    ],
)

write_text(
    ROOT / "week07-agents/research_assistant.py",
    '''"""AI Research Assistant — Week 7. One agent, two tools."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from jekacode.ai import ask

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = (ROOT / "knowledge" / "jekacode-handbook.md").read_text(encoding="utf-8")


def search_handbook(query: str) -> str:
    q = set(query.lower().split())
    parts = [p.strip() for p in HANDBOOK.split("##") if p.strip()]
    parts = sorted(parts, key=lambda p: sum(1 for w in q if w in p.lower()), reverse=True)
    return parts[0][:800] if parts else "Nothing found."


def outline(topic: str) -> str:
    return ask(
        f"Break this research topic into 4 tasks:\\n{topic}",
        system="Numbered list only.",
    )


st.set_page_config(page_title="Jekacode Research Assistant")
st.image("../assets/jekacode-logo.png", width=220)
st.title("AI Research Assistant")
st.caption("Goal → pick tools → organise → report")

topic = st.text_input("Research request", placeholder="Explain the Jekacode AI Engineering programme to a parent")
provider = st.selectbox("Model", ["gemini", "deepseek"])

if st.button("Run agent") and topic:
    with st.spinner("Thinking..."):
        tasks = outline(topic)
        notes = search_handbook(topic)
        report = ask(
            f"Write a structured report with headings: Problem, Facts we have, What we still don't know, Next step.\\n"
            f"Topic: {topic}\\nTasks:\\n{tasks}\\nNotes:\\n{notes}",
            provider=provider,
            system="Honest. If notes are weak, say so. You are a Jekacode research intern.",
        )
    st.subheader("Tasks")
    st.write(tasks)
    st.subheader("Tool: handbook search")
    st.write(notes)
    st.subheader("Report")
    st.write(report)
''',
)

week_readme(
    "week08-automation",
    8,
    "AI Automation & Multi-Step Workflows",
    "Automation is a recipe that starts itself. Trigger → get data → AI → decision → action. n8n is the Lego board. Python is the backup so nobody is stuck.",
    [
        "Triggers and actions",
        "Why businesses automate boring copy-paste work",
        "Sketch an n8n workflow",
        "Build a Python email-classifier as the classroom version",
    ],
    "AI Email Assistant (or another workflow from the menu)",
    [
        ("Day 1", "Automation picture"),
        ("Day 2", "n8n tour"),
        ("Day 3", "AI node idea"),
        ("Day 4", "Python classifier"),
        ("Day 5", "Choose a project"),
    ],
)

write_nb(
    ROOT / "week08-automation/01_learn.ipynb",
    [
        md(header("WEEK 8", "Trigger → AI → action", "n8n for the picture. Python so everyone can finish.")),
        md(
            """## The spine of every automation

```
Trigger (new email, new form, new row)
      ↓
Get data
      ↓
AI processing (classify, summarize, draft)
      ↓
Decision (urgent? spam? sales?)
      ↓
Action (draft reply, notify a human, save a note)
```

**n8n** is a visual tool for this. Teachers: follow the n8n beginner video in `teachers/VIDEO_GUIDE.md`.

Students: if n8n is hard to install, complete the Python app `email_assistant.py`. Same brain, different body.

## Example: AI Email Assistant

```
New email
  ↓
AI reads it
  ↓
Classifies: question / complaint / praise / spam
  ↓
Generates a draft
  ↓
A human reviews before send  ← important
```

Never auto-send money, legal advice, or exam answers without a person in the loop this term."""
        ),
        code(
            """from jekacode.ai import ask

email = '''Subject: My POS machine is down again
I have been waiting since yesterday. Customers are leaving. Fix this now.'''

print(ask(
    f"Classify this email as QUESTION, COMPLAINT, PRAISE, or SPAM. Then draft a calm reply.\\n\\n{email}",
    system="You work support for a Lagos fintech SME. Be respectful. Do not promise refunds you cannot keep.",
))"""
        ),
    ],
)

write_nb(
    ROOT / "week08-automation/02_lab.ipynb",
    [
        md(header("WEEK 8 LAB", "Email assistant + n8n sketch", "Draw it, then run it.")),
        md(
            """1. On paper, draw trigger → AI → action for **one** of: customer support, content, leads, meeting notes.
2. Open `n8n-email-assistant.json` (import into n8n if you have it).
3. Run the Python version:

```bash
streamlit run week08-automation/email_assistant.py
```

Project menu (pick one): AI customer support · AI email assistant · AI lead qualification · AI content workflow · AI meeting summarizer."""
        ),
    ],
)

write_text(
    ROOT / "week08-automation/email_assistant.py",
    '''"""AI Email Assistant — Week 8 Python path."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from jekacode.ai import ask

SYSTEM = (
    "You are a support assistant for African SMEs. "
    "First line: LABEL: QUESTION|COMPLAINT|PRAISE|SPAM. "
    "Then a draft reply a human can edit. Never send; humans send."
)

st.set_page_config(page_title="Jekacode Email Assistant")
st.image("../assets/jekacode-logo.png", width=220)
st.title("AI Email Assistant")
st.caption("New message → classify → draft → human review")

incoming = st.text_area("Paste an email", height=220)
provider = st.selectbox("Model", ["gemini", "deepseek"])
if st.button("Process") and incoming:
    st.write(ask(incoming, provider=provider, system=SYSTEM))
''',
)

write_text(
    ROOT / "week08-automation/n8n-email-assistant.json",
    """{
  "name": "Jekacode AI Email Assistant",
  "nodes": [
    {
      "parameters": { "path": "jekacode-email", "httpMethod": "POST" },
      "id": "1",
      "name": "New Email Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0]
    },
    {
      "parameters": {
        "jsCode": "return [{ json: { body: $json.body || $json } }];"
      },
      "id": "2",
      "name": "Get Data",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [240, 0]
    }
  ],
  "connections": {
    "New Email Webhook": { "main": [[{ "node": "Get Data", "type": "main", "index": 0 }]] }
  },
  "settings": { "executionOrder": "v1" },
  "notes": "Classroom sketch: webhook trigger then your Gemini/DeepSeek HTTP node. Keep a human review step before any send mail node."
}
""",
)

print("weeks 4-8 done")
