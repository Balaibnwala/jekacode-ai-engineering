# Every file, why it exists

## User story

> As Ada in SS2, I want to ask study questions in a window that looks like WhatsApp so I can screenshot it for my portfolio.

## Use case

Classroom and capstone: one local URL, navy/green Jekacode brand, choice of Gemini or Ollama.

---

## `index.html` — the skeleton

| Bit | What it is for |
|---|---|
| `<!DOCTYPE html>` | Tells the browser this is modern HTML |
| `<link rel="stylesheet" href="/styles.css">` | Load colours and layout |
| `<img src="/logo.png">` | Official logo (Flask serves the file from `assets/`) |
| `<select id="provider">` | Which kitchen: Gemini, DeepSeek, or Ollama |
| `<main id="log">` | Where bubbles appear |
| `<form id="form">` | Send button + text box |
| `<script src="/app.js">` | Behaviour (must be last so the HTML exists first) |

## `styles.css` — the look

| Bit | What it is for |
|---|---|
| `--navy` `--green` | Official Jekacode colours |
| `body` background navy | Brand canvas |
| `.bubble.user` green | Your messages |
| `.composer` flex | Input + Send on one row |

## `app.js` — the behaviour

| Line idea | What it is for |
|---|---|
| `getElementById` | Find the box, form, log |
| `addBubble` | Create a `<div>` and put text in it |
| `submit` + `preventDefault` | Stop the page from refreshing |
| `fetch("/chat", { method: "POST", ...})` | Talk to Python |
| `JSON.stringify` | Turn JS object into text the server understands |
| `data.reply` | Show the model’s answer |

## `server.py` — the brain

| Bit | What it is for |
|---|---|
| `sys.path.append(ROOT)` | So `import jekacode` works |
| `Flask(__name__)` | Create the web app |
| `@app.get("/")` | Homepage |
| `@app.post("/chat")` | Receive the question |
| `ask(...)` | Same helper as notebooks |
| `jsonify` | Send JSON back to `app.js` |
| `app.run(port=5000)` | Listen on your laptop |

**Trade-off:** HTML is more files than Gradio. Gradio is one file. HTML looks like a product. You will use both in this week.
