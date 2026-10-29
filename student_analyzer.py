"""Student Performance Analyzer

A beginner-friendly command-line program using Python's standard library.
Run: python student_analyzer.py
"""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sample_data.csv")


def load_students():
    students = []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            marks = [float(row[f"subject{i}"]) for i in range(1, 4)]
            students.append({"name": row["name"], "marks": marks})
    return students


def grade_for(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "Needs Improvement"


def main():
    students = load_students()
    if not students:
        print("No student records found.")
        return

    print("\nSTUDENT PERFORMANCE REPORT")
    print("-" * 64)
    print(f"{'Name':<18}{'Total':>8}{'Percent':>12}{'Grade':>20}")
    print("-" * 64)

    summaries = []
    for student in students:
        total = sum(student["marks"])
        percentage = total / (len(student["marks"]) * 100) * 100
        grade = grade_for(percentage)
        summaries.append((student["name"], total, percentage, grade))
        print(f"{student['name']:<18}{total:>8.1f}{percentage:>11.1f}%{grade:>20}")

    class_average = sum(item[2] for item in summaries) / len(summaries)
    top_student = max(summaries, key=lambda item: item[2])

    print("-" * 64)
    print(f"Class average percentage: {class_average:.1f}%")
    print(f"Top performer: {top_student[0]} ({top_student[2]:.1f}%)")
    print("\nNote: Sample data is fictional. Grade thresholds are examples.")


if __name__ == "__main__":
    main()
