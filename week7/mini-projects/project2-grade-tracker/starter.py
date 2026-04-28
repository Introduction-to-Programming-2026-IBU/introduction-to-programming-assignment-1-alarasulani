# starter.py — Grade Tracker
# Project 2 | Easy | 25–30 minutes
#
# Run from this folder:
#   python starter.py

import csv

# ── Step 1: Set up storage variables ─────────────────────────────────────────
scores = []          # we'll collect all scores here for the average
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# We track highest and lowest as dicts so we can store the name too
highest = {"name": "", "score": -1}
lowest  = {"name": "", "score": 101}   # Why 101? Discuss with your pair.

# ── Step 2: Read the CSV ──────────────────────────────────────────────────────
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name  = row["name"]
        score = int(row["score"])   # IMPORTANT: CSV values are strings — must convert

        scores.append(score)
        
        if score > highest["score"]:
            highest["name"] = name
            highest["score"] = score
            
        if score < lowest["score"]:
            lowest["name"] = name
            lowest["score"] = score

        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"
        
        grade_counts[letter] += 1
        
# ── Step 3: Calculate the average ────────────────────────────────────────────
average = round(sum(scores) / len(scores), 1)

# ── Step 4: Print the report ──────────────────────────────────────────────────
print("=== Quiz Grade Summary ===")

print(f"Students assessed : {len(scores)}")
print(f"Average score     : {average}")
print(f"Highest score     : {highest['score']}  ({highest['name']})")
print(f"Lowest score      : {lowest['score']}  ({lowest['name']})")

print("\nGrade Distribution:")

print(f"  A (90-100) : {grade_counts['A']} students")
print(f"  B (80-89)  : {grade_counts['B']} students")
print(f"  C (70-79)  : {grade_counts['C']} students")
print(f"  D (60-69)  : {grade_counts['D']} students")
print(f"  F ( 0-59)  : {grade_counts['F']} students")