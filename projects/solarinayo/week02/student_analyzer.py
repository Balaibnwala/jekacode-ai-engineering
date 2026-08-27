"""Sample submission — solarinayo, Week 2.

Classroom original: week02-python/student_analyzer.py
This copy adds a fourth student (Tunde) as the homework stretch.

How to run (course root):
    python projects/solarinayo/week02/student_analyzer.py

No API keys. Marks must never go through Gemini.
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
    print("JEKACODE STUDENT REPORT  ·  solarinayo sample")
    print("-" * 40)
    class_total = 0
    for student in students:
        avg = average(student["scores"])
        class_total += avg
        status = "Pass" if grade(avg) != "F" else "Resit"
        print(f"{student['name']:12} {avg:5.1f}  {grade(avg)}  {status}")
    print("-" * 40)
    print(f"Class average: {class_total / len(students):.1f}")


if __name__ == "__main__":
    report(
        [
            {"name": "Ada", "scores": [70, 80, 90]},
            {"name": "Bola", "scores": [40, 55, 50]},
            {"name": "Chika", "scores": [88, 92, 79]},
            {"name": "Tunde", "scores": [51, 49, 60]},  # homework: fourth student
        ]
    )
