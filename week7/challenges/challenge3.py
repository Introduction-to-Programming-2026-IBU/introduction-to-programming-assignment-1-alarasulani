# challenge3.py — CSV Writer
# Read favorites.csv, count votes per language, write results to language_summary.csv.

import csv

def main():
    counts = {}

    # Read CSV and count votes
    with open("../part1/favorites.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            language = row["language"]
            counts[language] = counts.get(language, 0) + 1

    # Total votes
    total = sum(counts.values())

    # Write to new CSV file
    with open("language_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["language", "votes", "percentage"])

        # Write rows
        for language, votes in counts.items():
            percentage = (votes / total) * 100
            writer.writerow([language, votes, f"{percentage:.2f}"])

    print("Saved to language_summary.csv")

if __name__ == "__main__":
    main()