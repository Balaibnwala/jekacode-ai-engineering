# Hugging Face — the model market

Hugging Face is not one chatbot. It is a **hub**: models, datasets, demo apps (Spaces), and leaderboards.

Think: GitHub, but for AI models.

## Create an account

1. [https://huggingface.co/join](https://huggingface.co/join)
2. Confirm email
3. Optional token: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
   Create a **Read** token. Put it in `.env` as `HF_TOKEN=...`

You can browse without a token. A token is for calling hosted models from Python.

## What you will click in class

| Place | Why |
|---|---|
| [huggingface.co/models](https://huggingface.co/models) | Search `text-generation`, `yoruba`, `tts` |
| [saheedniyi/YarnGPT](https://huggingface.co/saheedniyi/YarnGPT) | Nigerian-accented English speech |
| [saheedniyi/YarnGPT-local](https://huggingface.co/saheedniyi/YarnGPT-local) | Yoruba, Igbo, Hausa speech |
| [huggingface.co/spaces](https://huggingface.co/spaces) | Click-to-try demos (Gradio) |
| [huggingface.co/docs/hub/spaces-sdks-gradio](https://huggingface.co/docs/hub/spaces-sdks-gradio) | Deploy a Gradio app |

## Classroom rule

Running YarnGPT **weights** on a school laptop can be heavy (download + GPU). Default path:

1. Understand the **idea** (text in → Nigerian voice out)
2. Try the official demo / Colab from the model card
3. Your app can still **write** Yoruba/Pidgin with Gemini, then a human plays it in YarnGPT

That is AI engineering: pick the right tool for the machine you have.

## Python helper

```python
from jekacode.ai import ask
print(ask("Say hello in one line.", provider="huggingface"))
```

If this errors, use `provider="ollama"` or `provider="gemini"`. Hugging Face hosted models change often; Ollama and Gemini are the reliable class demo.
