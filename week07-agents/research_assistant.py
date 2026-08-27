"""AI Research Assistant — Week 7. One agent, two tools.

What we achieve
    Topic in → (1) outline tasks with an LLM (2) search a local handbook with Python
    → (3) write a report that admits what we do not know.

How to run
    streamlit run week07-agents/research_assistant.py
Gradio twin
    python week07-agents/gradio_app.py
Keys
    guides/HOW_TO.md
"""

import sys
from pathlib import Path

# Course root on sys.path so `import jekacode` works.
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from jekacode.ai import ask
from jekacode.ui import banner

ROOT = Path(__file__).resolve().parents[1]
# Tool memory: a markdown file, not the internet.
HANDBOOK = (ROOT / "knowledge" / "jekacode-handbook.md").read_text(encoding="utf-8")


def search_handbook(query: str) -> str:
    """Deterministic tool: pick the heading-chunk that shares the most words."""
    q = set(query.lower().split())
    parts = [p.strip() for p in HANDBOOK.split("##") if p.strip()]
    parts = sorted(parts, key=lambda p: sum(1 for w in q if w in p.lower()), reverse=True)
    return parts[0][:800] if parts else "Nothing found."


def outline(topic: str) -> str:
    """LLM tool: break a topic into tasks. This CAN be inconsistent if you rerun."""
    return ask(
        f"Break this research topic into 4 tasks:\n{topic}",
        system="Numbered list only.",
    )


banner(st, "AI Research Assistant", "Goal → pick tools → organise → report")

topic = st.text_input("Research request", placeholder="Explain the Jekacode AI Engineering programme to a parent")
provider = st.selectbox("Model", ["gemini", "grok", "deepseek", "ollama"])

if st.button("Run agent") and topic:
    # spinner = latency honesty. Two ask() calls will wait.
    with st.spinner("Thinking..."):
        tasks = outline(topic)  # hop 1: LLM
        notes = search_handbook(topic)  # Python, not LLM
        report = ask(
            f"Write a structured report with headings: Problem, Facts we have, What we still don't know, Next step.\n"
            f"Topic: {topic}\nTasks:\n{tasks}\nNotes:\n{notes}",
            provider=provider,
            system="Honest. If notes are weak, say so. You are a Jekacode research intern.",
        )  # hop 2: LLM uses tool output
    st.subheader("Tasks")
    st.write(tasks)
    st.subheader("Tool: handbook search")
    st.write(notes)
    st.subheader("Report")
    st.write(report)
