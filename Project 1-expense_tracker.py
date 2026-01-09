print("Welcome to Expense Tracker!")

expenses = []

def show_menu():
    print("\n------- MENU -------")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spendings")
    print("4. Exit")

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = int(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nYour expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Date: {exp['date']}, Category: {exp['category']}, "
              f"Description: {exp['description']}, Amount: ₹{exp['amount']}")

def total_spendings():
    if not expenses:
        print("No expenses to calculate.")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spendings: ₹{total}")

while True:
    show_menu()
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_spendings()
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
