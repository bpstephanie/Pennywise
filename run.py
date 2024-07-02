import gspread
from google.oauth2.service_account import Credentials
import time
import os
import sys
import datetime
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
    Clears CLI code after 10 seconds
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
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)
    print(f"You will now need to enter the date, category, description and transaction amount of the expense you would like to add. Please have this information ready.\n")
    print()
    while True:
        try:
            print()
            print(f"Please enter the date of the transaction in the following format(DD/MM/YYYY):")
            print()
            expense_input_date = input("> \n")
            global new_date
            # Converts user date input into datetime object
            # Credit for code https://stackoverflow.com/questions/53248537/typeerror-not-supported-between-instances-of-datetime-datetime-and-str
            date = datetime.datetime.strptime(expense_input_date, '%d/%m/%Y')
            
            # initializing date ranges
            min_date = datetime.datetime(2024, 1, 1)
            max_date = datetime.datetime.now()

            if date >= min_date and date <= max_date:
                new_date = date.date().strftime("%d/%m/%Y")
                return new_date
            else:
                raise ValueError(Fore.RED + "The date you've entered is out of range" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Invalid data. Please enter a date which lies between 01/01/2024 and today.' + Style.RESET_ALL)

def get_transaction_category(user1):
    """
    Gets the category of the transaction from the user.
    """
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)
    print(f"You will now need to enter the date, category, description and transaction amount of the expense you would like to add. Please have this information ready.\n")
    print()
    print()
    print(f"The current category you have are: ")
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
    print()
    print("You can also enter a different category.")
    print()

    while True:
        print()
        print('Please enter the category of the transaction:')
        user_input = input("> \n")

        global expense_input_category
        expense_input_category = user_input.capitalize()
    
        try:
            if expense_input_category !='' and len(expense_input_category) <= 15 and all(chr.isalpha() or chr.isspace() for chr in expense_input_category):
                return expense_input_category
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}. The category must be 14 letters or less." + Style.RESET_ALL)
        
def get_transaction_description():
    """
    Gets the description of the transaction from the user.
    """
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)
    print(f"You will now need to enter the date, category, description and transaction amount of the expense you would like to add. Please have this information ready.\n")
    print()
    # Credit for code to only accept letters: https://www.shiksha.com/online-courses/articles/isalpha-method-in-python/#:~:text=The%20isalpha()%20method%20can,entered%20only%20contains%20alphabetic%20characters.
    while True:
        try:
            print('Please enter the description of the transaction.')
            global new_description
            new_description = input('> \n')

            if new_description != '' and 3 <= len(new_description) <= 30 and all(chr.isalpha() or chr.isspace() for chr in new_description):
                return new_description
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"Invalid input: The description needs to be between 3 and 30 letters long." + Style.RESET_ALL)

def get_transaction_amount():
    """
    Gets the amount of the transaction from the user.
    """
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)
    print(f"You will now need to enter the date, category, description and transaction amount of the expense you would like to add. Please have this information ready.\n")
    print()
    while True:
        print('Please enter the amount of the transaction, e.g. 29.95')
        print()
        print("Please do not include currency and make sure the amount is not more than 5000")
        user_input = input('> \n')
        global new_amount
        new_amount = float(user_input)
        try:
            if new_amount != "" and new_amount > 0 and new_amount <= 5000:
                return new_amount
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + "Invalid input: Please make sure you have not entered an amount more than 5000." + Style.RESET_ALL)

def confirm_new_expense():
    """
    Summarizes all the new expense information the user has given.
    Asks user to confirm all details are correct.
    """
    print()
    print("""
    --------------------------------------------------------------------------------
                                    Add New Expense
    --------------------------------------------------------------------------------
    """)
    print()
    print("""
                Here is the new expense information you provided:               
    """)
    print()
    print(f"                          Date:               {new_date}")
    print(f"                          Category:           {expense_input_category}")
    print(f"                          Description:        {new_description}")
    print(f"                          Amount:             £{new_amount}")
    print()
    print("                 Is this information correct? Please enter Y/N")
    user_input = input("                    > \n")

    while True:
        try:
            if user_input.lower() == "y":
                confirmed_expense = [str(new_date), expense_input_category, new_description, new_amount]
                update_worksheet(confirmed_expense)
                break
            elif user_input.lower() == 'n':
                print("""
                          Would you like to: 
                
                          1. Re-enter the information?
                          2. Return to the Main Menu?
                
                If you wanted to enter 'YES' for the previous question but made
                a mistake, please enter Y now to save your information.""")
                print()
                no_answer = input("                             > \n")
                print()
                if no_answer == "1":
                    print(Fore.BLUE)
                    typingPrint("               Deleting new expense data, please wait...               ")
                    print(Style.RESET_ALL)
                    clear_screen()
                    add_new_expense()
                elif no_answer == "2":
                    print(Fore.BLUE)
                    typingPrint("    Deleting new expense data and returning to Main Menu, please wait...               ")
                    print(Style.RESET_ALL)
                    clear_screen()
                    main_menu()
                elif no_answer.lower() == "y":
                    confirmed_expense = [new_date, expense_input_category, new_description, new_amount]
                    update_worksheet(confirmed_expense)
                    break
                else:
                    raise ValueError("")
            else:
                raise ValueError("")
        except ValueError as e:
            print("Invalid input")

