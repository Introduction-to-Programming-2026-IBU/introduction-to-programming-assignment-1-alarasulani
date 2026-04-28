# starter.py — Survey Dashboard
# Project 4 | Hard | 60–90 minutes (split across 2 sessions)
#
# Run from this folder:
#   python starter.py
#
# Split the work across four roles — see README.md for the role breakdown.

import csv
import sqlite3

# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 — CREATE THE DATABASE AND TABLE
# ══════════════════════════════════════════════════════════════════════════════

conn = sqlite3.connect("survey.db")
db   = conn.cursor()

db.execute("""
CREATE TABLE IF NOT EXISTS responses (
    student_id TEXT,
    faculty TEXT,
    year INTEGER,
    satisfaction INTEGER,
    favourite_tool TEXT,
    comments TEXT
)
""")

# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 — READ ALL THREE CSV FILES AND INSERT ROWS
# ══════════════════════════════════════════════════════════════════════════════

csv_files = [
    "faculty_science.csv",
    "faculty_arts.csv",
    "faculty_business.csv",
]

for filename in csv_files:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            db.execute(""" INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?)""", (
                row["student_id"],
                row["faculty"],
                int(row["year"]),
                int(row["satisfaction"]),
                row["favourite_tool"],
                row["comments"]
            ))

conn.commit()
print("Database loaded successfully.\n")

# ══════════════════════════════════════════════════════════════════════════════
# STEP 3 — DASHBOARD QUERIES
# ══════════════════════════════════════════════════════════════════════════════

print("=" * 30)
print("  UNIVERSITY SURVEY DASHBOARD")
print("=" * 30)

# ── Query 1: Total responses by faculty (Coder B) ────────────────────────────
print("\n1. Total Responses by Faculty")

rows = db.execute("""
    SELECT faculty, COUNT(*)
    FROM responses
    GROUP BY faculty
    ORDER BY faculty
""").fetchall()

total = 0
for faculty, count in rows:
    print(f"    {faculty:<10}: {count}")
    total += count

print(f"    {'TOTAL':<10}: {total}")


# ── Query 2: Average satisfaction by year (Coder B) ──────────────────────────
print("\n2. Average Satisfaction by Year of Study")

rows = db.execute("""
    SELECT year, ROUND(AVG(satisfaction), 1)
    FROM responses
    GROUP BY year
    ORDER BY year
""").fetchall()

for year, avg in rows:
    print(f"    Year {year} : {avg} / 5")

# ── Query 3: Favourite tool popularity (Coder B) ─────────────────────────────
print("\n3. Favourite Tool Popularity")

rows = db.execute("""
    SELECT favourite_tool, COUNT(*) 
    FROM responses
    GROUP BY favourite_tool
    ORDER BY COUNT(*) DESC
""").fetchall()
                  
for tool, count in rows:
    print(f"   {tool:<8}: {count:>2} students")

# ── Query 4: Faculty comparison table (Coder C) ──────────────────────────────
print("\n4. Faculty Comparison")
print(f"   {'Faculty':<12} | {'Avg Satisfaction':<18} | Most Popular Tool")
print("   " + "-" * 50)

# For each faculty, find average satisfaction and most popular tool
faculties = ["Arts", "Business", "Science"]

for faculty in faculties:
    avg_row = db.execute("""
        SELECT ROUND(AVG(satisfaction), 1)
        FROM responses
        WHERE faculty = ?
    """, (faculty,)).fetchone()

    tool_row = db.execute("""
        SELECT favourite_tool, COUNT(*) as n
        FROM responses
        WHERE faculty = ?
        GROUP BY favourite_tool
        ORDER BY n DESC
        LIMIT 1
    """, (faculty,)).fetchone()

    avg = avg_row[0]
    tool = tool_row[0] if tool_row else "N/A"

    print(f"   {faculty:<10} | {avg:<18} | {tool}")

# ── Query 5: Interactive filter (Coder C) ────────────────────────────────────
print()

try:
    min_score = int(input("Enter minimum satisfaction score (1-5): "))
except ValueError:
    print("Invalid input. Defaulting to 4.")
    min_score = 4

rows = db.execute("""
    SELECT student_id, faculty, year, favourite_tool
    FROM responses
    WHERE satisfaction >= ?
    ORDER BY faculty, year
""", (min_score,)).fetchall()

print(f"\nStudents with satisfaction >= {min_score}:")

if not rows:
    print("  No results found.")

for student_id, faculty, year, tool in rows:
    print(f"  {student_id} | {faculty:<8} | Year {year} | {tool}")

# ══════════════════════════════════════════════════════════════════════════════
# CLEANUP
# ══════════════════════════════════════════════════════════════════════════════
conn.close()
