# challenge1.py — Frequency Filter
# Read favorites.csv, ask for a minimum vote count, print filtered results.
# No starter hints — build this from scratch using what you learned in week1 and week2.

import csv

def main():
    # Ask user for minimum votes
    try:
        min_votes = int(input("Minimum votes to display: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    counts = {}

    # Read CSV file
    with open("../part1/favorites.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            language = row["language"]
            counts[language] = counts.get(language, 0) + 1

    # Filter and sort results
    filtered = [
        (lang, count) for lang, count in counts.items()
        if count >= min_votes
    ]

    # Sort by count descending
    filtered.sort(key=lambda x: x[1], reverse=True)

    # Print results
    for lang, count in filtered:
        print(f"{lang}: {count}")

if __name__ == "__main__":
    main()