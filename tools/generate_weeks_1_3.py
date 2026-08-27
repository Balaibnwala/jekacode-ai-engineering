from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nb import ROOT, code, header, md, note, week_readme, write_nb, write_text

write_nb(
    ROOT / "setup/check_setup.ipynb",
    [
        md(header("SETUP", "Is your computer ready?", "Run every cell. Green text is good. Red text is a clue.", 1)),
        md("If a cell fails, read [setup/README.md](README.md) again. Ask Gemini: *Explain this error like I am 12.*"),
        code("import sys\nprint('Python version:', sys.version.split()[0])\nprint('You want 3.11 or newer.')"),
        code("from pathlib import Path\nprint('Course folder:', Path.cwd())"),
        code("from jekacode.brand import NAVY, GREEN\nprint('Navy', NAVY)\nprint('Green', GREEN)\nprint('Brand colours loaded.')"),
        code(
            "from jekacode.ai import ask\n\nprint('Trying Gemini...')\nprint(ask('Reply with exactly this sentence: Jekacode is ready.', provider='gemini'))"
        ),
        md(note("DeepSeek is optional today", "If you do not have a DeepSeek key yet, skip the next cell. Gemini is enough for class.")),
        code(
            "from jekacode.ai import ask\n\nprint('Trying DeepSeek...')\nprint(ask('Reply with exactly this sentence: DeepSeek is ready.', provider='deepseek'))"
        ),
        md("### You are ready when Gemini answered.\nOpen [../week01-intro-to-ai/README.md](../week01-intro-to-ai/README.md)."),
    ],
)

week_readme(
    "week01-intro-to-ai",
    1,
    "Introduction to AI & AI Engineering",
    "This week is mostly talking and thinking. You will finish knowing what AI is, what generative AI is, what an LLM is, and what an AI Engineer does.",
    [
        "AI is the big field of computers doing thinking-like jobs",
        "Generative AI creates new text (and more)",
        "LLMs are the talking models behind Gemini and DeepSeek",
        "AI Engineers build useful apps around those models",
        "A good prompt is a clear instruction",
    ],
    "AI Use Case Explorer",
    [
        ("Day 1", "What is AI?"),
        ("Day 2", "ML vs Generative AI vs LLMs"),
        ("Day 3", "How a chat app works + careers"),
        ("Day 4", "Prompt practice"),
        ("Day 5", "Use-case project"),
    ],
)

write_nb(
    ROOT / "week01-intro-to-ai/01_learn.ipynb",
    [
        md(header("WEEK 1", "What is AI, really?", "Plain words. No scary maths.")),
        md(
            """## The 12-year-old version

A computer is usually a very fast rule-follower. If you write `2 + 2`, it will not suddenly write a poem.

**AI** is when we build computer systems that can do jobs that used to need a person's judgement: spotting a face in a photo, suggesting the next word in a sentence, recommending a song.

**Machine Learning** is one way to make AI. Instead of writing every rule, we show the computer many examples and it finds patterns.

**Generative AI** is AI that *makes* new stuff: a paragraph, a quiz, a caption for a shop on Instagram.

A **Large Language Model (LLM)** is generative AI trained on a huge amount of text. Gemini and DeepSeek are LLMs. They predict useful next words, which feels like understanding.

An **AI Engineer** is not only a chatter. They connect the model to a real problem: a school handbook, a shop inbox, farm questions, exam practice."""
        ),
        md(
            """## Four jobs people mix up

| Role | Everyday sentence |
|---|---|
| Software Engineer | Builds apps and websites |
| Data Scientist | Finds stories in numbers |
| Machine Learning Engineer | Trains models from data |
| **AI Engineer** | Uses models (like Gemini) to build products people can use |

In this Jekacode cohort, you are training to be an **AI Engineer**."""
        ),
        md(
            """## How a chat system works

```
You type a question
        ↓
The app adds extra instructions (a "system prompt")
        ↓
The app sends the text over the internet (an API request)
        ↓
Gemini or DeepSeek writes a reply
        ↓
The app shows the reply on the screen
```

Later weeks turn this picture into real code."""
        ),
        md(note("Remember this", "AI is the field. Generative AI creates content. LLMs talk. AI Engineers build apps.")),
        md("## Try a tiny Python cell\n\nYou are still allowed to be a beginner. This only prints a sentence."),
        code('print("I am learning AI Engineering at Jekacode.")'),
        md(
            """## Class question (write your answer in the next cell)

If you could give Gemini access to a **school database**, **shop records**, or **farm advice**, what would you build?"""
        ),
        code('idea = """\\nMy idea:\\nWho it helps:\\n"""\\nprint(idea)'),
    ],
)

