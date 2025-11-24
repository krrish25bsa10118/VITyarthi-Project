import csv
import os
from datetime import datetime

FILE_NAME = "expense_tracker.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Type", "Description", "Amount", "Balance"])


def read_transactions():
    if not os.path.exists(FILE_NAME):
        return []

    transactions = []
    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)
    return transactions


def save_transactions(transactions):
    balance = 0
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Type", "Description", "Amount", "Balance"])

        for t in transactions:
            amt = float(t["Amount"])
            balance += amt if t["Type"] == "Income" else -amt
            writer.writerow([t["Date"], t["Type"], t["Description"], t["Amount"], balance])



def get_balance():
    transactions = read_transactions()
    if transactions:
        return float(transactions[-1]["Balance"])
    return 0.0


def add_income():
    desc = input("Enter description: ").strip()
    try:
        amt = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    transactions = read_transactions()
    transactions.append({
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Type": "Income",
        "Description": desc,
        "Amount": amt,
        "Balance": 0   
    })
    save_transactions(transactions)

    print("Income added. New balance:", get_balance())



def add_expense():
    desc = input("Enter description: ").strip()

    try:
        amt = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if amt > get_balance():
        print("Error: Not enough balance.")
        return

    transactions = read_transactions()
    transactions.append({
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Type": "Expense",
        "Description": desc,
        "Amount": amt,
        "Balance": 0
    })
    save_transactions(transactions)

    print("Expense recorded. New balance:", get_balance())


def show_transactions():
    transactions = read_transactions()
    if not transactions:
        print("No records found.")
        return

    print("\n--- Transaction History ---")
    for i, t in enumerate(transactions):
        print(f"{i}. {t['Date']} | {t['Type']} | {t['Description']} | ₹{t['Amount']} | Bal: ₹{t['Balance']}")
    print("---------------------------\n")



def delete_transaction():
    show_transactions()
    try:
        choice = int(input("Enter transaction number to delete: "))
    except ValueError:
        print("Invalid choice.")
        return

    transactions = read_transactions()

    if choice < 0 or choice >= len(transactions):
        print("Invalid index.")
        return

    del transactions[choice]
    save_transactions(transactions)

    print("Transaction deleted.")



def main():
    initialize_file()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Transactions")
        print("4. Delete Transaction")
        print("5. Show Current Balance")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_transactions()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            print("Current Balance:", get_balance())
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
