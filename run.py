import gspread
from google.oauth2.service_account import Credentials
import time
import os
import sys


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Pennywise")
jan_expenses = SHEET.worksheet("January")
feb__expenses = SHEET.worksheet("February")
mar_expenses = SHEET.worksheet("March")

jan_data = jan_expenses.get_all_values()

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
    
    $$$$$$$\                                                        $$\                     
    $$  __$$\                                                       \__|                    
    $$ |  $$ | $$$$$$\  $$$$$$$\  $$$$$$$\  $$\   $$\ $$\  $$\  $$\ $$\  $$$$$$$\  $$$$$$\  
    $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$ | $$ | $$ |$$ |$$  _____|$$  __$$\ 
    $$  ____/ $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |\$$$$$$\  $$$$$$$$ |
    $$ |      $$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ | \____$$\ $$   ____|
    $$ |      \$$$$$$$\ $$ |  $$ |$$ |  $$ |\$$$$$$$ |\$$$$$\$$$$  |$$ |$$$$$$$  |\$$$$$$$\ 
    \__|       \_______|\__|  \__|\__|  \__| \____$$ | \_____\____/ \__|\_______/  \_______|
                                            $$\   $$ |                                      
                                            \$$$$$$  |                                      
                                            \______/                                       

    
                                    Welcome back to Pennywise.

Find out how much you have spent this month and if you've been savvy enough to hold off Pennywise...

    ''')
    typingPrint("""
                                      Loading, please wait...                                       """)
    time.sleep(3)
    clear_screen()
def expense_transaction_date():
    """
    Gets the date of the transaction from the user.
    """
    transaction_date = input(r"""
    Please enter the date of the transaction in the following format(YYYY/MM/DD):
    >""")

def add_new_expense():
    """
    Gets expense details from user
    """
    expense_transaction_date()



def view_statement():
    """
    Displays a menu giving 3 options of how the user wants to see their statement: by month, by date, by category
    """


def view_budget_goals():
    """
    Displays users spending goals for each category
    """
    
def main_menu():
    """
    Displays the main menu to user, where they can choose how to proceed
    """

    while True:
        print("""
        What would you like to do today?
        
        1. Add new expense
        2. View statement
        3. View budget goals
        4. Exit
        """)


        try:
            user_input = input("Enter your choice here: ")
            print(user_input)
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




def main():
    welcome_page()
    main_menu()

main()
