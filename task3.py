import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
HEADERS = ["Date", "Category", "Description", "Amount"]


def initialize_file():
    """Creates the CSV file with headers if it doesn't exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def add_expense():
    """Prompts the user for expense details and appends them to the CSV file."""
    print("\n--- ➕ Add New Expense ---")

    # Category
    category = input("Enter category (e.g., Food, Transport, Bills): ").strip().capitalize()
    if not category:
        category = "Uncategorized"

    # Description
    description = input("Enter description (brief note): ").strip()

    # Amount (Input validation)
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount > 0:
                break
            print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Date defaults to today's date
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Save to file
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category, description, f"{amount:.2f}"])

    print(f"✅ Saved: ${amount:.2f} for '{description}' under [{category}].")


def load_expenses():
    """Reads and returns all expenses from the CSV file."""
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Amount"] = float(row["Amount"])
            expenses.append(row)
    return expenses


def view_expenses(filter_category=None):
    """Displays expenses (all or filtered) and shows the total."""
    expenses = load_expenses()

    if not expenses:
        print("\nℹ️ No expenses recorded yet.")
        return

    # Filter if requested
    if filter_category:
        expenses = [exp for exp in expenses if exp["Category"].lower() == filter_category.lower()]
        title = f"\n--- 📋 Expenses for Category: [{filter_category.capitalize()}] ---"
    else:
        title = "\n--- 📋 All Recorded Expenses ---"

    if not expenses:
        print(f"\nℹ️ No expenses found under category '{filter_category}'.")
        return

    # Print Table
    print(title)
    print(f"{'Date':<12} | {'Category':<15} | {'Description':<25} | {'Amount':>10}")
    print("-" * 70)

    total = 0.0
    for exp in expenses:
        print(f"{exp['Date']:<12} | {exp['Category']:<15} | {exp['Description']:<25} | ${exp['Amount']:>9.2f}")
        total += exp["Amount"]

    print("-" * 70)
    print(f"{'RUNNING TOTAL:':<56} ${total:>9.2f}\n")


def filter_by_category():
    """Prompts user for a category and displays matching expenses."""
    expenses = load_expenses()
    if not expenses:
        print("\nℹ️ No expenses recorded yet.")
        return

    # Get unique categories for a friendly suggestion menu
    categories = sorted({exp["Category"] for exp in expenses})
    print(f"\nAvailable categories: {', '.join(categories)}")
    category = input("Enter category name to filter by: ").strip()

    if category:
        view_expenses(filter_category=category)


def main():
    initialize_file()

    while True:
        print("\n=== 💰 Simple Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses & Running Total")
        print("3. Filter Expenses by Category")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            print("Goodbye! Happy tracking.")
            break
        else:
            print("Invalid choice. Please pick between 1 and 4.")


if __name__ == "__main__":
    main()