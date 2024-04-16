import sqlite3

conn = sqlite3.connect('budget.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY, date TEXT, item TEXT, amount REAL)''')

def add_expenses(num_items):
    """Add multiple expenses to the database based on user input"""
    for i in range(num_items):
        date = input("Enter the date (YYYY-MM-DD) for item {}: ".format(i + 1))
        item = input("Enter the item for item {}: ".format(i + 1))
        amount = float(input("Enter the amount for item {}: ₹".format(i + 1)))
        c.execute("INSERT INTO expenses (date, item, amount) VALUES (?, ?, ?)", (date, item, amount))
    conn.commit()
    print("Expenses added successfully.")

def view_expenses():
    """View all expenses in the database"""
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    for expense in expenses:
        print(expense)

num_items = int(input("How many items do you want to add? "))

add_expenses(num_items)
view_expenses()

conn.close()
