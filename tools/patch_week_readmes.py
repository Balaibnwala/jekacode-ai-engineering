"""Prepend each week README with goals / tools / how-to / behind-the-scenes."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MARKER = "## This week — novice guide"

BRIEFS = {
    "week01-intro-to-ai": """## This week — novice guide

**What we want to achieve:** Leave Week 1 able to explain AI, ML, generative AI, LLM, and the AI Engineer job. Write a weak vs engineered prompt. Ship an AI Use Case Explorer.

**Tools:** VS Code, this repo, a browser for `visuals/`. Optional: Ollama and/or a Gemini key.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) — install VS Code + Python + venv, then Ollama (`ollama run llama3.2`) and/or Gemini (`aistudio.google.com` → `.env`).

**What goes on behind the scenes:** An LLM does **inference** (it already trained). Your prompt becomes **tokens**. The model predicts the next tokens. That feels like answering. Nobody here is training GPT.

**Class files:** `day1.ipynb` theory · `day2.ipynb` lab · `day3.ipynb` project. Every code cell comments the lines.

""",
    "week02-python": """## This week — novice guide

**What we want to achieve:** Variables, lists, dicts, functions, `if`/`for`, reading a traceback. Ship a **deterministic** Student Performance Analyzer (no LLM for marks).

**Tools:** VS Code, Python 3.11+, this notebook. Optional Gemini only to *explain* errors.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) section 0. Run `python week02-python/student_analyzer.py` from the course root.

