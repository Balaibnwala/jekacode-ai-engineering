"""Create day1 / day2 / day3 notebooks + official curriculum READMEs."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import ROOT, boot, code, header, md, note, write_nb, write_text

GLOSS = "../guides/AI_ENGINEERING_TERMS.md"
TEST = "../guides/TEST_ALL_MODELS.md"


def days(folder, w, d1, d2, d3):
    write_nb(ROOT / folder / "day1.ipynb", d1)
    write_nb(ROOT / folder / "day2.ipynb", d2)
    write_nb(ROOT / folder / "day3.ipynb", d3)


def curriculum(folder, n, title, outline, tasks, labs, project, extra=""):
    ol = "\n".join(f"{i}. {x}" for i, x in enumerate(outline, 1))
    tk = "\n".join(f"- {x}" for x in tasks)
    lb = "\n".join(f"- {x}" for x in labs)
    write_text(
        ROOT / folder / "README.md",
        f"""# MODULE {n} — {title}

Official Jekacode format: **Outline · Tasks · Labs · Project**.  
**Three class files:** `day1.ipynb` (theory) · `day2.ipynb` (lab) · `day3.ipynb` (project).

Dictionary: [{GLOSS}]({GLOSS}) · Test models: [{TEST}]({TEST})

## Outline

{ol}

## Tasks

{tk}

## Labs

{lb}

## Project

{project}

## Class files

| File | Class | What it is |
|---|---|---|
| `day1.ipynb` | 1 See it | Theory + terms |
| `day2.ipynb` | 2 Type it | Guided lab |
| `day3.ipynb` | 3 Ship it | Mini/capstone work for this week |

{extra}

Copy finished work into `projects/YOUR_NAME/week{n:02d}/` and [open a PR](../guides/fork_push_pr.md) if asked.
""",
    )


# --- setup test notebook ---
write_nb(
    ROOT / "setup/test_all_models.ipynb",
    [
        md(header("TEST", "Test Gemini, Grok, DeepSeek, Ollama", "Latency, inconsistency, hallucination.", 1)),
        boot(),
        md(f"Read [{TEST}]({TEST}) and [{GLOSS}]({GLOSS}) first. Skip any provider whose key you do not have."),
        code(
            """from jekacode.ai import ask, ask_timed

PROMPT = "Reply with exactly: Jekacode is ready."
for name in ["gemini", "grok", "deepseek", "ollama"]:
    print("====", name, "====")
    result = ask_timed(PROMPT, provider=name)
    print("ok:", result["ok"], "latency_ms:", result["latency_ms"])
    print((result["text"] or result["error"] or "")[:400])
    print()"""
        ),
        md("### Inconsistency — same prompt three times (Gemini)"),
        code(
            """prompt = "Name one West African food in one word only."
for i in range(3):
    print(i + 1, ask(prompt, provider="gemini"))"""
        ),
        md("### Hallucination probe — a fee that is not in our handbook"),
        code(
            """print(ask(
    "What is the official transcript fee in naira at Greenfield Secondary School? Answer with a number only.",
    provider="gemini",
))
print("--- If it invented a number, that is a hallucination. The sample handbook does not list a fee. ---")"""
        ),
    ],
)

# ========== WEEK 1 ==========
curriculum(
    "week01-intro-to-ai",
    1,
    "Introduction to Artificial Intelligence & AI Engineering",
    [
        "Introduction to Artificial Intelligence",
        "Machine Learning, Generative AI and LLMs",
        "How modern AI systems (ChatGPT-like) work",
        "AI Engineer vs Data Scientist vs Software Engineer",
        "Real-world applications",
        "Prompts and AI interaction",
        "Development environment (VS Code, Git, Ollama, Gemini)",
    ],
    [
        "Identify 10 real-world problems AI can help solve",
        "Research and present 3 AI-powered products",
        "Compare AI Engineer, Data Scientist, Software Engineer",
        "Write effective prompts",
        "Identify one Nigerian or African problem AI could help with",
    ],
    [
        "Set up Python and Git",
        "Install VS Code",
        "GitHub account",
        "First Python program",
        "Interact with a model (Ollama and/or Gemini)",
    ],
    "**AI Use Case Explorer** — pick a real problem and design a simple AI-powered solution.",
    extra="Pictures: [../visuals/how-ai-works.html](../visuals/how-ai-works.html) · [software-vs-ai.html](../visuals/software-vs-ai.html) · [chat-vs-engineer.html](../visuals/chat-vs-engineer.html)",
)
days(
    "week01-intro-to-ai",
    1,
    [
        md(header("WEEK 1 · DAY 1", "Theory: What AI is", "Terms first. Maths later — not this course.")),
        boot(),
        md(f"""## Programme idea

