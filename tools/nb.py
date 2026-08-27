"""Helpers for writing Jekacode lesson notebooks."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def src(text: str) -> list[str]:
    if not text.endswith("\n"):
        text += "\n"
    return text.splitlines(keepends=True)


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": src(text)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": src(text),
    }


def header(week: str, title: str, subtitle: str, depth: int = 1) -> str:
    logo = ("../" * depth) + "assets/jekacode-logo.png"
    return f"""<div style="background:#03045E;padding:28px 32px;border-radius:16px;font-family:Arial,sans-serif;">
<img src="{logo}" alt="Jekacode" width="240"/>
<p style="color:#16D365;font-size:12px;letter-spacing:2.5px;margin:18px 0 6px 0;">JEKACODE AI ENGINEERING · {week}</p>
<h1 style="color:#ffffff;margin:0;font-size:28px;">{title}</h1>
<p style="color:#d7deea;margin:10px 0 0 0;font-size:16px;">{subtitle}</p>
</div>"""


def note(title: str, body: str) -> str:
    return f"""<div style="border-left:6px solid #16D365;background:#F4F6FB;padding:14px 16px;border-radius:0 8px 8px 0;font-family:Arial,sans-serif;">
<strong style="color:#03045E;">{title}</strong>
<p style="margin:8px 0 0 0;color:#1b1f2a;">{body}</p>
</div>"""


def boot() -> dict:
    """First code cell so `import jekacode` works from a week folder."""
    return code(
        '''# --- Why this cell exists (read once) ---
# Python only finds packages that live on a list of folders called sys.path.
# This notebook sits in a week folder. The jekacode helper lives one folder up.
# Novices: you are not "hacking". You are telling Python where the course lives.

import sys
# sys = the "system" module. We use it to change where Python looks for imports.

from pathlib import Path
# Path is a friendly way to talk about folders. It works on Mac, Windows, and Linux.

root = Path.cwd()
# cwd = current working directory = "the folder this notebook thinks it is in".

if not (root / "jekacode").exists():
    # If we cannot see the jekacode folder here, we are inside week01, week02, ...
    root = root.parent
    # parent = the folder above this one (the course root).

if str(root) not in sys.path:
    sys.path.append(str(root))
    # Now `from jekacode.ai import ask` can succeed.

print("Course folder Python will use:", root)
print("You should see jekacode inside that folder.")'''
    )


def week_open(goal: str, tools: str, how: str, behind: str) -> dict:
    """Standard start-of-week / start-of-day briefing for novices."""
    return md(
        f"""## What we want to achieve

{goal}

## Tools you need (names only)

{tools}

## How to (do these before the first code cell if you have not)

{how}

## What goes on behind the scenes

{behind}

**Keys & installs (bookmark):** [../guides/HOW_TO.md](../guides/HOW_TO.md) · **Terms:** [../guides/AI_ENGINEERING_TERMS.md](../guides/AI_ENGINEERING_TERMS.md)"""
    )



def write_nb(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    nb = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python (Jekacode)",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "cells": cells,
    }
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    print("wrote", path.relative_to(ROOT))


def week_readme(folder: str, number: int, title: str, blurb: str, learn: list[str], project: str, days: list[tuple[str, str]]) -> None:
    learn_list = "\n".join(f"- {item}" for item in learn)
    days_list = "\n".join(f"- **{k}:** {v}" for k, v in days)
    write_text(
        ROOT / folder / "README.md",
        f"""# Week {number} — {title}

{blurb}

## You will learn

{learn_list}

## This week's files

- `01_learn.ipynb` — ideas
- `02_lab.ipynb` — you type
- Project: **{project}**

## Suggested days

{days_list}

## Submit

Copy your project into `projects/YOUR_NAME/week{number:02d}/` and write five lines: what you built, who it helps, how to run it, what was hard, what you would improve.
""",
    )
