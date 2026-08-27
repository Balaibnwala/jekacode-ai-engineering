"""
Jekacode HTML chatbot backend.

User story: As a student, I want a WhatsApp-like window in my browser.
Use case: Type a question → JavaScript POSTs JSON → Python calls ask() → bubble shows the reply.

How to run (course root so jekacode imports):
    python week04-ai-apps/html-chatbot/server.py
Then open http://127.0.0.1:5000

Keys / Ollama: guides/HOW_TO.md
Line-by-line frontend: EXPLAINED.md and comments in app.js
"""

import sys
from pathlib import Path

# This folder → week04-ai-apps → course root (where the jekacode package lives).
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

# Flask = tiny web framework. jsonify packs Python dicts as JSON for the browser.
# request = the incoming HTTP request. send_from_directory = serve a static file.
from flask import Flask, jsonify, request, send_from_directory

from jekacode.ai import ask  # same door the notebooks use

HERE = Path(__file__).resolve().parent  # html-chatbot folder
app = Flask(__name__)  # the web application object


@app.get("/")
def home():
    """GET /  → send the chat page (HTML). The browser then requests CSS/JS itself."""
    return send_from_directory(HERE, "index.html")


@app.get("/styles.css")
def css():
    """GET /styles.css → colours, layout (navy + green)."""
    return send_from_directory(HERE, "styles.css")


@app.get("/app.js")
def js():
    """GET /app.js → what happens when you click Send."""
    return send_from_directory(HERE, "app.js")


@app.get("/logo.png")
def logo():
    """GET /logo.png → official Jekacode mark from assets/."""
    return send_from_directory(ROOT / "assets", "jekacode-logo.png")


@app.post("/chat")
def chat():
    """
    POST /chat
    Body JSON: { "message": "Explain gravity", "provider": "gemini" }
    Returns: { "reply": "..." }
    Behind the scenes: this is the backend hop. ask() then hops again to the model.
    """
    data = request.get_json(silent=True) or {}  # silent=True → None instead of crash
    message = (data.get("message") or "").strip()
    provider = (data.get("provider") or "gemini").strip()
    if not message:
        return jsonify({"error": "Type a message first."}), 400  # 400 = bad request
    system = (
        "You are a kind Jekacode tutor for African beginners. "
        "Short answers. Simple English. No fake citations."
    )
    try:
        reply = ask(message, provider=provider, system=system)
    except Exception as error:
        return jsonify({"error": str(error)}), 500  # 500 = our server / key / network
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # debug=True auto-reloads when you save. Use only on your laptop.
    # host 127.0.0.1 = this computer only, not the whole cafe Wi‑Fi.
    app.run(host="127.0.0.1", port=5000, debug=True)
