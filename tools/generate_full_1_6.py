"""Full novice day1–day3 notebooks for weeks 1–6."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import ROOT, boot, code, header, md, note, week_open, write_nb

HOW = """1. Bookmark [../guides/HOW_TO.md](../guides/HOW_TO.md)
2. VS Code open on the **course folder** · terminal shows `(.venv)`
3. Ollama: [https://ollama.com](https://ollama.com) then `ollama run llama3.2`
4. Gemini key: [Google AI Studio](https://aistudio.google.com/app/apikey) → copy `.env.example` to `.env` → `GEMINI_API_KEY=`
5. Grok key (optional): [console.x.ai](https://console.x.ai) → `GROK_API_KEY=`
6. This notebook: top right **Select Kernel** → Python in `.venv`"""


def save(folder, d1, d2, d3):
    write_nb(ROOT / folder / "day1.ipynb", d1)
    write_nb(ROOT / folder / "day2.ipynb", d2)
    write_nb(ROOT / folder / "day3.ipynb", d3)


# ----- WEEK 1 -----
save(
    "week01-intro-to-ai",
    [
        md(header("WEEK 1 · DAY 1", "What is AI Engineering?", "Theory first. You will talk before you ship.")),
        week_open(
            "Leave today able to explain AI, ML, generative AI, LLM, and the AI Engineer job — without maths. See a ChatGPT-like pipeline on a picture.",
            "VS Code, this notebook, a browser for visuals, (optional) Ollama already installed.",
            HOW,
            "An LLM does **inference**: it already trained. Your prompt is turned into **tokens**. The model predicts the next tokens. That feels like answering. Nobody in this room is training GPT from scratch.",
        ),
        boot(),
        md("""## The 12-year-old picture

A normal program is a recipe: `2 + 2` is always `4`.

**AI** = computers doing judgement-like jobs (suggest, recognise, draft).

**Machine learning** = learn patterns from examples instead of writing every rule.

**Generative AI** = *makes* new text (quizzes, captions).

**LLM** = a generative model trained on huge text. **Gemini**, **Grok**, **DeepSeek**, **Llama (Ollama)** are LLMs. **ChatGPT** is a *product* around an LLM. We copy the *pattern*, not OpenAI’s API.

**Parameters** = millions of knobs set during **training**. You only do **inference** (asking).

Open [../visuals/how-ai-works.html](../visuals/how-ai-works.html) and [../visuals/software-vs-ai.html](../visuals/software-vs-ai.html)."""),
        md("""## Three jobs

| Role | What they do | Exact every time? |
|---|---|---|
| Software engineer | Rules in code | Yes — school grades |
| Data scientist | Stories in numbers | Charts |
| **AI engineer** | Apps around models | Useful language — must **test** for hallucination |

**Hallucination** = sounds sure, is wrong. **Inconsistency** = same prompt, different answer. **Latency** = wait time (ms). Full dictionary: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)"""),
        md("""## What goes on behind ChatGPT-like products (theory)

1. You type a **prompt** (text).
2. Software splits it into **tokens** (pieces of words).
3. The **LLM** predicts the next tokens, one after another (**inference**).
4. A product wraps that in a chat window, safety filters, and a bill.

**Training** already happened in a huge data centre. **You** only send HTTP.

**Software vs AI engineering:** a grade calculator must be exact. A quiz generator can vary. That trade-off is why Week 11 exists (evaluation).

**Normal chat vs engineered prompt:** “write about Python” vs role + audience + length + “do not invent libraries.” Picture: [../visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html)."""),
        md("## A tiny program (no AI yet) — every line"),
        code(
            '''# print() is a function. A function is a named recipe.
# The quotes mark a string = text for humans.
print("I am learning AI Engineering at Jekacode.")
# Behind the scenes: Python sends those characters to the notebook output area.'''
        ),
        md(note("Exit ticket", "AI is the field. Generative AI creates. LLMs talk. Engineers build apps and test them.")),
    ],
    [
        md(header("WEEK 1 · DAY 2", "Lab: prompts and African problems", "Normal chat vs engineered instructions.")),
        week_open(
            "Write a weak prompt and a strong prompt. List 10 problems. Pick one Nigerian/African problem with the five questions.",
            "This notebook. Optional Gemini/Ollama if you want the model to answer live.",
            HOW,
            "A **prompt** is just text. The model does not ‘know you’. Clear role + task + limits change the **tokens** it predicts. That is the start of prompt engineering (Week 5).",
        ),
        boot(),
        md("Picture: [../visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html)"),
        code(
            '''# Two strings. We are not calling the AI yet — we are designing the instruction.
weak = "Write about Python."
# Triple-quoted or plus signs both make long text. Here we use parentheses to join strings.
better = (
    "You are a Python instructor for JSS2 in Lagos. "
    "Explain Python using a school result sheet. Under 120 words. "
    "Do not invent library names."
)
print("WEAK\\n", weak)
print("\\nENGINEERED\\n", better)'''
        ),
        md("If you already have a Gemini key or Ollama, run this. If not, skip — Day 3 covers Ollama."),
        code(
            '''from jekacode.ai import ask
# from X import Y  means: open the file/package X and take the tool named Y.
# ask() sends your text to a model. provider= chooses the kitchen.

print(ask(better, provider="gemini"))
# Try provider="ollama" if Gemini is not set up. See HOW_TO.md.'''
        ),
        code(
            '''problems = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. "]
# A list is a row of lockers. Fill the strings.
african = {
    "who": "",
    "how_often": "",
    "current_fix": "",
    "why_not_enough": "",
    "can_ai_help": "",
}
# A dict is a form with named fields.
print(problems)
print(african)'''
        ),
    ],
    [
        md(header("WEEK 1 · DAY 3", "Project: Use Case Explorer + first model", "Ship a one-pager. Talk to Ollama or Gemini.")),
        week_open(
            "Save an AI Use Case Explorer into projects/YOUR_NAME/week01/. Get one live model reply and notice latency.",
            "Ollama and/or Gemini. Git if you already forked (guides/fork_push_pr.md).",
            HOW + "\n7. Pull llama: `ollama run llama3.2` once so Day 3 is not a 3GB surprise in class.",
            "Ollama = HTTP to localhost:11434. Gemini = HTTPS to Google with your key. Same `ask()` door. Different kitchens. **Latency** is the wait; measure with `ask_timed`.",
        ),
        boot(),
        code(
            '''from jekacode.ai import ask_timed
# ask_timed is ask() plus a stopwatch (latency_ms).

result = ask_timed(
    "Explain Jekacode like I am 12. Four sentences.",
    provider="ollama",  # change to "gemini" if Ollama is not installed
    system="Simple English. Warm.",
)
# result is a dict: ok, text, latency_ms, error
print("ok:", result["ok"])
print("waited_ms:", result["latency_ms"])
print(result["text"] or result["error"])'''
        ),
        md("""Write in `projects/YOUR_NAME/week01/README.md`:

- Problem, users, what AI would do, what must stay ordinary code
- Which model you used and the latency number"""),
    ],
)

# ----- WEEK 2 -----
save(
    "week02-python",
    [
        md(header("WEEK 2 · DAY 1", "Python is a recipe", "Input → process → output. Later the process is an LLM.")),
        week_open(
            "Understand variables, types, lists, dicts. See why grades must NOT go through Gemini (hallucination / inconsistency).",
            "VS Code, this notebook, Python 3.11+.",
            HOW,
            "Python reads your file top to bottom. A **variable** is a labelled box. An **LLM** predicts tokens; `70 >= 50` is exact. Mixing them without thinking is how fake scores happen.",
        ),
        boot(),
        code(
            '''# A string (text). Quotes are required.
student = "Chidi"
# An int (whole number). No quotes.
score = 78
# >= means "greater or equal". The result is True or False (a boolean).
passed = score >= 50
print(student, score, passed)'''
        ),
        code(
            '''# A list: ordered lockers. Index 0 is the first locker (computers start at 0).
scores = [70, 85, 40]
# A dict: named fields, like a form.
row = {"name": "Amaka", "city": "Enugu"}
print("first score", scores[0])
print("name", row["name"])'''
        ),
        md("**def** starts a function = a named recipe you can reuse. **if** chooses a path. **for** repeats."),
        code(
            '''def grade(score):
    # Exact rules. Never ask Grok to invent this.
    if score >= 70:
        return "A"
    if score >= 50:
        return "C"
    return "F"

for s in [88, 49]:
    print(s, "→", grade(s))'''
        ),
    ],
    [
        md(header("WEEK 2 · DAY 2", "Lab: errors are maps", "Break it. Read the last line.")),
        week_open(
            "Read a traceback. Use an LLM to *explain* an error, not to compute the grade.",
            "This notebook. Optional Gemini.",
            HOW,
            "When Python crashes it prints a **traceback**: file, line, error type. The last line is the treasure. That is **debugging**. Behind the scenes Python walks the call stack (which function called which) and prints it. An LLM can *translate* that into English. It must not *replace* `grade()`.",
        ),
        boot(),
        md("""## Theory: the four errors you will actually see

| Error | Plain English | Typical fix |
|---|---|---|
| `NameError` | You used a name Python has never seen | Spell it, or create it first |
| `TypeError` | You mixed types (`"3" + 1`) | Convert with `int()` or `str()` |
| `IndexError` | You asked for locker 9 in a list of 3 | Check `len(list)` |
| `KeyError` | The dict has no field with that name | Print `row.keys()` |

**Files:** `open("notes.txt").read()` loads text. `Path("notes.txt").write_text("hello")` saves. Week 6 uses this for the handbook."""),
        code("# Uncomment the next line, run, read the NameError, then comment it again.\\n# print(undefined_name)"),
        code(
            '''# A dict of one student. Keys are the field names on the form.
row = {"name": "Tunde", "score": 64}

# .get(key, default) never crashes if the key is missing.
print("name:", row.get("name", "?"))
print("missing field:", row.get("city", "not on the form"))

# try/except = "if this blows up, do the other thing".
try:
    print("bad index:", [10, 20][9])
except IndexError as err:
    # err is the error object. str(err) is the message humans read.
    print("caught IndexError:", err)'''
        ),
        md("Paste the error into Gemini: `Explain like I am 12.` That is AI for **productivity**, not for inventing marks."),
        code(
            '''from jekacode.ai import ask
# Optional: skip if you have no key yet.
print(ask(
    "Explain this error like I am 12:\\nNameError: name 'undefined_name' is not defined",
    provider="gemini",
    system="Jekacode tutor. Short. No shame.",
))'''
        ),
    ],
    [
        md(header("WEEK 2 · DAY 3", "Project: Student Performance Analyzer", "Deterministic software. Copy to projects/week02.")),
        week_open(
            "Run student_analyzer.py. Add a fourth student. Pass/Resit. Class average.",
            "Terminal + the .py file (comments on every idea).",
            "From course root: `python week02-python/student_analyzer.py`",
            "This program never calls an API. Same input → same output. That is the opposite of LLM inconsistency.",
        ),
        boot(),
        code(
            '''# Import the file sitting next to this notebook (run kernel from week02-python).
import student_analyzer
student_analyzer.report([
    {"name": "Ada", "scores": [70, 80, 90]},
    {"name": "Bola", "scores": [40, 55, 50]},
])'''
        ),
    ],
)

# ----- WEEK 3 -----
save(
    "week03-llm-apis",
    [
        md(header("WEEK 3 · DAY 1", "APIs, tokens, latency, limits", "Gemini and Grok are kitchens. Your key is the ticket.")),
        week_open(
            "Explain API, key, token, context window, latency, hallucination, inconsistency. Call Gemini (and Grok if you have a key).",
            "`.env` with GEMINI_API_KEY. Optional GROK_API_KEY. Optional Ollama.",
            HOW,
            "Your Python uses **requests** to POST JSON to a URL (**endpoint**). The server runs **inference** and returns tokens. You pay for tokens and you wait (**latency**). Nothing magical happens on your laptop except Ollama.",
        ),
        boot(),
        md("""Pictures: [../visuals/api-architecture.html](../visuals/api-architecture.html) · [../visuals/latency.html](../visuals/latency.html)

| Import | Why |
|---|---|
| `requests` (inside jekacode.ai) | Speak HTTP, the language of APIs |
| `dotenv` | Load `.env` so keys are not in GitHub |
| `ask` | One function so you do not copy URLs every week |

GPT/Claude: **names to recognise**. We do not require those keys.

## Theory: tokens, context, cost, limits

- A **token** is a chip of text (often ~¾ of an English word). You pay for input + output tokens.
- **Context window** = how much the model can “see” at once. Paste a whole textbook → overflow or dropped start. That is why **RAG** (Week 6) sends *chunks*, not the library.
- **Rate limit** = too many requests; wait. Classroom 429 errors are normal if thirty people hit Gemini together.
- **Hallucination** vs **inconsistency**: wrong-but-confident vs same-prompt-different-wording. Test both with `ask_timed` on Day 2."""),
        code(
            '''from jekacode.ai import ask
# provider="gemini" reads GEMINI_API_KEY and calls Google.
print(ask(
    "Explain a token like I am 12. Four sentences.",
    provider="gemini",
    system="Jekacode tutor. No jargon piles.",
))'''
        ),
    ],
    [
        md(header("WEEK 3 · DAY 2", "Lab: test all kitchens", "Skip any provider you have no key for.")),
        week_open(
            "Fill a table: provider, latency_ms, ok, notes. See inconsistency and cost-awareness.",
            "Keys you actually created. Ollama if installed.",
            HOW + "\nAlso open [../setup/test_all_models.ipynb](../setup/test_all_models.ipynb)",
            "`ask_timed` starts a clock, calls `ask`, stops the clock. Networks wobble — three runs beat one tweet.",
        ),
        boot(),
        code(
            '''from jekacode.ai import ask_timed
q = "Summarise what an API is in one sentence for a POS agent in Lagos."
for p in ["gemini", "grok", "deepseek", "ollama"]:
    r = ask_timed(q, provider=p)
    print("====", p, "====")
    print("ok", r["ok"], "ms", r["latency_ms"])
    print((r["text"] or r["error"] or "")[:300], "\\n")'''
        ),
    ],
    [
        md(header("WEEK 3 · DAY 3", "Project: Writing Assistant", "Generate, summarise, rewrite, improve.")),
        week_open(
            "Four functions. Compare Gemini vs Grok on the same sample. Save to projects/week03.",
            "Gemini required. Grok optional.",
            HOW,
            "Each button is a different **user prompt** with the same **system prompt**. That is how products stay on-brand.",
        ),
        boot(),
        code(
            '''from jekacode.ai import ask
W = "Writing coach for African students. Simple English."
sample = "AI na computer wey fit help people write."
print("IMPROVE\\n", ask(f"Improve grammar only:\\n{sample}", system=W, provider="gemini"))
print("\\nGROK\\n", ask(f"Improve grammar only:\\n{sample}", system=W, provider="grok"))'''
        ),
    ],
)

# ----- WEEK 4 -----
save(
    "week04-ai-apps",
    [
        md(header("WEEK 4 · DAY 1", "Frontend vs backend", "A spinner is an engineering choice.")),
        week_open(
            "Explain frontend/backend. Run Gradio *or* Streamlit *or* HTML chat. Know why latency needs a 'Thinking…' state.",
            "Same keys as Week 3. Gradio is already in requirements.txt.",
            HOW + "\nGradio: `python week04-ai-apps/gradio_chat.py` then open the printed URL.",
            "Browser = frontend (HTML or Gradio’s generated HTML). Python = backend. `ask()` = more HTTP to Gemini/Grok/Ollama. Three hops: human → your server → model vendor.",
        ),
        boot(),
        md("""| UI | How to run | Feel |
|---|---|---|
| **Gradio** | `python week04-ai-apps/gradio_chat.py` | Fastest prototype |
| Streamlit | `streamlit run week04-ai-apps/hello.py` | Tabs |
| HTML | `python week04-ai-apps/html-chatbot/server.py` | WhatsApp-like |

Picture: [../visuals/ui-choices.html](../visuals/ui-choices.html)

**import gradio as gr** — `gr` is a nickname. The library draws boxes so you do not write CSS today."""),
        code(
            '''# You usually run Gradio as a .py file, not in this cell.
# This cell only reminds you of the import story.
print("Gradio file: week04-ai-apps/gradio_chat.py — every line is commented.")
print("HTML explain: week04-ai-apps/html-chatbot/EXPLAINED.md")'''
        ),
    ],
    [
        md(header("WEEK 4 · DAY 2", "Lab: run all three UIs", "Terminal, not only Shift+Enter.")),
        week_open(
            "Hello Streamlit, Study Assistant, Gradio chat, HTML chat. Try Gemini and Grok in the dropdown.",
            "Terminal with (.venv). Models from HOW_TO.",
            """```bash
streamlit run week04-ai-apps/hello.py
streamlit run week04-ai-apps/study_assistant.py
python week04-ai-apps/gradio_chat.py
python week04-ai-apps/html-chatbot/server.py
```
HTML: http://127.0.0.1:5000""",
            "Each click packages JSON, your backend calls `ask()`, tokens return, the UI paints text. If you double-click because it feels slow, you pay twice — that is why we mention **latency**.",
        ),
        md("Read `hello.py` and `gradio_chat.py` comments aloud with a partner. Then this recap cell:"),
        boot(),
        code(
            '''# You do not launch Gradio from a notebook cell (two servers fight).
# This cell only names the three UIs so you remember the how-to.
print("Gradio:   python week04-ai-apps/gradio_chat.py")
print("Streamlit: streamlit run week04-ai-apps/study_assistant.py")
print("HTML:     python week04-ai-apps/html-chatbot/server.py")
print("Keys:     ../guides/HOW_TO.md")'''
        ),
    ],
    [
        md(header("WEEK 4 · DAY 3", "Project: Study Assistant", "Ship one UI to projects/week04.")),
        week_open(
            "A working explain/summarise/quiz/plan app (Streamlit) **or** Gradio **or** HTML. Screenshot + how to run.",
            "Same as Day 2.",
            "Copy the folder you chose into projects/YOUR_NAME/week04/. Push / PR: [../guides/fork_push_pr.md](../guides/fork_push_pr.md)",
            "User story: *As an SS2 student I want an explanation I can screenshot.* AI sits only in `ask()`. The tabs are ordinary Python. Behind the scenes each button builds a **user prompt**; `TEACHER` is the **system prompt** that stays put.",
        ),
        boot(),
        md("""## Theory recap before you ship

- **Frontend** = what the human sees (Gradio boxes, Streamlit tabs, HTML bubbles).
- **Backend** = Python that calls `ask()`.
- **Latency** = why the HTML chat shows “Thinking…”. Without it, people click twice and you pay twice.
- **Inconsistency** = click Explain twice; wording may change. That is normal for LLMs.

Read `study_assistant.py` top-to-bottom. Every import has a comment."""),
        md("Stretch: Pidgin tab, or CSS tweak in the HTML chat using navy `#03045E` and green `#16D365`."),
    ],
)

