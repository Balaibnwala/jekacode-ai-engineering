# Deploy notes (Streamlit Community Cloud)

1. Push your app Python file to GitHub.
2. Go to https://share.streamlit.io
3. New app → pick the repo, the file (`study_assistant.py` etc.).
4. Add secrets: `GEMINI_API_KEY`, optional `DEEPSEEK_API_KEY`.
5. Install is automatic from `requirements.txt` at the repo root.

If the logo path breaks in the cloud, remove `st.image("../assets/...")` or point it at a raw GitHub URL for `assets/jekacode-logo.png`.
