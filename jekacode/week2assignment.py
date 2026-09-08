

# 1. Store at least 6 students as a list of dictionaries
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95},
    {"name": "Eva", "score": 49},
    {"name": "Frank", "score": 63}
]

# 2.
def calculate_statistics(students):
    scores = [student["score"] for student in students ]
    average_score = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    return average_score, highest_score, lowest_score

average_score, highest_score, lowest_score = calculate_statistics(students)
print(calculate_statistics(students))
print("Average_score:", average_score)
print("Highest_score:", highest_score)
print("Lowest_score:", lowest_score)
 # 3. Loop through the list and print a pass/fail line for each student (pass = 50+)
print("--- Student Results ---")
for student in students:
    if student["score"] >= 50:
        print(student["name"], student["score"], "PASS")
    else:
        print(student["name"], student["score"], "FAIL")


    prompt = f"""
The class average is {average_score},
The highest score is {highest_score},
The lowest score is {lowest_score},
Write a one paragraph summary of the class performance in plain english.
"""


