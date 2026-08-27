"""Week 2 project — Student Performance Analyzer.

What we achieve
    Names + scores in → average, letter grade, Pass/Resit, class average.
    Same input always gives the same grade. That is software engineering.

User story
    As a form teacher, I want averages and grades from a list of scores
    so I do not calculate by hand.

How to run
    python week02-python/student_analyzer.py

Why no Gemini here
    Marks must not hallucinate or wobble (inconsistency). Week 3 puts an LLM
    in the *middle* of a similar pipeline for language, not for arithmetic.
"""


def average(scores):
    # sum(...) adds the numbers. len(...) counts how many. Divide = mean.
    return sum(scores) / len(scores)


def grade(avg):
    # Exact rules. Do not use an LLM for this — marks must not hallucinate.
    if avg >= 70:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    return "F"


def report(students):
    print("JEKACODE STUDENT REPORT")
    print("-" * 32)  # a line of dashes for humans
    class_total = 0
    for student in students:  # loop: do the same work for each child
        avg = average(student["scores"])  # dict lookup: the "scores" field
        class_total += avg
        status = "Pass" if grade(avg) != "F" else "Resit"  # one-line if
        # f-string: :12 = pad name, :5.1f = one decimal place
        print(f"{student['name']:12} {avg:5.1f}  {grade(avg)}  {status}")
    print("-" * 32)
    print(f"Class average: {class_total / len(students):.1f}")


if __name__ == "__main__":
    # This block runs only when you type: python student_analyzer.py
    # If another file does `import student_analyzer`, it will not auto-print.
    report(
        [
            {"name": "Ada", "scores": [70, 80, 90]},
            {"name": "Bola", "scores": [40, 55, 50]},
            {"name": "Chika", "scores": [88, 92, 79]},
        ]
    )
