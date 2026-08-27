# MODULE 6 — RAG & Knowledge-Based AI Systems

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

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

## Outline

1. Retrieval-Augmented Generation
2. Why models hallucinate
3. Knowledge bases
4. Documents and AI
5. Chunking
6. Embeddings (idea)
7. Vector databases (idea)
8. Retrieval and context
9. Simple RAG app

## Tasks

- LLM vs RAG
- Normal chat vs document chat
- Knowledge base for an organisation
- Try different chunk sizes
- When RAG is the right tool

## Labs

- Upload/process docs
- Split chunks
- Embeddings (optional later)
- Store (even a Python list)
- Retrieve
- Chatbot from documents

## Project

**AI Document Assistant** — school / Jekacode / SME policy handbook.

[../visuals/rag-flow.html](../visuals/rag-flow.html)

Submit: `projects/YOUR_NAME/week06/` · [PR guide](../guides/fork_push_pr.md)
