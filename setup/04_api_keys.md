# API keys — Gemini, Grok, DeepSeek

**Full novice walkthrough (screens, `.env`, errors):** [../guides/HOW_TO.md](../guides/HOW_TO.md) sections 2–4.

This course does **not** require OpenAI or OpenRouter.

Classroom models:

| Provider | Where you get a key | Typical use |
|---|---|---|
| **Gemini** | [Google AI Studio](https://aistudio.google.com/app/apikey) | Main class model (often free tier) |
| **Grok** | [xAI console](https://console.x.ai) | Compare style/speed with Gemini |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | Cheap second cloud model |
| **Ollama** | none — [setup/05_ollama.md](05_ollama.md) | Local, private, may be slower |
| **Hugging Face** | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Hub + optional inference |

You do **not** need every key on day 1. Gemini + Ollama is enough to start. Add Grok when the teacher says “compare three models.”

## Gemini

1. [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Create API key → paste as `GEMINI_API_KEY`
3. Default model: `gemini-2.0-flash` (fast). You may try `gemini-2.5-flash` if your account has it.

## Grok (xAI)

1. Open [console.x.ai](https://console.x.ai)
2. Create an API key
3. Paste as `GROK_API_KEY`
4. Default model env: `GROK_MODEL=grok-3-mini` (smaller/faster). If xAI lists a newer name in your dashboard, put that name in `.env`.

## DeepSeek

Same as before: [platform.deepseek.com](https://platform.deepseek.com) → `DEEPSEEK_API_KEY`

## `.env` example

```
GEMINI_API_KEY=...
GROK_API_KEY=...
DEEPSEEK_API_KEY=...
```

Never screenshot this file. Never commit it.

## Test every model you have

Open [test_all_models.ipynb](test_all_models.ipynb) or [../guides/TEST_ALL_MODELS.md](../guides/TEST_ALL_MODELS.md).

If Gemini prints `Jekacode is ready`, the main path works.