This is a **practical AI Engineering** cohort: little or no coding → real apps. We learn by building. Theory still matters so you can *talk like an engineer*.

Full dictionary: [{GLOSS}]({GLOSS})

## Outline for today

1. **AI** — computers doing judgement-like jobs (recommend, recognise, draft).
2. **Machine learning** — learn from examples, not only handwritten rules.
3. **Generative AI** — *makes* text (and more).
4. **LLM** — a generative model trained on huge text. It predicts useful next tokens. Gemini, Grok, DeepSeek, Llama are LLMs. **ChatGPT** is a *product* wrapped around an LLM. We study the *pattern*, not that company's API.
5. **Parameters** — knobs set in **training**. You do **inference** (asking) with `ask()`.

Open [../visuals/how-ai-works.html](../visuals/how-ai-works.html)."""),
        md("""## Three jobs (do not mix them)

| Role | Job | Exact answers? |
|---|---|---|
| Software Engineer | Rules in code | Yes — grade calculators |
| Data Scientist | Stories in numbers | Charts, not chat apps |
| **AI Engineer** | Products around models | Useful language; must be *tested* |

**Trade-off:** If the answer must never change (fees, marks), use Python. If the job is language, use an LLM *plus* tests.

Open [../visuals/software-vs-ai.html](../visuals/software-vs-ai.html)."""),
        md("""## How ChatGPT-like systems work (theory)

```
User text → app adds system prompt → API request → model (inference) → tokens back → UI
```

**Hallucination** (preview): the model can sound sure and be wrong. **Inconsistency**: same prompt, different wording next time. We test both from Week 3 / Week 11.

**Latency**: waiting time. Local Ollama can be slow; Gemini Flash is often quick. Picture: [../visuals/latency.html](../visuals/latency.html)"""),
        code('print("I am learning AI Engineering at Jekacode.")'),
        md(note("Exit ticket", "AI is the field. Generative AI creates. LLMs talk. AI Engineers build and *test* apps.")),
    ],
    [
        md(header("WEEK 1 · DAY 2", "Lab: prompts + problems", "Normal chat vs engineered instructions.")),
        boot(),
        md("""Open [../visuals/chat-vs-engineer.html](../visuals/chat-vs-engineer.html).

**Weak:** Write about Python.  
**Engineered:** role + place + example + length + “do not invent library names.”

That is the start of **prompt engineering** (deep in Week 5)."""),
        code(
            """weak = "Write about Python."
better = (
    "You are a Python instructor for JSS2 in Lagos. "
    "Explain Python using a result sheet. Under 120 words. "
    "Do not invent library names."
)
print("WEAK\\n", weak)
print("\\nENGINEERED\\n", better)"""
        ),
        md("Optional (needs a key or Ollama):"),
        code(
            """from jekacode.ai import ask
