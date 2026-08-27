# Week 2 — Student Performance Analyzer (sample)

**Student:** solarinayo

## What I built

A Python script that takes names + scores, prints average, letter grade, Pass/Resit, and class average. **No LLM.** Same input always gives the same grade.

## Who it helps

A form teacher who is tired of calculating averages by hand.

## How to run it

From the **course root**:

```bash
python projects/solarinayo/week02/student_analyzer.py
```

## What was hard

Remembering that list index `0` is the first score, and that `grade()` must not call Gemini.

## What I would improve

Read scores from a CSV file in a later week. Still no AI for the mark.

## User story

As a form teacher, I want averages and grades from a list of scores so I do not calculate by hand.
