# favorites3.py
# Task: Same as favorites2 but print directly without a named variable.
#       One-liner inside the loop: print(row["language"])
#
# This version is more concise. favorites2 is more readable.
# Neither is "wrong" — it depends on the situation.

import csv

with open("../favorites.csv", "r") as file:
    for row in csv.DictReader(file):
        print(row["language"])