print(ask(better, provider="gemini"))  # try "ollama" if no Gemini yet"""
        ),
        md("### Tasks (type here)"),
        code(
            """problems = [f"{i}." for i in range(1, 11)]
products = ["", "", ""]
roles = {"AI Engineer": "", "Data Scientist": "", "Software Engineer": ""}
african = {"who": "", "how_often": "", "current_fix": "", "why_not_enough": "", "can_ai_help": ""}
print(problems, products, roles, african, sep="\\n---\\n")"""
        ),
    ],
    [
        md(header("WEEK 1 · DAY 3", "Project: Use Case Explorer + Ollama", "Ship a one-pager. Talk to a local model.")),
        boot(),
        md("""**Mini project:** AI Use Case Explorer. Save into `projects/YOUR_NAME/week01/`.

Install: [../setup/05_ollama.md](../setup/05_ollama.md) — `ollama run llama3.2` (not a 70B model)."""),
        code(
            """from jekacode.ai import ask, ask_timed

result = ask_timed(
    "Explain Jekacode like I am 12. Four sentences.",
    provider="ollama",
    system="Simple English.",
)
print("latency_ms:", result["latency_ms"])
print(result["text"] or result["error"])"""
        ),
        md("If Ollama failed, try `provider=\"gemini\"`. Write your use-case: problem, users, where AI sits, what stays as ordinary code."),
    ],
)

# ========== WEEK 2 ==========
curriculum(
    "week02-python",
    2,
    "Python Programming for AI",
    [
        "Python fundamentals",
        "Variables and data types",
        "Lists, dictionaries and sets",
        "Conditionals",
        "Loops",
        "Functions",
        "Files",
        "Debugging",
        "Using AI to understand errors",
    ],
    [
        "Program that collects student information",
        "Simple calculator",
        "Analyse student scores",
        "Beginner challenges",
        "Use an AI assistant to debug",
    ],
    [
        "Environment",
        "Variables",
        "Functions",
        "Lists and dictionaries",
        "Read/write files",
    ],
    "**Student Performance Analyzer** — scores → average → grade → report. This is *deterministic* software. Do not use an LLM for the grade.",
)
days(
    "week02-python",
    2,
    [
        md(header("WEEK 2 · DAY 1", "Theory: programs as recipes", "Input → process → output. Same shape as AI apps later.")),
        boot(),
        md(f"""AI apps are still Python. The model is one *step* in the recipe.

| Programming | Later AI |
|---|---|
| input() | user types in HTML / Streamlit |
| `if score >= 50` | exact rules — **no hallucination** |
| `print(report)` | UI shows Gemini/Grok text |

**Inconsistency** is a property of LLMs, not of `2+2`. That is why Week 2 exists.

Terms today: **variable**, **type**, **list**, **dict**, **function**, **bug**, **traceback**. Dictionary: {GLOSS}"""),
        code(
            """student = "Chidi"   # string
score = 78          # int
passed = score >= 50
print(student, score, passed)"""
        ),
        code(
            """scores = [70, 85, 40]
student = {"name": "Amaka", "city": "Enugu"}
print(scores[0], student["name"])"""
        ),
    ],
    [
        md(header("WEEK 2 · DAY 2", "Lab: if, loops, functions, errors", "Break it, read the last line of the error.")),
        boot(),
        code(
            """def grade(score):
    if score >= 70:
        return "A"
    if score >= 50:
        return "C"
    return "F"

for s in [88, 49]:
    print(s, "→", grade(s))"""
        ),
        code("# Uncomment to see a NameError, then fix it.\\n# print(undefined_name)"),
        md("Use Gemini/Grok: paste the error and ask *Explain like I am 12.* That is AI for **productivity**, not for computing the grade."),
    ],
    [
        md(header("WEEK 2 · DAY 3", "Project: Student Performance Analyzer", "Run student_analyzer.py. Add a fourth student.")),
        boot(),
        md("Open `student_analyzer.py` — every line is commented (user story + why LLM must not grade). Copy to `projects/YOUR_NAME/week02/`."),
        code("import student_analyzer\\nstudent_analyzer.report([{'name':'Ada','scores':[70,80,90]}])"),
    ],
)

