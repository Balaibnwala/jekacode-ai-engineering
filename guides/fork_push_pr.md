# Fork, push, and open a Pull Request

GitHub is how the class shares code. You will **fork** the course (your copy), **push** your work, and optionally open a **Pull Request (PR)** so teachers can see it.

Open this picture in your browser too: [../visuals/git-flow.html](../visuals/git-flow.html)

## Words in 12-year-old English

| Word | Meaning |
|---|---|
| **Repository (repo)** | The project folder on GitHub |
| **Fork** | Your own copy of someone else's repo, under *your* username |
| **Clone** | Download that copy to your laptop |
| **Commit** | A saved snapshot with a short message |
| **Push** | Upload your commits to GitHub |
| **Pull Request** | "Please look at my changes" — a review form |
| **`.env`** | Secret keys. **Never** commit this file |

## One-time: fork the class repo

1. Open the class repo: [https://github.com/solarinayo/jekacode-ai-engineering](https://github.com/solarinayo/jekacode-ai-engineering)
2. Click **Fork** (top right).
3. Keep the name. Click **Create fork**.
4. You now have `https://github.com/YOUR_USERNAME/jekacode-ai-engineering`.

## Clone to your laptop

```bash
git clone https://github.com/YOUR_USERNAME/THE_REPO_NAME.git
cd THE_REPO_NAME
```

In VS Code: **File → Open Folder** → that folder.

## Every week: save and push your project

Put work in `projects/YOUR_USERNAME/` (see [projects/README.md](../projects/README.md)).

Filled example to copy the *shape* from: [projects/solarinayo/](../projects/solarinayo/).

```bash
git status
git add projects/YOUR_USERNAME
git commit -m "Add week 4 study assistant"
git push
```

If GitHub asks you to sign in, use the browser or a Personal Access Token (teacher can demo once).

### If `git push` says you have no upstream

```bash
git push -u origin main
```

(Some repos use `master`. Use the name `git status` shows.)

## Open a Pull Request (PR)

Use a PR when:

- The teacher asked the class to submit via PR, **or**
- You improved a lesson and want it in the main Jekacode repo

### PR into the class/org repo

1. Push to **your fork**
2. On GitHub, open **your** repo
3. Click **Contribute** → **Open pull request**  
   (or GitHub shows a yellow banner **Compare & pull request**)
4. Base repo = Jekacode class repo · base branch = `main`  
   Head = your fork · your branch = `main` (or a feature branch)
5. Title example: `Week 4 — Ada Okafor study assistant`
6. Description: what you built, how to run it, screenshot if you have one
7. Click **Create pull request**

Do **not** include `.env`, API keys, or huge model files.

## Optional: a branch per week (tidier)

```bash
git checkout -b week-04-ada
# ... work ...
git add projects/YOUR_USERNAME/week04
git commit -m "Week 4 HTML chatbot"
git push -u origin week-04-ada
```

Then open the PR from `week-04-ada` into `main`.

## Diagram

```
Jekacode repo (upstream)
        │  fork
        ▼
Your GitHub copy (origin)
        │  clone / push
        ▼
Your laptop
        │  pull request
        ▼
Teacher reviews → merge or comment
```

## If you get stuck

| Problem | Try |
|---|---|
| `permission denied` | You are pushing to a repo you do not own. Push to **your fork**. |
| `unrelated histories` | Ask the teacher. Do not `--force` unless they say so. |
| I committed `.env` | Tell the teacher immediately. Rotate (replace) the keys. |

Week 10 repeats deploy. This page is enough to start submitting from Week 1.
