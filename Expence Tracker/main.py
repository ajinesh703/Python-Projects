import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (food, travel, etc): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    note = input("Enter note (optional): ").strip()

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added.")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.")
        return
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))

def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded.")
        return
    total = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f"Total expenses: {total}")

def main():
    init_file()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View Total\n4. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
