import gspread
from google.oauth2.service_account import Credentials
import time
import os
import sys
from datetime import datetime
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Pennywise")
user1_expenses = SHEET.worksheet("user1")

user1 = user1_expenses.get_all_values()

# Credit for clear screen function: https://www.geeksforgeeks.org/clear-screen-python/
def clear_screen():
    """
    Clears CLI ahead of next code page
    """
    # for windows
    if os.name == 'nt':
        os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

def delayed_clear():
    """
    Clears CLI code after 2 seconds
    """

    time.sleep(2)
    clear_screen()

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def welcome_page():
    """
    Displays welcome text
    """
    print(r'''
    

    $$$$$$$\                                                  $$\                   
    $$  __$$\                                                 \__|                  
    $$ |  $$ |$$$$$$\ $$$$$$$\ $$$$$$$\ $$\   $$\$$\  $$\  $$\$$\ $$$$$$$\ $$$$$$\  
    $$$$$$$  $$  __$$\$$  __$$\$$  __$$\$$ |  $$ $$ | $$ | $$ $$ $$  _____$$  __$$\ 
    $$  ____/$$$$$$$$ $$ |  $$ $$ |  $$ $$ |  $$ $$ | $$ | $$ $$ \$$$$$$\ $$$$$$$$ |
    $$ |     $$   ____$$ |  $$ $$ |  $$ $$ |  $$ $$ | $$ | $$ $$ |\____$$\$$   ____|
    $$ |     \$$$$$$$\$$ |  $$ $$ |  $$ \$$$$$$$ \$$$$$\$$$$  $$ $$$$$$$  \$$$$$$$\ 
    \__|      \_______\__|  \__\__|  \__|\____$$ |\_____\____/\__\_______/ \_______|
                                        $$\   $$ |                                  
                                        \$$$$$$  |                                  
                                        \______/                                   

        
                                Welcome back to Pennywise.

    Find out how much you have spent this month and if you've been savvy enough to 
                                hold off Pennywise...

        ''')
    typingPrint("""
                              Loading, please wait...                           """)
    time.sleep(3)
    clear_screen()

def transaction_date():
    """
    Gets the date of the transaction from the user.
    """
    while True:
        try:
            print(f"Please enter the date of the transaction in the following format(DD-MM-YYYY):")

            global transaction_date 
            transaction_date = input("")

            # Converts user date input into datetime object
            # CCredit for code https://stackoverflow.com/questions/53248537/typeerror-not-supported-between-instances-of-datetime-datetime-and-str
            new_date = datetime.strptime(transaction_date, '%d-%m-%Y')
            
            # initializing date ranges
            min_date = datetime(2024, 1, 1)
            max_date = datetime.now()

            if new_date >= min_date and new_date <= max_date:
                return new_date
            else:
                raise ValueError("The date you've entered is out of range")
        except ValueError:
            print(f'Invalid data.\n Please enter a date which lies between 01-01-2024 and today.')
            return False
        return True

def transaction_category():
    """
    Gets the category of the transaction from the user.
    """

def add_new_expense():
    """
    Gets expense details from user
    """
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)

    print(f"You will now need to enter the date, category, description and transaction amount of the expense you would like to add. Please have this information ready.\n")
    transaction_date()
    transaction_category()
    transaction_description()
    transaction_amount()

def by_date():
    """
    Displays all transactions made since the beginning of the year to the user in table format
    """
    print("""
    --------------------------------------------------------------------------------
                            View Statement By Date
    --------------------------------------------------------------------------------
    """)
    print(tabulate(user1, headers=["Date", "Category", "Description", "Amount"]))
    print("""
    If you want to go back to the Main Menu, please enter mm:""")
    try:
        rtrn_mm = input("")

        if rtrn_mm.lower() == "mm":
            clear_screen()
            main_menu()
        else:
            raise ValueError("Please enter mm to go back to the Main Menu")
    except ValueError as e:
        print("Please enter mm to go back to the Main Menu")

def by_month():
    """
    Displays the amount the user has spent each month since the beginning of the year
    """
    print("""
    --------------------------------------------------------------------------------
                            View Statement By Month
    --------------------------------------------------------------------------------
    """)

def by_category():
    print("""
    --------------------------------------------------------------------------------
                          View Statement By Category
    --------------------------------------------------------------------------------
    """)   

def view_statement():
    """
    Displays a menu giving 3 options of how the user wants to see their statement: by month, by date, by category
    """

    while True:
        print("""
        --------------------------------------------------------------------------------
                                    View Statement
        --------------------------------------------------------------------------------
        """)
        print("How would you like to see your transactions?")
        print("""
        1. By date
        2. By month
        3. By category""")
        print("If you would like to go back to the main menu, please enter MM")

        try:
            statement_choice = input("")

            # Credit for table format https://www.educba.com/python-print-table/
            if statement_choice == "1":
                print("You have chosen option 1: By date.")
                delayed_clear()
                by_date()
                break
            elif statement_choice == "2":
                print("You have chosen option 2: By month.")
                delayed_clear()
                by_month()
                break
            elif statement_choice == "3":
                print("You have chosen option 3: By category.")
                delayed_clear()
                by_category()
                break
            elif statement_choice.lower() == "mm":
                print("You have chosen to go back to the Main Menu")
                delayed_clear()
                main_menu()
                break
            else:
                raise ValueError("Please select one of the options provided")
        except ValueError:
            print(f'Invalid data.\n Please enter option 1, 2, or 3 to see your transactions or enter mm to go back to the Main Menu')
            return False

def view_budget_goals():
    """
    Displays users spending goals for each category
    """
    print("""
    --------------------------------------------------------------------------------
                                    Budget Goals
    --------------------------------------------------------------------------------
    """)
    print("""Your goals for each category are:""")
    
def main_menu():
    """
    Displays the main menu to user, where they can choose how to proceed
    """

    while True:
        print("""
        --------------------------------------------------------------------------------
                                       Main Menu
        --------------------------------------------------------------------------------
        """)
        print("""
        What would you like to do today?
        
        1. Add new expense
        2. View statement
        3. View budget goals
        4. Exit
        """)


        try:
            user_input = input("        Enter your choice here: ")
            #print(user_input)
            print(f"You chose option: {user_input}")
            
            if user_input == "1":
                print(f"Add new expense form is loading, please wait...")
                clear_screen()
                add_new_expense()
                break
            elif user_input == "2":
                print(f"View statement is loading, please wait...")
                clear_screen()
                view_statement()
                break
            elif user_input == "3":
                print(f"View budget goals is loading, please wait...")
                clear_screen()
                view_budget_goals()
                break
            elif user_input == "4":
                print(f"Exiting, please wait...")
                delayed_clear()
                welcome_page()
                break
            else:
                raise ValueError(f'Please select one of the options provided')
                delayed_clearn()
                main_menu()
        except ValueError as e:
            print(f'Invalid data: {e}, please try again.\n')
            delayed_clear()
            main_menu()
            return False
        return True

def pennywise_program():
    welcome_page()
    main_menu()

pennywise_program()
