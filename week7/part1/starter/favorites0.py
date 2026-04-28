# favorites0.py
# Task: Print every student's favourite language using csv.reader
#
# Expected output (first few lines):
#   Python
#   C
#   Python
#   ...
#
# Hint: csv.reader returns each row as a LIST.
#       The language column is at index 1.
#       Don't forget to skip the header row with next()

import csv

import csv

# Open the file
with open("../favorites.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row[1])