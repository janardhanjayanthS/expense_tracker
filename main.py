from datetime import datetime as dt




def add_expense():
    """
    add a new expense to csv file
    """
    print('New expense details')
    description: str = input('Enter description: ')
    amount: int | float = prompt_amount()
    category: str = promt_category()
    
    
def prompt_amount() -> int | float:
    """
    Prompt for amount
    """
    while True:
        try:
            amount: int | float = float(input('Enter amount'))
            if amount > 0:
                return amount
            else:
                print('value of amount should not be 0 or negative')
        except ValueError:
            print('Enter a valid integer/float value for amount')


def promt_category() -> str:
    """
    prompts for category
    """
    category_dict = {
        1: 'food',
        2: 'transport',
        3: 'entertainment',
        4: 'utilities',
        5: 'other'
    }
    for i, value in category_dict.items():
        print(f'{i}. {value}')

    while True:
        try:
            choice: int = int(input('Enter catergory 1 - 5'))
            if choice in category_dict.keys():
                return category_dict[choice]
            else:
                print('Enter a valid number from 1 to 5')
        except ValueError:
            print('Enter a valid number from 1 to 5')

if __name__ == '__main__':
    
    while True:
        print('Expense Tracker: ')
        print('1. Add Expense')

        choice = int(input('Enter Your choice from 1 to : '))

        if choice == 1:
            add_expense()
        