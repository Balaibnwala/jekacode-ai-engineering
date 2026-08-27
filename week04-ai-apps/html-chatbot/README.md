# HTML / CSS / JS chatbot

**User story:** As a student, I want a chat that looks like a real website, not a notebook.

**Architecture**

```
Browser (index.html + styles.css + app.js)
        ↓  POST /chat  { message, provider }
Flask (server.py)
        ↓  ask()
Gemini / DeepSeek / Ollama
        ↓
JSON { reply }
        ↓
Green / navy bubbles
```

## Run

From the **course root**, with `.venv` on:

```bash
python week04-ai-apps/html-chatbot/server.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

Need Ollama? Start it first. Need Gemini? `.env` must have `GEMINI_API_KEY`.

Every line: [EXPLAINED.md](EXPLAINED.md)

Copy this folder into `projects/YOUR_NAME/week04/` when it works.
