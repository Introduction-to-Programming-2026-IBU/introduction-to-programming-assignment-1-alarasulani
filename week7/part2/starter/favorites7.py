# favorites7.py
# Task: Print language counts sorted ALPHABETICALLY (A → Z)
#
# Hint: sorted(counts) returns the keys in alphabetical order.
#       The dictionary itself is NOT changed.

import csv

with open("../../part1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