**What goes on behind the scenes:** Python reads top to bottom. A variable is a labelled box. `70 >= 50` is exact. An LLM predicts tokens and can **hallucinate** a grade — that is why this week is ordinary software.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`. The `.py` file comments every idea.

""",
    "week03-llm-apis": """## This week — novice guide

**What we want to achieve:** Explain API, key, token, context window, **latency**, **hallucination**, **inconsistency**. Call Gemini (and Grok if you have a key). Ship a Writing Assistant.

**Tools:** `.env` with `GEMINI_API_KEY`. Optional `GROK_API_KEY`, Ollama, DeepSeek.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) sections 1–4. Test kit: [../setup/test_all_models.ipynb](../setup/test_all_models.ipynb).

**What goes on behind the scenes:** Python **POSTs JSON** to an **endpoint**. The vendor runs inference and returns tokens. You wait (latency) and may pay for tokens. Ollama is the same idea on `localhost:11434`.

**Imports you will see:** `ask` (one door), `ask_timed` (stopwatch), `dotenv` (load `.env`).

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week04-ai-apps": """## This week — novice guide

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

""",
    "week05-prompt-engineering": """## This week — novice guide

**What we want to achieve:** Role, few-shot, constraints, chaining. Reduce hallucination (“do not invent prices”). Ship a Business Assistant.

**Tools:** Gemini/Grok. Gradio or Streamlit.

**How to:**
```bash
python week05-prompt-engineering/gradio_app.py
streamlit run week05-prompt-engineering/business_assistant.py
```
[../guides/HOW_TO.md](../guides/HOW_TO.md)

**What goes on behind the scenes:** A **system prompt** is extra text prepended as policy. The model still only predicts tokens. **Chaining** = output of step 1 becomes input of step 2. Each `ask()` is a new inference (more latency).

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week06-rag": """## This week — novice guide

**What we want to achieve:** Explain LLM vs RAG. Chunk a handbook. Answer only from retrieved text. Fail on purpose when the fee is missing.

**Tools:** `knowledge/*.md`, Gemini or Grok. Gradio or Streamlit.

**How to:**
```bash
python week06-rag/gradio_app.py
streamlit run week06-rag/document_assistant.py
```
[../guides/HOW_TO.md](../guides/HOW_TO.md)

**What goes on behind the scenes:** Retrieve chunks (this week: overlapping words) → stuff them in the prompt → `ask()`. **Embeddings / vector DBs** = search by meaning (idea only). Privacy: no BVNs in Gemini.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week07-agents": """## This week — novice guide

**What we want to achieve:** Chatbot vs agent vs workflow. One agent + tools. Know tool choice can be **inconsistent**. Ship a Research Assistant.

**Tools:** Gemini/Grok. `python week07-agents/gradio_app.py` or Streamlit `research_assistant.py`.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md). Picture: [../visuals/agent-flow.html](../visuals/agent-flow.html).

**What goes on behind the scenes:** You write `search_handbook()` in Python. The LLM only plans or writes *after* the tool. Each extra `ask()` adds latency. An agent is a loop: think → tool → observe → write.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week08-automation": """## This week — novice guide

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

""",
    "week09-african-problems": """## This week — novice guide

**What we want to achieve:** Validate a real Nigerian/African problem (five questions). Language + cost + latency. YarnGPT as a *voice* option. Start the major solution (MVP).

**Tools:** Notebook, Gradio, Gemini. Optional Hugging Face / Colab for YarnGPT.

**How to:** `python week09-african-problems/gradio_app.py` · [../guides/HOW_TO.md](../guides/HOW_TO.md) section 5.

**What goes on behind the scenes:** Flash vs Ollama vs YarnGPT-on-Colab is product engineering (RAM, data bundle, audio). Translation can hallucinate idioms — `[check with a speaker]`.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week10-deploy": """## This week — novice guide

**What we want to achieve:** Prototype → public URL. Secrets on the host, never in git. Test on a phone. Note **cold start** latency.

**Tools:** GitHub. Streamlit Community Cloud or Hugging Face Space (Gradio).

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) section 12 · [../guides/fork_push_pr.md](../guides/fork_push_pr.md) · local Gradio `python week10-deploy/gradio_app.py`.

**What goes on behind the scenes:** Host clones the repo, installs requirements, injects Secrets as `os.getenv` — same names as `.env`. Cloud cannot see your laptop’s Ollama.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week11-responsible-ai": """## This week — novice guide

**What we want to achieve:** Hallucination, inconsistency, bias, prompt injection, privacy. Timed eval. Ship an Evaluation Report with **numbers**.

**Tools:** Gemini (and Grok). Gradio sandbox: `python week11-responsible-ai/gradio_app.py`.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) · [../guides/TEST_ALL_MODELS.md](../guides/TEST_ALL_MODELS.md).

**What goes on behind the scenes:** System prompts are still text. Guardrails = policy + tests, not a force field. `ask_timed` is `ask()` plus `time.perf_counter()`.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
    "week12-capstone": """## This week — novice guide

**What we want to achieve:** Eight demo answers. README a stranger can run. 6-minute rehearsal. Demo day. You engineered — you did **not** train GPT.

**Tools:** Your live URL, `presentation.md`, spare Gradio `python week12-capstone/gradio_app.py`.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) if keys broke overnight. Submit `projects/YOUR_NAME/capstone/`.

**What goes on behind the scenes:** Interviewers hire people who can say where AI sits, what remains Python, and how they tested latency and hallucination.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

""",
}


def patch(folder: str, brief: str) -> None:
    path = ROOT / folder / "README.md"
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        # Replace existing guide: from marker through the next top-level ## that is not the marker
        start = text.index(MARKER)
        # Find the official "## Outline" which should remain
        outline = text.find("## Outline", start)
        if outline == -1:
            raise SystemExit(f"no ## Outline in {folder}")
        text = text[:start] + brief + text[outline:]
    else:
        # Insert after the first heading block (title + first paragraph)
        lines = text.splitlines(keepends=True)
        # After line 0 (title) plus following non-empty intro until first ##
        i = 0
        inserted = False
        out = []
        while i < len(lines):
            out.append(lines[i])
            if lines[i].startswith("# ") and not inserted:
                # skip the rest of the lead until we hit ## Official or ## Outline or blank+##
                i += 1
                # consume the short official-format intro paragraphs
                while i < len(lines) and not lines[i].startswith("## "):
                    out.append(lines[i])
                    i += 1
                out.append("\n" if not out[-1].endswith("\n") else "")
                out.append(brief if brief.endswith("\n") else brief + "\n")
                inserted = True
                continue
            i += 1
        text = "".join(out)
    path.write_text(text, encoding="utf-8")
    print("patched", path.relative_to(ROOT))


for folder, brief in BRIEFS.items():
    patch(folder, brief)

print("week READMEs patched")