write_nb(
    ROOT / "week01-intro-to-ai/02_lab.ipynb",
    [
        md(header("WEEK 1 LAB", "Prompts and use cases", "A prompt is just a clear instruction.")),
        md(
            """## Weak vs better

**Weak:** Write about Python.

**Better:** You are a Python instructor teaching absolute beginners in Lagos. Explain Python using a school result-sheet example. Keep it under 120 words. Use simple English.

A strong prompt usually has:

1. **Role** — who the AI should be
2. **Task** — what to do
3. **Context** — who it is for
4. **Limits** — length, language, format"""
        ),
        code(
            """weak = "Write about Python."
better = (
    "You are a Python instructor teaching absolute beginners in Lagos. "
    "Explain Python using a school result-sheet example. "
    "Keep it under 120 words. Use simple English."
)
print("WEAK:\\n", weak)
print("\\nBETTER:\\n", better)"""
        ),
        md("### Optional: send the better prompt to Gemini (needs your `.env` key)"),
        code('from jekacode.ai import ask\n\nprint(ask(better, provider="gemini"))'),
        md(
            """## Lab tasks (type in the cells)

1. Write 10 problems AI might help with (school, market, clinic, farm, transport).
2. Name 3 AI products you already use or have seen.
3. Pick **one Nigerian or African problem**. Who has it? How do they cope today?"""
        ),
        code(
            """problems = [
    "1. ",
    "2. ",
    "3. ",
    "4. ",
    "5. ",
    "6. ",
    "7. ",
    "8. ",
    "9. ",
    "10. ",
]
for item in problems:
    print(item)"""
        ),
        code(
            """products = ["", "", ""]
african_problem = {
    "who": "",
    "how_often": "",
    "current_fix": "",
    "why_not_enough": "",
    "can_ai_help": "",
}
print(products)
print(african_problem)"""
        ),
        md("Save your answers. Copy them into `projects/YOUR_NAME/week01/` for the **AI Use Case Explorer**."),
    ],
)

week_readme(
    "week02-python",
    2,
    "Python Programming for AI",
    "Python is how you give the computer a recipe. This week is slow on purpose. Same idea every time: input → process → output.",
    [
        "Variables, strings, numbers",
        "Lists and dictionaries",
        "if / else, loops, functions",
        "Reading a simple error message",
        "A tiny student score programme",
    ],
    "Student Performance Analyzer",
    [
        ("Day 1", "What Python is, variables, types"),
        ("Day 2", "Lists and dictionaries"),
        ("Day 3", "if and loops"),
        ("Day 4", "Functions and errors"),
        ("Day 5", "Analyzer project"),
    ],
)

write_nb(
    ROOT / "week02-python/01_learn.ipynb",
    [
        md(header("WEEK 2", "Python, like a recipe", "A variable is a labelled box. A function is a named recipe.")),
        md(
            """## Input → process → output

You will use this forever, including with AI:

```
User input  →  your code / AI model  →  useful output
```

Today the "model" is just your own Python."""
        ),
        code(
            """# A labelled box
student = "Chidi"
score = 78
passed = score >= 50

print(student)
print(score)
print("Passed?", passed)"""
        ),
        md("## Lists (a row of lockers) and dictionaries (a form with named fields)"),
        code(
            """scores = [70, 85, 40, 90]
print("First score:", scores[0])
print("How many:", len(scores))

student = {"name": "Amaka", "score": 88, "city": "Enugu"}
print(student["name"], "scored", student["score"])"""
        ),
        md("## if, loops, functions"),
        code(
            """def grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

for s in [88, 61, 49]:
    print(s, "→", grade(s))"""
        ),
        md(note("When it breaks", "Read the last line of the error. It often names the file, the line, and the missing name. That is the treasure map.")),
        code("# This cell is supposed to fail. Uncomment it, run it, read the error, then fix it.\n# print(undefined_name)"),
    ],
)

write_nb(
    ROOT / "week02-python/02_lab.ipynb",
    [
        md(header("WEEK 2 LAB", "Build a Student Performance Analyzer", "Collect scores, average them, give a grade, print a report.")),
        md("Fill the gaps. Run often. Tiny changes beat giant mystery code."),
        code(
            """students = [
    {"name": "Ada", "scores": [70, 80, 90]},
    {"name": "Bola", "scores": [40, 55, 50]},
    {"name": "Chika", "scores": [88, 92, 79]},
]


def average(scores):
    return sum(scores) / len(scores)


def grade(avg):
    if avg >= 70:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    return "F"


print("JEKACODE STUDENT REPORT")
print("-" * 28)
for student in students:
    avg = average(student["scores"])
    letter = grade(avg)
    print(f"{student['name']:10} average={avg:.1f}  grade={letter}")"""
        ),
        md(
            """## Challenge

1. Add a fourth student.
2. Print `Pass` or `Resit` (resit if grade is F).
3. Find the class average of all students."""
        ),
        code("# Your challenge code here\n"),
        md("Copy the finished script into `projects/YOUR_NAME/week02/`."),
    ],
)

