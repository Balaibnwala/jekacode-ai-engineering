# MODULE 10 — Building & Deploying AI Products

**day1.ipynb** theory · **day2.ipynb** lab · **day3.ipynb** project.  
Terms: [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)

## This week — novice guide

**What we want to achieve:** Prototype → public URL. Secrets on the host, never in git. Test on a phone. Note **cold start** latency.

**Tools:** GitHub. Streamlit Community Cloud or Hugging Face Space (Gradio).

**How to:** [../guides/HOW_TO.md](../guides/HOW_TO.md) section 12 · [../guides/fork_push_pr.md](../guides/fork_push_pr.md) · local Gradio `python week10-deploy/gradio_app.py`.

**What goes on behind the scenes:** Host clones the repo, installs requirements, injects Secrets as `os.getenv` — same names as `.env`. Cloud cannot see your laptop’s Ollama.

**Class files:** `day1.ipynb` · `day2.ipynb` · `day3.ipynb`.

## Outline

1. Prototype → product
2. Full-stack AI
3. Frontend/backend
4. Application data
5. Auth intro
6. Testing (including models)
7. Environment variables
8. Deploy
9. GitHub

## Tasks

- Architecture diagram
- Document features
- Sensitive info
- Test with users
- Deploy checklist

## Labs

- Connect FE/BE
- Store data (simple)
- Basic auth idea
- Env vars on host
- Deploy

## Project

**Deploy** one previous app (Streamlit Cloud or Hugging Face Space). Live link.

[../guides/fork_push_pr.md](../guides/fork_push_pr.md) · [../visuals/git-flow.html](../visuals/git-flow.html)

Submit: `projects/YOUR_NAME/week10/` · [PR guide](../guides/fork_push_pr.md)
