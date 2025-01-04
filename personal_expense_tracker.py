# -*- coding: utf-8 -*-
"""Personal_Expense_Tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J9KBHosBxMw0qnwYYowXlipmKyErdGU3
"""

from datetime import datetime
import os
from collections import defaultdict
from typing import Dict, List, Optional


class ExpenseTracker:
    def __init__(self, expenses_file: str = "expenses.txt"):
        self.expenses_file = expenses_file
        self.categories = {
            1: "Food",
            2: "Bills",
            3: "Transport",
            4: "Entertainment",
            5: "Shopping",
            6: "Other"
        }
        self._initialize_files()

    def _initialize_files(self) -> None:
        """Initialize expenses file if it doesn't exist."""
        if not os.path.exists(self.expenses_file):
            with open(self.expenses_file, 'w', encoding='utf-8') as f:
                f.write("Date,Category,Description,Amount\n")

    def get_greeting(self, name: str) -> str:
        """Return appropriate greeting based on time of day."""
        hour = datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good Morning 🌞"
        elif 12 <= hour < 17:
            greeting = "Good Afternoon ☀️"
        else:
            greeting = "Good Evening 🌙"
        return f"Hello, {greeting} {name}"

    def validate_date(self, date_str: str) -> Optional[str]:
        """Validate date string format and ensure it's not in the future."""
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date > datetime.now():
                print("\n\033[91m⚠️ Future dates are not allowed! Please enter a valid date.\033[0m")  # Red error message
                return None
            return date_str
        except ValueError:
            print("\n\033[91m⚠️ Invalid date format! Please use YYYY-MM-DD.\033[0m")  # Red error message
            return None

    def add_expense(self, date: str, category: str, description: str, amount: float) -> None:
        """Add an expense to the tracker."""
        with open(self.expenses_file, 'a', encoding='utf-8') as f:
            f.write(f"{date},{category},{description},{amount}\n")

    def get_all_expenses(self) -> List[Dict]:
        """Get all expenses from the file."""
        expenses = []
        with open(self.expenses_file, 'r', encoding='utf-8') as f:
            next(f)  # Skip header
            for line in f:
                if line.strip():
                    date, category, description, amount = line.strip().split(',')
                    expenses.append({
                        'date': date,
                        'category': category,
                        'description': description,
                        'amount': float(amount)
                    })
        return sorted(expenses, key=lambda x: x['date'], reverse=True)

    def get_last_10_expenses(self) -> List[Dict]:
        """Get the last 10 expenses."""
        all_expenses = self.get_all_expenses()
        return all_expenses[:10]

    def get_monthly_summary(self, year: int, month: int) -> Dict[str, float]:
        """Get summary of expenses for a specific month."""
        if year > datetime.now().year or (year == datetime.now().year and month > datetime.now().month):
            return {}

        summary = defaultdict(float)
        for expense in self.get_all_expenses():
            expense_date = datetime.strptime(expense['date'], '%Y-%m-%d')
            if expense_date.year == year and expense_date.month == month:
                summary[expense['category']] += expense['amount']
        return dict(summary)


def display_categories() -> None:
    """Display available expense categories."""
    print("\nAvailable Categories: 🗂️")
    print("1. Food 🍔")
    print("2. Bills 💡")
    print("3. Transport 🚗")
    print("4. Entertainment 🎉")
    print("5. Shopping 🛍️")
    print("6. Other 📂")


def format_currency(amount: float) -> str:
    """Format amount as Indian Rupees."""
    return f"₹{amount:,.2f}"


def main():
    tracker = ExpenseTracker()

    # Get user's name and display greeting
    name = input("Enter your full name: ").strip()
    print(f"\n{tracker.get_greeting(name)}")

    while True:
        print("\nWelcome to Personal Expense Tracker 💼")
        print("1. Add Expense ➕")
        print("2. View Expenses 👀")
        print("3. Monthly Summary 📊")
        print("4. Exit ❌")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            # Add Expense
            while True:
                date = input("\nEnter date (YYYY-MM-DD): ").strip()
                valid_date = tracker.validate_date(date)
                if valid_date:
                    break

            display_categories()
            while True:
                try:
                    category_choice = int(input("\nEnter category number (1-6): "))
                    if 1 <= category_choice <= 6:
                        break
                    print("⚠️ Please enter a number between 1 and 6")
                except ValueError:
                    print("\033[91m⚠️ Please enter a valid number.\033[0m")  # Red error message

            category = tracker.categories[category_choice]
            if category_choice == 6:
                other_category = input("Enter other category: ").strip()
                print(f"Category entered: {other_category}")
                category = other_category

            description = input("Enter description: ").strip()

            while True:
                try:
                    amount = float(input("Enter amount in rupees: ₹"))
                    if amount <= 0:
                        print("\033[91m⚠️ Amount must be positive!\033[0m")  # Red error message
                        continue
                    break
                except ValueError:
                    print("\033[91m⚠️ Please enter a valid amount.\033[0m")  # Red error message

            tracker.add_expense(valid_date, category, description, amount)
            print("\n✅ Expense added successfully!")

        elif choice == '2':
            print("\nView Options: 🧐")
            print("a. Overall Expenses till date 📅")
            print("b. Last 10 Expenses 📝")

            view_choice = input("\nEnter your choice (a/b): ").strip().lower()

            if view_choice == 'a':
                expenses = tracker.get_all_expenses()
                title = "Overall Expenses"
            elif view_choice == 'b':
                expenses = tracker.get_last_10_expenses()
                title = "Last 10 Expenses"
            else:
                print("\033[91m⚠️ Invalid choice!\033[0m")  # Red error message
                continue

            if not expenses:
                print("\nNo expenses recorded yet! 🛑")
                continue

            print(f"\n{title}:")
            print("-" * 70)
            total = 0
            for expense in expenses:
                print(f"Date: {expense['date']}, "
                      f"Category: {expense['category']}, "
                      f"Description: {expense['description']}, "
                      f"Amount: {format_currency(expense['amount'])}")
                total += expense['amount']
            print("-" * 70)
            print(f"Total: {format_currency(total)}")

        elif choice == '3':
            try:
                year = int(input("\nEnter year (YYYY): "))
                month = int(input("Enter month (1-12): "))

                if not (1 <= month <= 12):
                    print("\033[91m⚠️ Month must be between 1 and 12!\033[0m")  # Red error message
                    continue

                current_date = datetime.now()
                if year > current_date.year or (year == current_date.year and month > current_date.month):
                    print("\033[91m⚠️ Cannot generate summary for future months!\033[0m")  # Red error message
                    continue

                summary = tracker.get_monthly_summary(year, month)

                if not summary:
                    print(f"\nNo expenses recorded for {year}-{month:02} 📅")
                    continue

                print(f"\nMonthly Summary for {year}-{month:02} 📊")
                print("-" * 40)
                total = 0
                for category, amount in summary.items():
                    print(f"{category}: {format_currency(amount)}")
                    total += amount
                print("-" * 40)
                print(f"Total Expenses: {format_currency(total)}")

            except ValueError:
                print("\033[91m⚠️ Please enter valid numbers for year and month!\033[0m")  # Red error message

        elif choice == '4':
            print(f"\nGoodbye {name}! Have a great day! 👋")
            break

        else:
            print("\033[91m⚠️ Invalid choice! Please enter a number between 1 and 4.\033[0m")  # Red error message


if __name__ == "__main__":
    main()