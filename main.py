from datetime import datetime as dt

from csv_utility import append_expense
from helpers import Expense
from prompts import *



def add_expense():
    """
    add a new expense to csv file
    """
    print('New expense details')
    description: str = input('Enter description: ')
    amount: int | float = prompt_amount()
    category: str = promt_category()
    date: str = prompt_date()
    is_recurring: bool = prompt_recurrance()
    print('Expense information')
    print(description)
    print(amount)
    print(category)
    print(date)
    print(is_recurring)
    append_expense(
        Expense(
            description=description,
            amount=amount,
            category=category,
            date=date,
            is_recurring=is_recurring
    ))

    

    
    

if __name__ == '__main__':
    
    while True:
        print('Expense Tracker: ')
        print('1. Add Expense')


        choice = int(input('Enter Your choice from 1 to : '))

        if choice == 1:
            add_expense()
        