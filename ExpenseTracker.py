import datetime

# Initialize default categories with empty lists
categories = {
    'shopping': [],
    'groceries': [],
    'gas': [],
    'food': [],
    'utilities': [],
    'rent' : []
}

# Function to add an expense to a specific category with current date
def add_expense(category, amount):
    if category in categories:
        current_date = datetime.datetime.now()
        categories[category].append((amount, current_date))
        print(f'Added ${amount} to {category} category on {current_date.strftime("%Y-%m-%d %H:%M:%S")}.')
    else:
        print(f'Error: Category "{category}" does not exist.')

# Function to calculate and display total expenses for each month
def total_expenses_per_month():
    current_month = None
    total_monthly_expenses = {}

    for category, entries in categories.items():
        for amount, date in entries:
            month_key = (date.year, date.month)
            if month_key not in total_monthly_expenses:
                total_monthly_expenses[month_key] = 0
            total_monthly_expenses[month_key] += amount

    if total_monthly_expenses:
        print("\n===== Total Expenses Per Month =====")
        for year_month, total_amount in sorted(total_monthly_expenses.items()):
            year, month = year_month
            print(f"{year}-{month:02}: ${total_amount}")
    else:
        print("No expenses recorded.")


# Function to calculate and display total expenses for each day
def total_expenses_per_day():
    current_day = None
    total_daily_expenses = {}

    for category, entries in categories.items():
        for amount, date in entries:
            day_key = (date.month, date.day)
            if day_key not in total_daily_expenses:
                total_daily_expenses[day_key] = 0
            total_daily_expenses[day_key] += amount

    if total_daily_expenses:
        print("\n===== Total Expenses Today =====")
        for month_day, total_amount in sorted(total_daily_expenses.items()):
            month, day = month_day
            print(f"{month}-{day:02}: ${total_amount}")
    else:
        print("No expenses recorded.")

    
# Function to create a new category

def create_category(category_name):
    if category_name not in categories:
        categories[category_name] = []
        print(f'Category "{category_name}" created successfully.')
    else:
        print(f'Category "{category_name}" already exists.')

# Main function to run the expense tracker
def main():
    print("Welcome to Expense Tracker!")
    print("Default categories: shopping, groceries, gas, food, utilities")

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. Show Total Expenses Today")
        print("3. Show Total Expenses this Month")
        print("4. Create Category")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            category = input("Enter category for the expense: ").lower()
            if category in categories:
                try:
                    amount = float(input("Enter expense amount: $"))
                    add_expense(category, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.1")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f'Error: Category "{category}" does not exist. Please create it first.')

        elif choice == '2':
            total_expenses_per_day()

        elif choice == '3':
            total_expenses_per_month()

        elif choice == '4':
            category_name = input("Enter name for new category: ").lower()
            create_category(category_name)

        elif choice == '5':
            print("Exiting the Expense Tracker.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()