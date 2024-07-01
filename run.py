import gspread
from google.oauth2.service_account import Credentials
import time
import os
import sys
from datetime import datetime
from tabulate import tabulate
from colorama import Back, Fore, Style


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
#print(user1)

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

    time.sleep(10)
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
    print(Fore.GREEN + r'''
    

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

    ''' + Style.RESET_ALL + '''    
                                Welcome back to Pennywise.

    Find out how much you have spent this month and if you've been savvy enough to 
                                hold off Pennywise...

        ''')
    print(Fore.BLUE)
    typingPrint("""
                                Loading, please wait...                           """)
    print(Style.RESET_ALL)
    time.sleep(1)
    clear_screen()

def get_transaction_date():
    """
    Gets the date of the transaction from the user.
    """
    while True:
        try:
            print()
            print(f"Please enter the date of the transaction in the following format(DD-MM-YYYY):")
            global expense_input_date
            print()
            expense_input_date = input(">")

            # Converts user date input into datetime object
            # CCredit for code https://stackoverflow.com/questions/53248537/typeerror-not-supported-between-instances-of-datetime-datetime-and-str
            new_date = datetime.strptime(expense_input_date, '%d-%m-%Y')
            
            # initializing date ranges
            min_date = datetime(2024, 1, 1)
            max_date = datetime.now()

            if new_date >= min_date and new_date <= max_date:
                return new_date
            else:
                raise ValueError(Fore.RED + "The date you've entered is out of range" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Invalid data. Please enter a date which lies between 01-01-2024 and today.' + Style.RESET_ALL)
            get_transaction_date()
            return False
        return True

def get_transaction_category(user1):
    """
    Gets the category of the transaction from the user.
    """
    print()
    print(f"The current category choices are: ")
    print()
    current_choices = [row[1] for row in user1]
    one_cat_list = []

    # Credit for code https://www.dataquest.io/blog/how-to-remove-duplicates-from-a-python-list/
    for category in current_choices:
        if category not in one_cat_list:
            one_cat_list.append(category)
            
    sorted_list = sorted(one_cat_list)
    for i in sorted_list:
        print(i)

    while True:
        print()
        print('Please enter the category of the transaction:')
        print()
        user_input = input(">")
        expense_input_category = user_input.capitalize()
    
        try:
            if expense_input_category.isalpha():
                return expense_input_category
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}. The category needs to include letters only." + Style.RESET_ALL)
        
def get_transaction_description():
    """
    Gets the description of the transaction from the user.
    """

    # Credit for code to only accept letters: https://www.shiksha.com/online-courses/articles/isalpha-method-in-python/#:~:text=The%20isalpha()%20method%20can,entered%20only%20contains%20alphabetic%20characters.
    while True:
        try:
            print('Please enter the description of the transaction, e.g. Gym')
            tran_descr = input('>')

            if len(tran_descr) > 3 and len(tran_descr) < 30 and tran_descr.isalpha():
                return tran_descr
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"Invalid input: The description needs to be between 3 and 30 letters long." + Style.RESET_ALL)
           
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
    print()
    get_transaction_date()
    get_transaction_category(user1)
    get_transaction_description()
    #transaction_amount()

def by_date():
    """
    Displays all transactions made since the beginning of the year to the user in table format
    """
    print("""
    --------------------------------------------------------------------------------
                            View Statement By Date
    --------------------------------------------------------------------------------
    """)
    # Credit for table format https://www.educba.com/python-print-table/
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

def by_category(user1):
    """
    Calculates total expenses in each category and displays them to the user.
    """
    print("""
    --------------------------------------------------------------------------------
                          View Statement By Category
    --------------------------------------------------------------------------------
    """)
    category_total = {}

    for row in user1:
        category = row[1]
        amount = float(row[3])

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    #total_amount = sum(amount.range(0,-1))    
    alphabetized_category_total = dict(sorted(category_total.items()))
    print(tabulate(alphabetized_category_total.items(), headers = ["Category", "Amount"]))
    #print(total_amount)

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
            if statement_choice == "1":
                print("You have chosen option 1: By date.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_date()
                break
            elif statement_choice == "2":
                print("You have chosen option 2: By month.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_month()
                break
            elif statement_choice == "3":
                print("You have chosen option 3: By category.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_category(user1)
                break
            elif statement_choice.lower() == "mm":
                print("You have chosen to go back to the Main Menu")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                main_menu()
                break
            else:
                raise ValueError(Fore.RED + "Please select one of the options provided" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + f'Invalid data.\n Please enter option 1, 2, or 3 to see your transactions or enter mm to go back to the Main Menu' + Style.RESET_ALL)
            return False

def view_budget_goals():
    """
    Displays users spending goals for each category
    """
    print(Fore.MAGENTA + """
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
            
            if user_input == "1":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Add new expense form is loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                add_new_expense()
                break
            elif user_input == "2":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        View statement is loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                view_statement()
                break
            elif user_input == "3":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                            View budget goals is loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                view_budget_goals()
                break
            elif user_input == "4":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.YELLOW)
                typingPrint("""
                                        Exiting, please wait...                           """)
                print(Style.RESET_ALL)
                delayed_clear()
                welcome_page()
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f'Invalid data: Please select one of the options provided' + Style.RESET_ALL)
            delayed_clear()

def pennywise_program():
    welcome_page()
    main_menu()

pennywise_program()
#add_new_expense()
#get_transaction_category(user1)
#get_transaction_description()