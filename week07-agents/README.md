# MODULE 7 — AI Agents & Tool Calling

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Chatbot vs agent vs workflow. One agent + tools. Know tool choice can be **inconsistent**. Ship a Research Assistant.

**Tools:** Gemini/Grok. `python week07-agents/gradio_app.py` or Streamlit `research_assistant.py`.

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md). Picture: [../visuals/agent-flow.html](../visuals/agent-flow.html).

**What goes on behind the scenes:** You write `search_handbook()` in Python. The LLM only plans or writes *after* the tool. Each extra `ask()` adds latency. An agent is a loop: think → tool → observe → write.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. AI agents
2. Agents vs chatbots
3. Agents vs workflows
4. Tools and function calling
5. External tools
6. Decision-making
7. Multi-step tasks
8. Memory (tiny)
9. Simple agents

## Tasks

- Five agent-suitable tasks
- Chatbot vs agent
- Design a workflow
- Define tools
- Multi-step agent

## Labs

- First agent
- Function calling (simple)
- Connect tools
- Research workflow
- Test decisions (inconsistency!)

## Project

**AI Research Assistant** — request → tasks → tools → report.

[../visuals/agent-flow.html](../visuals/agent-flow.html)

Submit: `projects/YOUR_NAME/week07/` · [PR guide](../guides/fork_push_pr.md)
