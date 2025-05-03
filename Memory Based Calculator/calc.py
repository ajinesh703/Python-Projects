import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("calculator_history.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT NOT NULL,
            result REAL NOT NULL
        )"""
    )
    conn.commit()
    conn.close()

# Add calculation to the database
def add_to_history(operation, result):
    conn = sqlite3.connect("calculator_history.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (operation, result) VALUES (?, ?)", (operation, result))
    conn.commit()
    conn.close()

# View calculation history
def view_history():
    conn = sqlite3.connect("calculator_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Perform calculations
def calculate():
    setup_database()
    print("Welcome to the Calculator with History!")
    while True:
        print("\nOptions:")
        print("1. Perform a calculation")
        print("2. View history")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                operation = input("Enter the operation (e.g., 5 + 3): ")
                result = eval(operation)
                print(f"Result: {result}")
                add_to_history(operation, result)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            history = view_history()
            if history:
                print("\nCalculation History:")
                for record in history:
                    print(f"{record[0]}. {record[1]} = {record[2]}")
            else:
                print("No history found.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculate()