# ----- WEEK 5 -----
save(
    "week05-prompt-engineering",
    [
        md(header("WEEK 5 · DAY 1", "Prompt engineering as a contract", "Chat is casual. Products need standing orders.")),
        week_open(
            "Use role, few-shot, constraints, chaining. Reduce hallucination ('do not invent prices').",
            "Gemini/Grok. Gradio optional: `python week05-prompt-engineering/gradio_app.py`",
            HOW,
            "The model always predicts tokens. A **system prompt** is extra text prepended as policy. **Chaining** = output of step 1 becomes input of step 2 so the second step cannot wander as far.",
        ),
        boot(),
        code(
            '''from jekacode.ai import ask
print("WEAK\\n", ask("Write about Python.", provider="gemini"))
print("\\nENGINEERED\\n", ask(
    "You are a Python instructor in Ibadan. Result-sheet example. Under 160 words. One practice task.",
    system="Plain English. No fake libraries.",
    provider="gemini",
))'''
        ),
    ],
    [
        md(header("WEEK 5 · DAY 2", "Lab: chain Gemini then Grok", "Two kitchens, one workflow.")),
        week_open(
            "List problems with Gemini. Write a caption with Grok. Notice inconsistency if you rerun.",
            "Both keys if possible; else twice Gemini.",
            HOW,
            "Two HTTP round-trips → more **latency**. That is normal for workflows.",
        ),
        boot(),
        code(
            '''from jekacode.ai import ask
biz = "A suya spot in Wuse that also sells soft drinks"
sys = "Nigerian SME helper. Do not invent prices."
ideas = ask(f"List 5 customer problems:\\n{biz}", system=sys, provider="gemini")
print("STEP 1\\n", ideas)
print("STEP 2\\n", ask(f"One Instagram caption from the strongest problem.\\n{ideas}", system=sys, provider="grok"))'''
        ),
    ],
    [
        md(header("WEEK 5 · DAY 3", "Project: Business Assistant", "Streamlit or Gradio.")),
        week_open(
            "Four outputs for one SME. Human still posts. projects/week05.",
            "streamlit or gradio_app.py",
            """```bash
streamlit run week05-prompt-engineering/business_assistant.py
python week05-prompt-engineering/gradio_app.py
```""",
            "Each `ask()` is a separate inference. Four buttons ≈ four latencies and four chances to hallucinate a phone number — the system prompt forbids that; you still test it.",
        ),
        boot(),
        md("""## Theory: the prompt contract (say this out loud)

| Piece | Job |
|---|---|
| **Role** | Who the model is (SME helper, not a US copywriter) |
| **Task** | What to produce (Instagram post, not “write something”) |
| **Constraints** | What it must not do (no fake prices) |
| **Few-shot** | Tiny examples of the *shape* you want |
| **Chain** | Step 1 output becomes step 2 input |

**Hallucination guard:** “Do not invent prices or phone numbers.” Test it: ask for the shop’s WhatsApp. A **pass** is “I do not have it.”"""),
        code(
            '''from jekacode.ai import ask
# Few-shot = show two tiny examples so the third follows the pattern.
sys = (
    "You label SME messages. Reply with ONE word: QUESTION, COMPLAINT, PRAISE, or SPAM.\\n"
    "Example: 'How much is a screen?' → QUESTION\\n"
    "Example: 'You people are thieves' → COMPLAINT"
)
print(ask("The suya was perfect, thank you.", system=sys, provider="gemini"))'''
        ),
    ],
)

