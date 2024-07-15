import os
import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, filename='expenses.txt'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        expenses = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                expenses = [line.strip().split(',') for line in file.readlines()]
        return expenses

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            for expense in self.expenses:
                file.write(','.join(expense) + '\n')

    def add_expense(self, category, amount):
        date = datetime.date.today().strftime("%Y-%m-%d")
        expense = [date, category, str(amount)]
        self.expenses.append(expense)
        self.save_expenses()
        print(f'Expense added:\nDate: {date}\nCategory: {category}\nAmount: RS{amount}')

    def view_expenses(self):
        if not self.expenses:
            print('No expenses recorded.')
        else:
            print("{:<10} {:<12} {:<20} {:<10}".format("Index", "Date", "Category", "Amount"))
            for index, expense in enumerate(self.expenses, start=1):
                print("{:<10} {:<12} {:<20} {:<10}".format(index, expense[0], expense[1], f"RS{expense[2]}"))

    def calculate_total_expenses(self):
        total_expenses = sum(float(expense[2]) for expense in self.expenses)
        return total_expenses

    def expense_categories_summary(self):
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense[1]] += float(expense[2])

        print("Expense Categories Summary:")
        for category, total in category_totals.items():
            print(f"{category}: RS{total}")

    def monthly_expense_summary(self):
        current_month = datetime.date.today().strftime("%Y-%m")
        monthly_expenses = [expense for expense in self.expenses if expense[0].startswith(current_month)]

        if not monthly_expenses:
            print(f'No expenses recorded for the month {current_month}.')
        else:
            print("{:<10} {:<12} {:<20} {:<10}".format("Index", "Date", "Category", "Amount"))
            for index, expense in enumerate(monthly_expenses, start=1):
                print("{:<10} {:<12} {:<20} {:<10}".format(index, expense[0], expense[1], f"RS{expense[2]}"))

    def delete_expense(self, index):
        if 1 <= index <= len(self.expenses):
            deleted_expense = self.expenses.pop(index - 1)
            self.save_expenses()
            print(f'Expense deleted:\nDate: {deleted_expense[0]}\nCategory: {deleted_expense[1]}\nAmount: RS{deleted_expense[2]}')
        else:
            print('Invalid index. Please enter a valid index.')

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print('\n1. Add Expense\n2. View Expenses\n3. Calculate Total Expenses\n4. Expense Categories Summary\n5. Monthly Expense Summary\n6. Delete Expense\n7. Quit')
        choice = input('Enter your choice (1/2/3/4/5/6/7): ')

        if choice == '1':
            category = input('Enter the expense category: ')
            amount = float(input('Enter the expense amount: '))
            expense_tracker.add_expense(category, amount)

        elif choice == '2':

            expense_tracker.view_expenses()
        elif choice == '3':
            total_expenses = expense_tracker.calculate_total_expenses()
            print(f'Total Expenses: RS{total_expenses}')
        elif choice == '4':
            expense_tracker.expense_categories_summary()
        elif choice == '5':
            expense_tracker.monthly_expense_summary()
        elif choice == '6':
            index = int(input('Enter the index of the expense to delete: '))
            expense_tracker.delete_expense(index)
        elif choice == '7':
            print('Saving expenses and exiting the Expense Tracker. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
