# favorites9.py
# Task: Count languages using SQL instead of a Python dictionary.
#
# Before running this file, import the CSV into SQLite:
#   sqlite3 favorites.db
#   .mode csv
#   .import ../week1/favorites.csv favorites
#   .quit
#
# The SQL query replaces the entire counting loop from favorites5–8.
# One query does what 10+ lines of Python did.
#
# Expected output:
#   Python 196
#   C 40
#   Scratch 28


import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect("favorites.db")
    cursor = conn.cursor()

    # SQL does all the counting work here
    cursor.execute("""
        SELECT language, COUNT(*) AS count
        FROM favorites
        GROUP BY language
        ORDER BY count DESC;
    """)

    # Print results in the required format
    for language, count in cursor.fetchall():
        print(f"{language} {count}")

    conn.close()

if __name__ == "__main__":
    main()