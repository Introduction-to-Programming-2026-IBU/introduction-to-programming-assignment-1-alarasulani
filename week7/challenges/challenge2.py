# challenge2.py — Two-Column Report
# Read favorites.csv, find the most common problem per language, print a table.

import csv

def main():
    data = {}

    # Read CSV file
    with open("../part1/favorites.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            language = row["language"]
            problem = row["problem"]

            # Create nested dictionary if needed
            if language not in data:
                data[language] = {}

            # Count problems per language
            data[language][problem] = data[language].get(problem, 0) + 1

    # Print header
    print("Language   | Most Common Problem")
    print("-----------+--------------------")

    # Process each language
    for language in sorted(data.keys()):
        problems = data[language]

        # Find most common problem
        most_common = max(problems, key=problems.get)

        print(f"{language:<10} | {most_common}")

if __name__ == "__main__":
    main()