# ========== WEEK 3 ==========
curriculum(
    "week03-llm-apis",
    3,
    "Large Language Models & AI APIs",
    [
        "What LLMs are",
        "Gemini, Grok, GPT/Claude (names), open-source via Ollama",
        "What an API is",
        "API keys and .env",
        "Python requests",
        "System vs user prompts",
        "Tokens, context windows, cost",
        "Limitations: hallucination, inconsistency, latency",
    ],
    [
        "Compare three models (Gemini, Grok, Ollama or DeepSeek)",
        "Prompts for summarise / generate / Q&A",
        "Estimate cost of an app (order of magnitude)",
        "Strengths and weaknesses table",
    ],
    [
        "Set up Gemini and optional Grok keys",
        ".env secrets",
        "First API call",
        "Short conversation",
        "Experiment with prompts and models",
        "Latency with ask_timed()",
    ],
    "**AI Writing Assistant** — generate, summarise, rewrite, improve.",
    extra="Test kit: [../setup/test_all_models.ipynb](../setup/test_all_models.ipynb) · [../visuals/latency.html](../visuals/latency.html) · [../visuals/api-architecture.html](../visuals/api-architecture.html)",
)
days(
    "week03-llm-apis",
    3,
    [
        md(header("WEEK 3 · DAY 1", "Theory: APIs, tokens, latency, limits", "Gemini and Grok are both kitchens. Different doors.")),
        boot(),
        md(f"""Picture: [../visuals/api-architecture.html](../visuals/api-architecture.html)

## Models you must be able to name

| Name | Who | In our code |
|---|---|---|
| **Gemini** | Google | `provider="gemini"` |
| **Grok** | xAI | `provider="grok"` |
| **DeepSeek** | DeepSeek | `provider="deepseek"` |
| **GPT** | OpenAI | *recognise only* — not required |
| **Claude** | Anthropic | *recognise only* |
| Open-source Llama | Ollama | `provider="ollama"` |

## Tokens & context window

Text is cut into **tokens**. The **context window** is the backpack size. Too much text → quality drops or errors. **Cost** ≈ input tokens + output tokens.

## Latency

Waiting time in **ms**. Measure with `ask_timed`. Fast is not always true. See [{GLOSS}]({GLOSS}) section 4 and [../visuals/latency.html](../visuals/latency.html).

## Hallucination vs inconsistency

- **Hallucination:** confident nonsense (fake fee, fake paper).
- **Inconsistency:** run 2 ≠ run 1 (stochastic).

Testing recipe: [{TEST}]({TEST})"""),
        code(
            """from jekacode.ai import ask
print(ask("Explain a token like I am 12. 4 sentences.", provider="gemini",
          system="You are a Jekacode tutor. No jargon piles."))"""
        ),
    ],
    [
        md(header("WEEK 3 · DAY 2", "Lab: call Gemini, Grok, time them", "Skip any key you do not have.")),
        boot(),
        code(
            """from jekacode.ai import ask_timed

q = "Summarise what an API is in one sentence for a POS agent in Lagos."
for p in ["gemini", "grok", "deepseek", "ollama"]:
    r = ask_timed(q, provider=p)
    print(p, "ms=", r["latency_ms"], "ok=", r["ok"])
    print((r["text"] or r["error"] or "")[:280], "\\n")"""
        ),
        md("Fill a table in your notes: provider, latency_ms, did it hallucinate a brand name?"),
    ],
    [
        md(header("WEEK 3 · DAY 3", "Project: Writing Assistant", "Four verbs: generate, summarise, rewrite, improve.")),
        boot(),
        code(
            '''from jekacode.ai import ask
W = "Writing coach for African students. Simple English."
sample = "AI na computer wey fit help people write."
print("SUMMARISE\\n", ask(f"5 bullets:\\n{sample}", system=W, provider="gemini"))
print("\\nIMPROVE\\n", ask(f"Improve grammar only:\\n{sample}", system=W, provider="gemini"))'''
        ),
        md("Try `provider=\"grok\"` on the same text. Copy into `projects/YOUR_NAME/week03/`."),
    ],
)

print("weeks 1-3 days written")
