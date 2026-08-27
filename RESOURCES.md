# Jekacode resources (classroom shelf)

Adapted from the spirit of classic **AI Engineering / LLM Engineering** resource lists: tools you actually touch, papers you only *hear about*, African models you should know.

This cohort still does **not** require OpenAI or OpenRouter. Gemini, DeepSeek, Ollama, Hugging Face.

## Repo rhythm

- Latest lessons live in this GitHub repo. At the start of a week, `git pull` on your fork (or download ZIP if you must).
- Submit work with [guides/fork_push_pr.md](guides/fork_push_pr.md).
- Three classes: [guides/THREE_CLASSES.md](guides/THREE_CLASSES.md).
- Pictures: [visuals/README.md](visuals/README.md).

## Start local, then cloud

1. [Ollama](https://ollama.com) + `llama3.2` (not a 70B toy-crusher)
2. [Google AI Studio](https://aistudio.google.com/app/apikey) Gemini
3. [DeepSeek Platform](https://platform.deepseek.com)
4. [Hugging Face](https://huggingface.co) models, Spaces, YarnGPT

If Ollama fails on a PC, second terminal: `ollama serve`. Colab is a later backup, not Week 1 homework for everyone.

## Common tools (what they are for)

| Tool | In this course |
|---|---|
| **Hugging Face** | Model hub, Spaces, YarnGPT, optional inference |
| **Gradio** | Fastest Python UI (`week04-ai-apps/gradio_chat.py`) |
| **Streamlit** | Tabbed apps (study / business / RAG) |
| **HTML/CSS/JS** | Real chat product (`week04-ai-apps/html-chatbot`) |
| **LangChain** | Named in resources; we teach RAG with plain Python first |
| **Google Colab** | YarnGPT / heavier notebooks if the laptop cannot |
| **n8n** | Week 8 automations |
| Weights & Biases, SageMaker, Bedrock, Vertex | Not required. Know the names for interviews. |

## African / local language

- [YarnGPT](https://huggingface.co/saheedniyi/YarnGPT) — Nigerian-accented English TTS  
- [YarnGPT-local](https://huggingface.co/saheedniyi/YarnGPT-local) — Yoruba, Igbo, Hausa  
- [yarngpt.co](https://yarngpt.co/) · [GitHub](https://github.com/saheedniyi02/yarngpt)  
- Classroom wrapper: [interesting-projects/yarngpt-voice-notice](interesting-projects/yarngpt-voice-notice)

## Frontier chat (for your curiosity — not homework APIs)

Gemini, DeepSeek, Claude, Mistral, Llama via Meta.ai, Perplexity. Compare *ideas* in a browser. Build with the classroom providers.

## Papers (teacher mentions, not exams)

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformers  
- [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922) — bias and hype  
- Chinchilla scaling (size of data vs size of model) — one slide, no maths homework  

## Leaderboards (optional browsing)

[Artificial Analysis](https://artificialanalysis.ai) · [Hugging Face leaderboards](https://huggingface.co/collections) · [LM Arena](https://lmarena.ai)

## Real products (why this job exists)

Harvey (law) · Khanmigo (education) · health copilots · code-porting tools. Jekacode parallel: school handbook, SME inbox, farm FAQ, scholarship search.

## Hugging Face + Gradio deploy

Week 10: Streamlit Cloud **or** a Hugging Face Space running Gradio. Same `ask()` helper.

## Extra builds

[interesting-projects/README.md](interesting-projects/README.md) — summarizer, YarnGPT notice, HTML chat.
