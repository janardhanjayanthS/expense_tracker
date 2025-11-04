import csv


def append_expense(description: str, amount: int | float, category: str, date: str, is_recurring: bool):
    """
    append values to csv file: expenses.csv
    """
    with open('expenses.csv', 'a') as csv_file:
        headers = ['description', 'amount', 'category', 'date', 'is_recurring']
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writerow({
            'description': description,
            'amount': amount,
            'category': category,
            'date': date,
            'is_recurring': is_recurring
        })
    print('Successfully appended to csv file')

