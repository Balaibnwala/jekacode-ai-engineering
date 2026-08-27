// app.js — behaviour for the Jekacode HTML chat (Week 4).
// The browser already loaded index.html. This file runs after that.
// How to run the server: python week04-ai-apps/html-chatbot/server.py
// Then open http://127.0.0.1:5000

// getElementById finds a tag by id="..." in the HTML.
const log = document.getElementById("log");       // where bubbles appear
const form = document.getElementById("form");     // the Send form
const input = document.getElementById("input");   // the text box
const provider = document.getElementById("provider"); // Gemini / Grok / ...

function addBubble(text, kind) {
  // createElement makes a new <div> in memory (not yet on screen).
  const div = document.createElement("div");
  // className becomes class="bubble user" or "bubble bot" (CSS colours).
  div.className = "bubble " + kind;
  // textContent = safe text (will not run HTML). Stops injection in the bubble.
  div.textContent = text;
  log.appendChild(div);              // actually put it in the log
  log.scrollTop = log.scrollHeight;  // scroll to the newest bubble
}

// addEventListener("submit") runs when the user hits Send or Enter.
form.addEventListener("submit", async (event) => {
  event.preventDefault(); // stop the browser refreshing the whole page
  const message = input.value.trim(); // trim() drops leftover spaces
  if (!message) return;               // empty send → do nothing (save latency/cost)
  addBubble(message, "user");
  input.value = "";                   // clear the box
  addBubble("Thinking…", "bot");      // latency honesty — people wait
  const waiting = log.lastChild;      // that "Thinking…" bubble, so we can remove it
  try {
    // fetch = HTTP from the browser. POST /chat hits Flask in server.py.
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" }, // we are sending JSON
      body: JSON.stringify({ message: message, provider: provider.value }),
    });
    const data = await response.json(); // parse the JSON Python sent back
    waiting.remove();
    if (data.error) addBubble(data.error, "err");
    else addBubble(data.reply, "bot");
  } catch (error) {
    waiting.remove();
    addBubble("Could not reach the Python server. Is it running?", "err");
  }
});

addBubble("Hi. I am the Jekacode study chat. Ask me a school question.", "bot");
