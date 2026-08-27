# Capstone — School Gate Notice + Study Helper (sample)

**Name:** Solarin Ayo (`solarinayo`)  
**Product name:** Jekacode Gate Notice  
**Live link:** *paste after Week 10 deploy*  
**GitHub:** `projects/solarinayo/`

This is a **sample** capstone README. Students replace every line with their own product.

## 1. Problem

Parents miss English-only assembly changes. SS2 students have long notes and no short explanations before tests.

## 2. Users

Lagos public-school parents (Yoruba / Pidgin) and SS2 science students on Android, often on small data bundles.

## 3. Solution

A small Gradio/Streamlit app: paste an English notice → draft in the language they asked for, with `[check with a speaker]`. Second tab: explain a WAEC topic in under 180 words.

## 4. Technology

VS Code · Python · Gradio or Streamlit · `jekacode.ai.ask()` · Gemini Flash (Grok optional) · Ollama when there is no data · secrets in `.env` / host Secrets

## 5. Where AI is used

Only inside `ask()`. Language choice, buttons, and “do not send until a human reads it” are ordinary Python. Grades and school fees must not be invented — RAG / refuse.

## 6. How to demo (click by click)

1. Open the live URL (or `python week09-african-problems/gradio_app.py`)
2. Paste: “Assembly is moved to 8:15am. Wear white.”
3. Ask for Yoruba. Show the `[check with a speaker]` line
4. Switch to Study Assistant: explain photosynthesis for JSS
5. Say out loud: latency number + one hallucination you caught

Timebox: 6 minutes.

## 7. Challenges

- Phone-data **latency** and Gemini **429** during rehearsal  
- Translation can **hallucinate** idioms  
- Almost committed `.env` (Week 10)

## 8. What you would improve

YarnGPT voice on Hugging Face Space/Colab. A real parent as tester. A tiny eval table from Week 11 in the repo.

## How to run locally

```bash
# from course root, (.venv) on, GEMINI_API_KEY in .env
python week09-african-problems/gradio_app.py
streamlit run week04-ai-apps/study_assistant.py
```

I did **not** train GPT. I engineered a product around a model, kept secrets off git, and tested hallucination and latency.
