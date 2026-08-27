"""Website page → short summary.

User story: As a student, I want a 5-bullet summary of a public webpage.

How to run:
    python interesting-projects/website-summarizer/summarize.py
Keys: guides/HOW_TO.md  (needs Gemini)

Behind the scenes: requests downloads HTML → BeautifulSoup strips tags →
we send up to 8000 characters to Gemini with “do not invent facts”.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import requests  # HTTP GET the page
from bs4 import BeautifulSoup  # parse HTML into text

from jekacode.ai import ask


def fetch_text(url: str) -> str:
    # User-Agent says who we are so some sites do not block an empty client.
    html = requests.get(url, timeout=30, headers={"User-Agent": "JekacodeStudent/1.0"}).text
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()  # drop junk so the model does not summarise menus
    text = " ".join(soup.get_text().split())  # collapse whitespace
    return text[:8000]  # cap tokens / cost / latency


def main() -> None:
    url = input("Public URL to summarise: ").strip()
    page = fetch_text(url)
    print(
        ask(
            f"Summarise this page in 5 bullets for a Nigerian SS2 student.\nURL: {url}\n\n{page}",
            provider="gemini",
            system="Do not invent facts that are not in the text.",
        )
    )


if __name__ == "__main__":
    main()
