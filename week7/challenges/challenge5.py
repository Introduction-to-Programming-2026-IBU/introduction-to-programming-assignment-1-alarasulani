# challenge5.py — Data Cleaner
# Read a messy CSV, detect problems, write a cleaned version, print a report.
# Create your own messy_data.csv with intentional errors to test against.

import csv

VALID_LANGUAGES = {"Python", "C", "Scratch"}

def main():
    seen_ids = set()

    stats = {
        "total": 0,
        "blank": 0,
        "missing": 0,
        "duplicates": 0,
        "invalid_score": 0,
        "unknown_language": 0,
        "cleaned": 0
    }

    cleaned_rows = []

    with open("messy_data.csv", newline="") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            stats["total"] += 1

            # Check blank row
            if not any(row.values()):
                stats["blank"] += 1
                continue

            student_id = row.get("student_id")
            language = row.get("language")
            score = row.get("score")

            # Missing data
            if not student_id or not language or not score:
                stats["missing"] += 1
                continue

            # Duplicate ID
            if student_id in seen_ids:
                stats["duplicates"] += 1
                continue
            seen_ids.add(student_id)

            # Validate score
            try:
                score = int(score)
                if score < 1 or score > 5:
                    stats["invalid_score"] += 1
                    continue
            except ValueError:
                stats["invalid_score"] += 1
                continue

            # Validate language
            if language not in VALID_LANGUAGES:
                stats["unknown_language"] += 1
                continue

            # If all checks pass → keep row
            cleaned_rows.append({
                "student_id": student_id,
                "language": language,
                "score": score
            })
            stats["cleaned"] += 1

    # Write cleaned data
    with open("cleaned_data.csv", "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["student_id", "language", "score"])
        writer.writeheader()
        writer.writerows(cleaned_rows)

    # Print report
    print("\n=== Cleaning Report ===")
    print(f"Total rows: {stats['total']}")
    print(f"Removed blank rows: {stats['blank']}")
    print(f"Removed missing fields: {stats['missing']}")
    print(f"Removed duplicates: {stats['duplicates']}")
    print(f"Removed invalid scores: {stats['invalid_score']}")
    print(f"Removed unknown languages: {stats['unknown_language']}")
    print(f"Clean rows written: {stats['cleaned']}")
    print("\nSaved to cleaned_data.csv")


if __name__ == "__main__":
    main()