def update_worksheet(data):
    """
        Update user1 worksheet, add new row with the list data provided
    """
    print(Fore.BLUE)
    typingPrint("                      Updating worksheet, please wait...               ")
    print(Style.RESET_ALL)
    user1_expenses = SHEET.worksheet("user1")
    user1_expenses.append_row(data)
    print('                       Worksheet updated successfully.\n')

    while True:
        print("""
                          What would you like to do next?
        
                          1. Add another expense
                          2. Go back to Main Menu
        """)


        try:
            user_input = input("                          > \n")
            
            if user_input == "1":
                print(f"                          You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Add new expense form is loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                add_new_expense()
                break
            elif user_input == "2":
                print(f"                          You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                            Returning to Main Menu, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                main_menu()
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f'               Invalid data: Please select one of the options provided' + Style.RESET_ALL)
            delayed_clear()

def add_new_expense():
    """
    Gets expense details from user
    """
    get_transaction_date()
    clear_screen()
    get_transaction_category(user1)
    clear_screen()
    get_transaction_description()
    clear_screen()
    get_transaction_amount()
    print(Fore.BLUE)
    typingPrint("         Loading new expense summary...                          ")
    print(Style.RESET_ALL)
    time.sleep(2)
    clear_screen()
    confirm_new_expense()

def by_date():
    """
    Displays all transactions made since the beginning of the year to the user in table format
    """
    print("""
    --------------------------------------------------------------------------------
                            View Statement By Date
    --------------------------------------------------------------------------------
    """)
    while True:
        # Credit for sorting the date by date: https://docs.python.org/3/howto/sorting.html
        sorted_user1 = sorted(user1, key=lambda i: datetime.datetime.strptime(i[0], "%d/%m/%Y"))
        
        # Credit for table format https://www.educba.com/python-print-table/
        print(tabulate(sorted_user1, headers=["Date", "Category", "Description", "Amount"]))
        print("""
        What would you like to do next?
        1. Go back to View Statement Menu
        2. Go back to Main Menu
        """)
        
        try:
            user_input = input("> \n")

            if user_input.lower() == "1":
                clear_screen()
                view_statement()
            elif user_input.lower() == "2":
                clear_screen()
                main_menu()
            else:
                raise ValueError("")
        except ValueError as e:
            print("Invalid input: Please choose option 1 or option 2.")

def by_category_per_month(user1):
    """
    Calculates total expenses in each category per month and displays them to the user.
    """
    print("PER MONTH")

def by_category_per_year(user1):
    """
    Calculates total expenses in each category since the beginning of the year and displays them to the user.
    """
    print("PER YEAR")
    category_total = {}

    for row in user1:
        category = row[1]
        amount = float(row[3])

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount
    
    total_amount = 0
    for value in user1:
        total_amount += float(value[3])
       
    alphabetized_category_total = dict(sorted(category_total.items()))
    print(tabulate(alphabetized_category_total.items(), headers = ["Category", "Amount"]))
    print()
    print(f"TOTAL:       {total_amount}")
    print()
    print("""
        What would you like to do next?

        1. Go back to View Statement Menu
        2. Go back to Main Menu
        
        """)
    
    user_input = input("        > \n")
    try:
        if user_input == "1":
            print(f"    You chose option: {user_input}")
            clear_screen()
            view_statement()
        elif user_input == "2":
            print(f"    You chose option: {user_input}")
            clear_screen()
            main_menu()
        else:
            raise ValueError("")
    except ValueError as e:
        print("Please choose from one of the options above.")

def by_category():
    """
    Calculates total expenses in each category and displays them to the user.
    """
    print("""
    --------------------------------------------------------------------------------
                          View Statement By Category
    --------------------------------------------------------------------------------
    """)
    
    print("""
        Would you like to see transactions per category per month or per year?
        
        1. Per month
        2. Per year
        
        If you would like to go back to the Main Menu, please enter MM""")
    
    user_input = input("    > \n")
    
    try:
        if user_input == "1":
            print(f"    You chose option: {user_input}")
            print()
            by_category_per_month(user1)
        elif user_input == "2":
            print(f"    You chose option: {user_input}")
            print()
            by_category_per_year(user1)
        elif user_input.lower() == "mm":
            print(f"    You chose option: {user_input}")
            print()
            clear_screen()
            main_menu()
        else:
            raise ValueError("")
    except ValueError as e:
        print("Please choose from one of the options above.")     

def by_month():
    """
    Displays the amount the user has spent each month since the beginning of the year
    """

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
        print("     How would you like to see your transactions?")
        print("""
        1. By date
        2. By month
        3. By category""")
        print("     If you would like to go back to the main menu, please enter MM")

        try:
            user_input = input("        > \n")
            if user_input == "1":
                print("     You have chosen option 1: By date.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                                Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_date()
                break
            elif user_input == "2":
                print("     You have chosen option 2: By month.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                                Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_month()
                break
            elif user_input == "3":
                print("     You have chosen option 3: By category.")
                print()
                print(Fore.BLUE)
                typingPrint("""
                                Loading, please wait...                           """)
                print(Style.RESET_ALL)
                clear_screen()
                by_category()
                break
            elif user_input.lower() == "mm":
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
                raise ValueError("")
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
            user_input = input("        Enter your choice here: \n")
            
            if user_input == "1":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        Add new expense form is loading, please wait...                 """)
                print(Style.RESET_ALL)
                clear_screen()
                add_new_expense()
                break
            elif user_input == "2":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                        View statement is loading, please wait...                       """)
                print(Style.RESET_ALL)
                clear_screen()
                view_statement()
                break
            elif user_input == "3":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.BLUE)
                typingPrint("""
                            View budget goals is loading, please wait...                """)
                print(Style.RESET_ALL)
                clear_screen()
                view_budget_goals()
                break
            elif user_input == "4":
                print(f"        You chose option: {user_input}")
                print()
                print(Fore.YELLOW)
                typingPrint("""
                                        Exiting, please wait...                         """)
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

#pennywise_program()
#add_new_expense()
#get_transaction_category(user1)
#get_transaction_description()
view_statement()
