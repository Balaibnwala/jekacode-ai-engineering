# Step 3 — GitHub (where your projects live)

GitHub is like Google Drive for code. You will put every weekly project in the `projects/` folder, then save it to GitHub.

## Create an account

1. Go to [https://github.com/signup](https://github.com/signup)
2. Use an email you can check.
3. Pick a simple username. This username will be your folder name later.

## Install Git

**Mac:** open Terminal and run `git --version`. If macOS offers to install developer tools, say yes.

**Windows:** install [Git for Windows](https://git-scm.com/download/win) and use the default options.

## First-time Git identity (once)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
```

## How you will submit work

Every week:

1. Copy the week template into `projects/YOUR_GITHUB_USERNAME/`
2. Build your project there
3. Ask the teacher how to push (Week 10 teaches this fully)

Until Week 10, you can zip your `projects/YOUR_GITHUB_USERNAME` folder and send it if needed.

Full picture: **[guides/fork_push_pr.md](../guides/fork_push_pr.md)** — fork the class repo, `git push` your folder, open a **Pull Request** so teachers can review. Never commit `.env`.

Read [projects/README.md](../projects/README.md) next.

Next: [05_ollama.md](05_ollama.md) (do this before Week 1 Class 3), then [04_api_keys.md](04_api_keys.md).
