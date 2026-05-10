# starter.py — Language Poll Analyser
# Project 1 | Easy | 20–25 minutes
#
# Run from this folder:
#   python starter.py
#
# The CSV file is at: ../../week1/favorites.csv

import csv

# ── Step 1: Read the CSV and count languages ──────────────────────────────────
counts = {}

with open("../../part" \
"1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]

        # TODO: Update counts — increment if exists, create if new
        counts[language] = counts.get(language, 0) + 1

# ── Step 2: Sort by popularity (most popular first) ───────────────────────────
sorted_languages = sorted(counts, key=counts.get, reverse=True)

# ── Step 3: Print the report ──────────────────────────────────────────────────
print("=== Language Popularity Report ===")

for rank, language in enumerate(sorted_languages, start=1):
    print(f"{rank}. {language:<8}: {counts[language]} students")

print(f"\nTotal responses: {sum(counts.values())}")
