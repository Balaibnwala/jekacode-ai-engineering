"""Chat with your documents — Week 6 RAG project (beginner retrieval).

What we achieve
    The model answers from YOUR file, not from memory. That is RAG:
    retrieve chunks, then generate. Hallucination test: ask a fee that is not in the file.

How to run
    streamlit run week06-rag/document_assistant.py
Gradio twin
    python week06-rag/gradio_app.py
Keys
    guides/HOW_TO.md
"""

# sys + Path: put the course root on the import path (same story as every week app).
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st  # website widgets
from pypdf import PdfReader  # reads pages out of a PDF upload
from jekacode.ai import ask  # LLM door
from jekacode.ui import banner  # Jekacode chrome

# Course root = parent of week06-rag. knowledge/ lives there.
ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"


def read_pdf(file) -> str:
    """Turn an uploaded PDF into one long string of text."""
    reader = PdfReader(file)  # file is the object Streamlit gives us
    # extract_text() can return None on a blank page — `or ""` keeps join happy.
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def chunk_text(text: str, size: int = 500) -> list[str]:
    """Split on words into piles of `size` words. Chunks fit the context window."""
    words = text.split()  # split() with no args = split on whitespace
    # range(start, stop, step) walks 0, 500, 1000, ...
    return [" ".join(words[i : i + size]) for i in range(0, len(words), size)]


def best_chunks(chunks: list[str], question: str, k: int = 3) -> str:
    """Rank chunks by how many question-words they contain (beginner retrieval)."""
    q = set(question.lower().split())  # set = unique words
    # sorted(..., reverse=True) puts the best overlap first.
    ranked = sorted(chunks, key=lambda c: sum(1 for w in q if w in c.lower()), reverse=True)
    return "\n\n---\n\n".join(ranked[:k])  # glue the top k with a divider


banner(st, "Chat With Your Documents", "Gemini is the student. Your file is the textbook.", layout="wide")

source = st.selectbox("Built-in document", ["school-handbook.md", "jekacode-handbook.md"])
upload = st.file_uploader("Or upload a PDF / TXT", type=["pdf", "txt", "md"])

if upload is not None:
    # Uploaded file: PDF vs plain text.
    text = read_pdf(upload) if upload.name.endswith(".pdf") else upload.read().decode("utf-8", errors="ignore")
else:
    # Built-in markdown from the knowledge folder.
    text = (KNOWLEDGE / source).read_text(encoding="utf-8")

chunks = chunk_text(text)
st.sidebar.write(f"Chunks: {len(chunks)}")  # sidebar = left column
question = st.text_input("Ask a question", placeholder="How do I request a transcript?")
provider = st.sidebar.selectbox("Model", ["gemini", "grok", "deepseek", "ollama"])

if st.button("Ask") and question:
    context = best_chunks(chunks, question)
    # ONLY the context — this instruction is the hallucination guard.
    answer = ask(
        f"Use ONLY the context. If missing, say you cannot find it in the document.\n\nCONTEXT:\n{context}\n\nQUESTION: {question}",
        provider=provider,
        system="You are a careful document assistant for Jekacode students.",
    )
    st.subheader("Answer")
    st.write(answer)
    with st.expander("Text I used"):
        # Show the retrieved chunks so a human can check the model did not invent naira.
        st.write(context)
