# YarnGPT — local language voice

[YarnGPT](https://huggingface.co/saheedniyi/YarnGPT) (Saheed Azeez) speaks **Nigerian-accented English**.  
[YarnGPT-local](https://huggingface.co/saheedniyi/YarnGPT-local) speaks **Yoruba, Igbo, and Hausa**.

Repo: [github.com/saheedniyi02/yarngpt](https://github.com/saheedniyi02/yarngpt) · site: [yarngpt.co](https://yarngpt.co/)

## User story

> As a school admin, I want a short voice notice in Yoruba so parents who prefer audio can hear assembly changes.

## Trade-off (read this on the projector)

| Path | What you get | Cost on a school laptop |
|---|---|---|
| Gemini `ask()` in Yoruba/Pidgin **text** | Always works in class | Low |
| YarnGPT **demo / Colab / Space** | Real Nigerian voices | Needs download + often GPU |
| Install full YarnGPT weights locally | Best control | Can freeze a weak PC |

**AI engineering choice:** generate the script with Gemini, generate the voice where the machine allows.

## Class path (always)

1. Write the notice in English.
2. Ask Gemini to translate to Yoruba *or* Igbo *or* Hausa *or* Nigerian Pidgin (you check with a speaker).
3. Paste into [YarnGPT Colab / model card demo](https://huggingface.co/saheedniyi/YarnGPT-local) if the teacher opened it.
4. Keep the text in `notice.md` for your GitHub project even if audio failed.

Run:

```bash
python interesting-projects/yarngpt-voice-notice/make_notice.py
```

Do not pretend the laptop “ran YarnGPT” if you only used Gemini text. Honesty is Week 11 energy.
