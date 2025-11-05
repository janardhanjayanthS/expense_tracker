import csv

from helpers import Expense

def append_expense(expense: Expense):
    """
    append values to csv file: expenses.csv
    """
    with open('expenses.csv', 'a') as csv_file:
        headers = ['description', 'amount', 'category', 'date', 'is_recurring']
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writerow({
            'description': expense.description,
            'amount': expense.amount,
            'category': expense.category,
            'date': expense.date,
            'is_recurring': expense.is_recurring
        })
    print('Successfully appended to csv file')

