
---

# 📘 Expense Tracker (Python + CSV)

This is a simple Python project that lets you track your daily income and expenses using a CSV file.
There is **no GUI** — everything works in the **terminal**, which makes it easy to read, understand, and modify.

The program stores every transaction (income or expense) in a file named **expense_tracker.csv** and keeps track of your running balance.


---
## 🔧 Features

* Add income
* Add expenses (only if you have enough balance)
* View all transactions
* Delete a transaction
* Automatically updates your balance
* Saves everything in a CSV file
* Easy to use, beginner-friendly code

---

## 📂 How It Works

When you run the program for the first time, it checks if the file
**expense_tracker.csv** exists.
If not, it creates it automatically.

Every time you add income or expense, a new record is added to the file, and the balance is recalculated.

---

## ▶️ How to Run the Project

1. Make sure you have **Python installed**.
2. Save the script as `expense_tracker.py`.
3. Open a terminal/command prompt.
4. Navigate to the folder where your file is saved.
5. Run:

```
python expense_tracker.py
```

You will see a menu like:

```
=== Expense Tracker ===
1. Add Income
2. Add Expense
3. Show Transactions
4. Delete Transaction
5. Show Current Balance
6. Exit
```

Just type the number of the option you want to use.

---

## 📊 Where is the CSV file saved?

The file **expense_tracker.csv** will be created in the **same folder** where your Python script is located.

You can open it using:

* Excel
* Google Sheets
* LibreOffice
* Notepad
* VS Code

---

## 📝 Example CSV Content

```
Date,Type,Description,Amount,Balance
2025-11-24 09:30,Income,Salary,2000,2000
2025-11-25 14:10,Expense,Grocery,200,1800
```

---

## 👍 Why This Project Is Useful

* Helps beginners understand how file handling works in Python
* Shows how to read/write CSV files
* Demonstrates basic menu-driven programs
* Useful for personal finance tracking


## Output Screens
![image 1](<screenshots/Screenshot 2025-11-24 223201.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223247.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223327.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223355.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223440.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223521.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223549.png>)
![image 1](<screenshots/Screenshot 2025-11-24 223619.png>)