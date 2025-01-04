# Personal_Expense_Tracker
"A console-based Python application for tracking personal expenses with features like time-based greetings, category-wise expense tracking, and monthly summaries. Built using Python's standard library."

## Features ✨

- **Time-based Greetings** 🌞
  - Personalized greetings based on the time of day (Morning/Afternoon/Evening)

- **Expense Management** 📝
  - Add new expenses with date, category, description, and amount
  - Predefined expense categories (Food, Bills, Transport, Entertainment, Shopping)
  - Custom category option available

- **Expense Viewing Options** 👀
  - View all expenses till date
  - Quick access to last 10 expenses
  - Monthly expense summaries

- **Data Validation** ✅
  - Date format validation (YYYY-MM-DD)
  - No future dates allowed
  - Positive amount validation
  - Category validation

- **Persistent Storage** 💾
  - All expenses are stored in a CSV file
  - Data persists between program runs

## Requirements 📋

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation 🚀

1. Clone the repository
```bash
git clone https://github.com/Abhijeet10219/personal-expense-tracker.git
cd personal-expense-tracker
```

2. Run the program
```bash
python expense_tracker.py
```

## Usage 📖

1. **Starting the Program**
   - Run the program and enter your name
   - You'll receive a time-appropriate greeting

2. **Main Menu Options**
   ```
   Welcome to Personal Expense Tracker 💼
   1. Add Expense ➕
   2. View Expenses 👀
   3. Monthly Summary 📊
   4. Exit ❌
   ```

3. **Adding an Expense**
   - Enter date in YYYY-MM-DD format
   - Select from available categories:
     1. Food 🍔
     2. Bills 💡
     3. Transport 🚗
     4. Entertainment 🎉
     5. Shopping 🛍️
     6. Other 📂
   - Enter description and amount

4. **Viewing Expenses**
   - Choose between:
     - Overall expenses till date
     - Last 10 expenses

5. **Monthly Summary**
   - Enter year and month
   - View category-wise expense breakdown
   - See total expenses for the month

## File Structure 📁

```
personal-expense-tracker/
├── expense_tracker.py    # Main program file
├── expenses.txt         # Data storage file (created automatically)
├── README.md           # Documentation
└── requirements.txt    # Project dependencies
```

## Data Storage 📊

Expenses are stored in `expenses.txt` in txt file with the following structure:
```
Date,Category,Description,Amount
2024-01-04,Food,Lunch,250.00
2024-01-04,Transport,Bus fare,50.00
```

## Error Handling 🛠️

- Invalid date format detection
- Future date prevention
- Invalid amount handling
- Category validation
- File handling error management

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments 🙏

- Built as part of a Python programming project
- Inspired by the need for simple expense tracking