write_text(
    ROOT / "week02-python/student_analyzer.py",
    '''"""Week 2 project — Student Performance Analyzer."""


def average(scores):
    return sum(scores) / len(scores)


def grade(avg):
    if avg >= 70:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    return "F"


def report(students):
    print("JEKACODE STUDENT REPORT")
    print("-" * 32)
    class_total = 0
    for student in students:
        avg = average(student["scores"])
        class_total += avg
        status = "Pass" if grade(avg) != "F" else "Resit"
        print(f"{student['name']:12} {avg:5.1f}  {grade(avg)}  {status}")
    print("-" * 32)
    print(f"Class average: {class_total / len(students):.1f}")


if __name__ == "__main__":
    report(
        [
            {"name": "Ada", "scores": [70, 80, 90]},
            {"name": "Bola", "scores": [40, 55, 50]},
            {"name": "Chika", "scores": [88, 92, 79]},
        ]
    )
''',
)

week_readme(
    "week03-llm-apis",
    3,
    "Large Language Models & AI APIs",
    "An API is a waiter. Your app places an order. Gemini or DeepSeek cooks the reply in the kitchen. You never enter the kitchen.",
    [
        "What an API and an API key are",
        "Why keys live in .env, not in notebooks you share",
        "How to call Gemini and DeepSeek from Python",
        "System prompt vs user prompt",
        "Tokens, length, and costs in simple words",
    ],
    "AI Writing Assistant",
    [
        ("Day 1", "API picture + keys"),
        ("Day 2", "First Gemini call"),
        ("Day 3", "First DeepSeek call"),
        ("Day 4", "System prompts"),
        ("Day 5", "Writing assistant"),
    ],
)

write_nb(
    ROOT / "week03-llm-apis/01_learn.ipynb",
    [
        md(header("WEEK 3", "Talking to Gemini and DeepSeek", "Your Python app sends text. The model sends text back.")),
        md(
            """## The only picture that matters

```
Your Python App
       ↓
  API Request  (https, with a secret key)
       ↓
  AI Model (Gemini or DeepSeek)
       ↓
  AI Response
       ↓
Your Application (print, or later a website)
```

**API** means Application Programming Interface: a doorway with rules.

**API key** is a password for that doorway. If someone steals it, they can spend your quota. Keep it in `.env`.

This course uses **Gemini** (Google AI Studio, free tier) and **DeepSeek**. Not OpenAI. Not OpenRouter."""
        ),
        md(
            """## Two kinds of messages

- **System prompt:** the job description ("You are a WAEC Physics tutor...")
- **User prompt:** what the person typed today

The helper `ask()` in `jekacode/ai.py` can send both."""
        ),
        code(
            """from jekacode.ai import ask

reply = ask(
    prompt="Explain gravity in 4 short sentences for a JSS2 student in Abuja.",
    provider="gemini",
    system="You are a kind Nigerian science teacher. No jargon.",
)
print(reply)"""
        ),
        md("Compare the same question on DeepSeek (skip if you have no key yet):"),
        code(
            """print(ask(
    prompt="Explain gravity in 4 short sentences for a JSS2 student in Abuja.",
    provider="deepseek",
    system="You are a kind Nigerian science teacher. No jargon.",
))"""
        ),
        md(note("Tokens", "Models cut text into small pieces called tokens. Longer prompts cost more and can hit a limit called the context window. For class, keep prompts short and clear.")),
    ],
)

write_nb(
    ROOT / "week03-llm-apis/02_lab.ipynb",
    [
        md(header("WEEK 3 LAB", "AI Writing Assistant", "Generate, summarize, rewrite, improve — four buttons in one notebook.")),
        code(
            '''from jekacode.ai import ask

WRITER = "You are a writing coach for African students and small businesses. Simple English. No fluff."


def generate(topic):
    return ask(f"Write a 120-word explanation of: {topic}", system=WRITER)


def summarize(text):
    return ask(f"Summarize in 5 bullet points:\\n{text}", system=WRITER)


def rewrite(text):
    return ask(f"Rewrite more clearly for a 15-year-old:\\n{text}", system=WRITER)


def improve(text):
    return ask(f"Improve grammar and keep the meaning. Return only the improved text:\\n{text}", system=WRITER)


sample = "AI na computer wey fit help people write, but engineer still need to build the app."
print("GENERATE\\n", generate("What is an API?"))
print("\\nSUMMARIZE\\n", summarize(sample))
print("\\nREWRITE\\n", rewrite(sample))
print("\\nIMPROVE\\n", improve(sample))'''
        ),
        md("Change `sample` and `topic`. Then copy this into `projects/YOUR_NAME/week03/`."),
    ],
)

print("weeks 1-3 done")
