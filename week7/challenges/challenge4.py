# challenge4.py — SQL Explorer
# Present an interactive menu that runs different SQL queries on favorites.db.
# Requires favorites.db — see week2/README.md for setup instructions.

import sqlite3
import csv

def setup_database(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            language TEXT,
            problem TEXT
        )
    """)

    # Check if already filled
    cursor.execute("SELECT COUNT(*) FROM favorites")
    if cursor.fetchone()[0] > 0:
        return

    # Load CSV
    with open("../part1/favorites.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO favorites (language, problem) VALUES (?, ?)",
                (row["language"], row["problem"])
            )
def main():
    conn = sqlite3.connect("favorites.db")
    cursor = conn.cursor()

    setup_database(cursor)
    conn.commit()

    while True:
        print("\n=== SQL Explorer ===")
        print("1. Count by language")
        print("2. Count by problem")
        print("3. Search by problem name")
        print("4. Top 5 problems overall")
        print("5. Quit")

        choice = input("Choice: ")

        if choice == "1":
            cursor.execute("""
                SELECT language, COUNT(*) 
                FROM favorites
                GROUP BY language
                ORDER BY COUNT(*) DESC
            """)
            for row in cursor.fetchall():
                print(f"{row[0]}: {row[1]}")

        elif choice == "2":
            cursor.execute("""
                SELECT problem, COUNT(*) 
                FROM favorites
                GROUP BY problem
                ORDER BY COUNT(*) DESC
            """)
            for row in cursor.fetchall():
                print(f"{row[0]}: {row[1]}")

        elif choice == "3":
            search = input("Problem name contains: ")

            cursor.execute("""
                SELECT problem, COUNT(*)
                FROM favorites
                WHERE problem LIKE ?
                GROUP BY problem
                ORDER BY COUNT(*) DESC
            """, (f"%{search}%",))  # parameterized query

            results = cursor.fetchall()
            if results:
                for row in results:
                    print(f"{row[0]}: {row[1]}")
            else:
                print("No matches found.")

        elif choice == "4":
            cursor.execute("""
                SELECT problem, COUNT(*)
                FROM favorites
                GROUP BY problem
                ORDER BY COUNT(*) DESC
                LIMIT 5
            """)
            for row in cursor.fetchall():
                print(f"{row[0]}: {row[1]}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")

    conn.close()


if __name__ == "__main__":
    main()