# ----- WEEK 6 -----
save(
    "week06-rag",
    [
        md(header("WEEK 6 · DAY 1", "RAG: give the student the textbook", "Hallucination is the disease. Retrieval is the medicine.")),
        week_open(
            "Explain LLM vs RAG. Chunk a handbook. Answer only from retrieved text.",
            "knowledge/school-handbook.md, Gemini or Grok. Gradio: week06-rag/gradio_app.py",
            HOW,
            "Without RAG the model predicts a *likely* fee. With RAG we **retrieve** chunks (here: shared words) and put them in the prompt. **Embeddings / vector DBs** are 'search by meaning' — idea only this week, no formulas.",
        ),
        boot(),
        md("[../visuals/rag-flow.html](../visuals/rag-flow.html)"),
        code(
            '''from pathlib import Path
from jekacode.ai import ask

# Path points at a file. read_text() loads it as one string.
text = Path("../knowledge/school-handbook.md").read_text()
# split("##") uses markdown headings as cheap **chunks**.
chunks = [p.strip() for p in text.split("##") if p.strip()]
q = "How do I ask for a transcript?"
words = set(q.lower().split())  # set = unique words
best = sorted(chunks, key=lambda c: sum(w in c.lower() for w in words), reverse=True)[0]
print(ask(
    f"ONLY this text. If missing, say you cannot find it.\\n{best}\\nQ:{q}",
    system="School information desk.",
    provider="gemini",
))'''
        ),
    ],
    [
        md(header("WEEK 6 · DAY 2", "Lab: document assistant + hallucination probe", "Ask a fee that is NOT in the file.")),
        week_open(
            "Run Streamlit or Gradio. Record whether the model invents naira amounts.",
            "Same keys.",
            """```bash
streamlit run week06-rag/document_assistant.py
python week06-rag/gradio_app.py
```""",
            "A **pass** is 'I cannot find it'. A **fail** is a confident fake fee. That is your hallucination test.",
        ),
        boot(),
        md("""## Theory before you click Run

`document_assistant.py` comments explain chunking and ranking. Read them aloud.

**Retrieval** this week is overlapping words, not magic. If the question says “transcript” and a chunk says “transcript”, that chunk wins.

**Gradio path** (paste the handbook yourself): `python week06-rag/gradio_app.py`

Try both questions:

1. Something **in** the handbook (assembly, transcript).
2. Something **not** in the handbook (a 2099 sports levy)."""),
        code(
            '''from pathlib import Path
from jekacode.ai import ask

text = Path("../knowledge/school-handbook.md").read_text()
honest = ask(
    f"ONLY this text. If missing, say you cannot find it.\\n{text[:2000]}\\nQ: How do I request a transcript?",
    system="School desk.",
    provider="gemini",
)
probe = ask(
    f"ONLY this text. If missing, say you cannot find it.\\n{text[:2000]}\\nQ: What is the secret 2099 sports levy in naira?",
    system="School desk. Never invent naira.",
    provider="gemini",
)
print("IN HANDBOOK?\\n", honest, "\\n\\nPROBE (should refuse)\\n", probe)'''
        ),
    ],
    [
        md(header("WEEK 6 · DAY 3", "Project: your knowledge base", "projects/week06 + how you tested hallucination.")),
        week_open(
            "School / Jekacode / SME policy assistant.",
            "Your .md or PDF.",
            "Copy knowledge files you are allowed to share. No real student data.",
            "Privacy is part of RAG: do not paste BVNs into Gemini. Behind the scenes: chunk → rank by overlapping words (this week) → stuff the best chunks into the prompt → `ask()`. **Embeddings** would rank by *meaning*; we name the idea so Week 11 eval still makes sense.",
        ),
        boot(),
        md("""## Theory: why RAG beats “just ask Gemini”

Plain LLM: predicts a *likely* school fee. That is how **hallucination** is born.

RAG: **retrieve** then **generate**. The model is a student with an open textbook.

| Step | What Python does | What the model does |
|---|---|---|
| 1 Chunk | Split the markdown | Nothing yet |
| 2 Retrieve | Pick chunks that share words with the question | Nothing yet |
| 3 Augment | Glue those chunks into the prompt | Reads them |
| 4 Generate | `ask()` | Writes only from that text (if you instruct it) |

**Fail the lab on purpose:** ask a fee that is *not* in the handbook. The honest answer is “I cannot find it.”"""),
        code(
            '''from pathlib import Path
from jekacode.ai import ask

text = Path("../knowledge/school-handbook.md").read_text()
# Probe: a number that should NOT be in a typical handbook.
q = "How many naira is the secret sports levy in 2099?"
print(ask(
    f"ONLY this document. If missing, say you cannot find it.\\n{text[:2500]}\\nQ:{q}",
    system="School desk. Never invent naira amounts.",
    provider="gemini",
))'''
        ),
    ],
)

print("weeks 1-6 full days written")
