import gspread
from google.oauth2.service_account import Credentials
import time
import os
import sys
import datetime
from tabulate import tabulate
import math
import colorama
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


# Credit: https://www.geeksforgeeks.org/clear-screen-python/
def clear_screen():
    """
    Clears CLI ahead of next code page
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("\033c", end="")


def delayed_clear():
    """
    Clears CLI code after 6 seconds
    """
    time.sleep(6)
    clear_screen()


# Credit: https://www.101computing.net/python-typing-text-effect/
def typingPrint(text):
    """
    In place of print() to create a typing text effect
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def welcome_page():
    """
    Displays program name and welcome text to user
    """
    print(Fore.GREEN + Style.BRIGHT + '''

    $$$$$$                                            $$
    $$   $$
    $$   $$ $$$$$  $$$$$$  $$$$$$  $$   $$ $$  $$  $$ $$  $$$$$   $$$$$
    $$$$$$ $$   $$ $$   $$ $$   $$ $$   $$ $$  $$  $$ $$ $$      $$ __$$
    $$     $$$$$$$ $$   $$ $$   $$ $$   $$ $$  $$  $$ $$  $$$$$  $$$$$$$
    $$     $$      $$   $$ $$   $$ $$   $$ $$  $$  $$ $$      $$ $$
    $$      $$$$$$ $$   $$ $$   $$  $$$$$$  $$$$ $$$  $$  $$$$$   $$$$$$
                                        $$
                                   $$   $$
                                    $$$$$
    ''' + Fore.WHITE + '''
    Welcome back to Pennywise, your budget tracker to keep you on top of
                               your expenses.
    ''')
    print()
    typingPrint(Fore.BLUE + """
                         Loading, please wait...""" + Fore.WHITE)


def get_transaction_date():
    """
    Gets the date of the transaction they want to add from the user.
    """
    print("""
    --------------------------------------------------------------------
                            Add New Expense
    --------------------------------------------------------------------
    """)
    print("""
    You will now need to enter the date, category, description and
    amount of the expense you would like to add. Please have this
    information ready.""")
    print()
    while True:
        try:
            print()
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + """
        Please enter the date of the transaction in the following
        format (DD/MM/YYYY):""")
            print()
            expense_input_date = input("""
            >""" + Fore.WHITE)
            global new_date
            # Converts user date input into datetime object
            # Credit in README
            date = datetime.datetime.strptime(expense_input_date, '%d/%m/%Y')
            # initializing date ranges
            min_date = datetime.datetime(2024, 1, 1)
            max_date = datetime.datetime.now()

            if date >= min_date and date <= max_date:
                new_date = date.date().strftime("%d/%m/%Y")
                clear_screen()
                break
            else:
                raise ValueError("")
        except ValueError:
            print(Fore.RED + '''
            Invalid data. Please enter a date which lies between 01/01/2024
            and today.'''
                  + Fore.WHITE)
    clear_screen()


def get_transaction_category(user1):
    """
    Gets the category of the transaction they want to add from the user.
    """
    print("""
    --------------------------------------------------------------------
                            Add New Expense
    --------------------------------------------------------------------
    """)
    print("""
    You will now need to enter the date, category, description and
    amount of the expense you would like to add. Please have this
    information ready.""")
    print()
    print()
    print(f"""
    You may enter a category you have already used or choose another.""")
    print()
    current_choices = [row[1] for row in user1]
    one_cat_list = []

    # Credit in README
    for category in current_choices:
        if category not in one_cat_list:
            one_cat_list.append(category)
    sorted_list = sorted(one_cat_list)
    for i in sorted_list:
        print(f'                    {i}')

    print()

    while True:
        try:
            print()
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT +'''
            Please enter the category of the transaction:''')
            user_input = input("            > " + Fore.WHITE)
            print()

            global exp_cat
            exp_cat = user_input.capitalize()
            if (
                2 < len(exp_cat) < 16 and len(exp_cat.strip()) != 0 and
                    exp_cat.isalpha()
            ):
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"""
            Invalid input: {e} The category must be ONE word between 3 - 15
            letters.""" + Fore.WHITE)


def get_transaction_description():
    """
    Gets the description of the transaction they want to add from the user.
    """
    print("""
    --------------------------------------------------------------------
                            Add New Expense
    --------------------------------------------------------------------
    """)
    print("""
    You will now need to enter the date, category, description and
    amount of the expense you would like to add. Please have this
    information ready.""")
    print()
    # Credit in README
    while True:
        try:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '''
            Please enter the description of the transaction.''')
            global new_dscr
            new_dscr = input('''
            >''' + Fore.WHITE)

            # Credit in README
            if (
                3 <= len(new_dscr) <= 30 and len(new_dscr.strip()) != 0
                    and new_dscr.isalpha()
            ):
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"""
            Invalid input: The description needs to be ONE word between
            3 - 30 letters long.""" + Fore.WHITE)


def get_transaction_amount():
    """
    Gets the amount of the transaction they want to add from the user.
    """
    print("""
    --------------------------------------------------------------------
                            Add New Expense
    --------------------------------------------------------------------
    """)
    print("""
    You will now need to enter the date, category, description and
    amount of the expense you would like to add. Please have this
    information ready.""")
    print()
    while True:
        try:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '''
        Please enter the amount of the transaction, e.g. 29.95''')
            print()
            print(Style.NORMAL + """
        Please do not include currency and make sure you have
        entered a number between 0 - 999.""")
            user_input = float(input(Style.BRIGHT + """
        >""" + Fore.WHITE))
            global new_amount
            # Credit in README
            new_amount = float("{:.2f}".format(user_input))
            if new_amount != "" and 0 < new_amount < 1000:
                print()
                typingPrint(Fore.BLUE + """
                            Loading new expense summary..."""
                            + Fore.WHITE)
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + """
            Invalid input: Please make sure you have entered
            a number between 0 - 999.""" + Fore.WHITE)


def confirm_new_expense():
    """
    Summarizes all the new expense information the user has given.
    Asks user to confirm all details are correct. If not user can
    start again or return to main menu.
    """
    print()
    print("""
    --------------------------------------------------------------------
                            Add New Expense
    --------------------------------------------------------------------
    """)
    print()
    print("""
            Here is the new expense information you provided:
    """)
    print()
    print(f"                     Date:               {new_date}")
    print(f"                     Category:           {exp_cat}")
    print(f"                     Description:        {new_dscr}")
    print(f"                     Amount:             £{new_amount}")
    print()

    while True:
        try:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + """
                Is this information correct? Please enter Y/N""")
            user_input = input("                >" + Fore.WHITE)
            if user_input.lower() == "y":
                confirmed_expense = [str(new_date), exp_cat,
                                     new_dscr, new_amount]
                update_worksheet(confirmed_expense)
                break
            elif user_input.lower() == 'n':
                print("""
            Would you like to:

            1. Re-enter the information?
            2. Return to the Main Menu?

            If you wanted to enter 'YES' for the previous question but
            made a mistake, please enter Y now to save your
            information.""")
                while True:
                    try:
                        print()
                        no_answer = input(Fore.LIGHTCYAN_EX +
                                          """                >"""
                                          + Fore.WHITE)
                        print()
                        if no_answer == "1":
                            typingPrint(Fore.BLUE + """
            Deleting new expense data, please wait..."""
                                        + Fore.WHITE)
                            clear_screen()
                            add_new_expense()
                        elif no_answer == "2":
                            typingPrint(Fore.YELLOW + """
        Deleting new expense data and returning to Main Menu, please wait..."""
                                        + Fore.WHITE)
                            clear_screen()
                            main_menu()
                        elif no_answer.lower() == "y":
                            confirmed_expense = [new_date,
                                                 exp_cat,
                                                 new_dscr, new_amount]
                            update_worksheet(confirmed_expense)
                        else:
                            raise ValueError("")
                    except ValueError as e:
                        print(Fore.RED + """
                    Invalid input: Please choose one of the options above"""
                              + Fore.WHITE)
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + """
            Invalid input: Please choose one of the options above""" +
                  Fore.WHITE)


def update_worksheet(data):
    """
    Updates user1 worksheet, adds new row with the list data provided
    """
    typingPrint(Fore.BLUE + Style.BRIGHT + """
                Updating worksheet, please wait...""" + Fore.WHITE)
    print()
    user1_expenses = SHEET.worksheet("user1")
    user1_expenses.append_row(data)
    print(Fore.MAGENTA + """
                Worksheet updated successfully."""
          + Fore.WHITE)
    print()
    print("""
            What would you like to do next?

            1. Add another expense
            2. Go back to Main Menu
        """)

    while True:
        try:
            user_input = input(Fore.LIGHTCYAN_EX + """
            >""" + Fore.WHITE)
            if user_input == "1":
                print(f"            You chose option: {user_input}")
                print()
                typingPrint(Fore.BLUE + """
                    Add new expense form is loading, please wait...
                        """ + Fore.WHITE)
                clear_screen()
                add_new_expense()
                break
            elif user_input == "2":
                print(f"            You chose option: {user_input}")
                print()
                typingPrint(Fore.YELLOW + """
                    Returning to Main Menu, please wait..."""
                            + Fore.WHITE)
                clear_screen()
                main_menu()
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"""
            Invalid data: Please select one of the options provided
                """ + Fore.WHITE)


def add_new_expense():
    """
    The step-by-step of how a user inputs information to add a new expense.
    """
    get_transaction_date()
    clear_screen()
    get_transaction_category(user1)
    clear_screen()
    get_transaction_description()
    clear_screen()
    get_transaction_amount()
    clear_screen()
    confirm_new_expense()


def by_date():
    """
    Displays all transactions made since the beginning of the year
    to the user in table format
    """
    clear_screen()
    print("""
    --------------------------------------------------------------------
                        View Statement By Date
    --------------------------------------------------------------------
    """)
    # Credit in README
    sorted_user1 = sorted(user1, key=lambda i:
                          datetime.datetime.strptime(i[0], "%d/%m/%Y"))
    # Credit for table format https://www.educba.com/python-print-table/
    print(f'{tabulate(sorted_user1,
             headers=["Date", "Category", "Description", "Amount"])}')
    print()
    print(Fore.CYAN +
          """    PLEASE NOTE: If you have just added an new expense via
          the 'Add new expense form' it will not yet show up here. It
          will only be able to view once you log on again."""
          + Fore.WHITE)
    print()
    print("""
    What would you like to do next?
    1. Go back to View Statement Menu
    2. Go back to Main Menu
    """)
    while True:
        try:
            user_input = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "    >" + Fore.WHITE)
            if user_input.lower() == "1":
                print("    You have chosen to go back to View Statement Menu.")
                print()
                typingPrint(Fore.BLUE + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                view_statement()
            elif user_input.lower() == "2":
                print("    You have chosen togo back to Main Menu.")
                print()
                typingPrint(Fore.YELLOW + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                main_menu()
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"""
            Invalid input: Please choose one of the options above."""
                  + Fore.WHITE)


def by_category(user1):
    """
    Calculates total expenses in each category since the beginning of the
    year and displays them to the user.
    """
    clear_screen()
    print("""
    --------------------------------------------------------------------
                        View Statement By Category
    --------------------------------------------------------------------
    """)
    category_total = {}
    for column in user1:
        category = column[1]
        amount = float(column[3])

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    total_amount = 0
    for value in user1:
        total_amount += float(value[3])

    alphabetized_category_total = dict(sorted(category_total.items()))
    print(tabulate(
        alphabetized_category_total.items(), headers=["Category", "Amount"]))
    print()
    print(f"TOTAL:          {math.ceil(total_amount*100)/100}")
    print()
    print(Fore.CYAN + """
        PLEASE NOTE: If you have just added an new expense via the
    'Add new expense form' it will not yet show up here. It will only
    be able to view once you log on again.""" + Fore.WHITE)
    print()
    print("""
    What would you like to do next?

    1. Go back to View Statement Menu
    2. Go back to Main Menu
    """)

    try:
        user_input = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "    >" + Fore.WHITE)
        if user_input == "1":
            print("        You have chosen to go back to View Statement Menu.")
            print()
            typingPrint(Fore.BLUE + """
                                Loading, please wait...""" + Fore.WHITE)
            clear_screen()
            view_statement()
        elif user_input == "2":
            print("        You have chosen to go back to Main Menu.")
            print()
            typingPrint(Fore.YELLOW + """
                                Loading, please wait...""" + Fore.WHITE)
            clear_screen()
            main_menu()
        else:
            raise ValueError("")
    except ValueError as e:
        print(Fore.RED + """
        Invalid input: Please choose from one of the options above."""
              + Fore.WHITE)


def by_month():
    """
    Displays the amount the user has spent each month since the beginning
    of the year.
    New months have to be manually added once transaction have been added
    in that month.
    """
    jan_total = {}
    feb_total = {}
    mar_total = {}
    apr_total = {}
    may_total = {}
    jun_total = {}
    jul_total = {}

    for column in user1:
        dates = column[0]
        amount = float(column[3])

        jan = dates[3] == '0' and dates[4] == '1'
        if jan in jan_total:
            jan_total[jan] += amount
        else:
            jan_total[jan] = amount

        feb = dates[3] == '0' and dates[4] == '2'
        if feb in feb_total:
            feb_total[feb] += amount
        else:
            feb_total[feb] = amount

        mar = dates[3] == '0' and dates[4] == '3'
        if mar in mar_total:
            mar_total[mar] += amount
        else:
            mar_total[mar] = amount

        apr = dates[3] == '0' and dates[4] == '4'
        if apr in apr_total:
            apr_total[apr] += amount
        else:
            apr_total[apr] = amount

        may = dates[3] == '0' and dates[4] == '5'
        if may in may_total:
            may_total[may] += amount
        else:
            may_total[may] = amount

        jun = dates[3] == '0' and dates[4] == '6'
        if jun in jun_total:
            jun_total[jun] += amount
        else:
            jun_total[jun] = amount

        jul = dates[3] == '0' and dates[4] == '7'
        if jul in jul_total:
            jul_total[jul] += amount
        else:
            jul_total[jul] = amount

    print("""
    --------------------------------------------------------------------
                         View Statement By Month
    --------------------------------------------------------------------
    """)

    print(f'        In January, you spent               {jan_total[1]}')
    print(f'        In February, you spent              {feb_total[1]}')
    print(f'        In March, you spent                 {mar_total[1]}')
    print(f'        In April, you spent                 {apr_total[1]}')
    print(f'        In May, you spent                   {may_total[1]}')
    print(f'        In June, you spent                  {jun_total[1]}')
    print(f'        In July, you spent                  {jul_total[1]}')

    print()
    print(Fore.CYAN + """
        If you would like to see your exact transactions per month,
    please go to View Statements by Date.""" + Fore.WHITE)
    print()
    print("""
    What would you like to do next?

    1. Go to View Statement by date
    2. Go back to View Statement Menu
    3. Go back to Main Menu
    """)

    try:
        user_input = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "    >" + Fore.WHITE)
        if user_input == "1":
            print("        You have chosen to View Statement by date.")
            print()
            typingPrint(Fore.BLUE + """
                                Loading, please wait...""" + Fore.WHITE)
            clear_screen()
            by_date()
        elif user_input == "2":
            print("""
                    You have chosen to go back to View Statement Menu.""")
            print()
            typingPrint(Fore.BLUE + """
                                Loading, please wait...""" + Fore.WHITE)
            clear_screen()
            view_statement()
        elif user_input == "3":
            print("        You have chosen to go back to Main Menu.")
            print()
            typingPrint(Fore.YELLOW + """
                                Loading, please wait...""" + Fore.WHITE)
            clear_screen()
            main_menu()
        else:
            raise ValueError("")
    except ValueError as e:
        print(Fore.RED + """
        Invalid input: Please choose from one of the options above."""
              + Fore.WHITE)


def view_statement():
    """
    Displays a menu giving 3 options of how the user wants to see their
    statement: by date, by month, by category
    """
    clear_screen()
    print("""
        --------------------------------------------------------------------
                                View Statement
        --------------------------------------------------------------------
        """)
    print("        How would you like to see your transactions?")
    print("""
        1. By date
        2. By month
        3. By category""")
    print("""
        If you would like to go back to the main menu, please enter MM""")
    while True:
        try:
            user_input = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "        >"
                               + Fore.WHITE)
            if user_input == "1":
                print("        You have chosen option 1: By date.")
                print()
                typingPrint(Fore.BLUE + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                by_date()
            elif user_input == "2":
                print("        You have chosen option 2: By month.")
                print()
                typingPrint(Fore.BLUE + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                by_month()
            elif user_input == "3":
                print("        You have chosen option 3: By category.")
                print()
                typingPrint(Fore.BLUE + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                by_category(user1)
            elif user_input.lower() == "mm":
                print("        You have chosen to go back to the Main Menu")
                print()
                typingPrint(Fore.YELLOW + """
                            Loading, please wait...""" + Fore.WHITE)
                clear_screen()
                main_menu()
                break
            else:
                raise ValueError("")
        except ValueError:
            print(Fore.RED + """
            Invalid data: Please choose one of the options above or
            enter MM to go back to the Main Menu.""" + Fore.WHITE)


def main_menu():
    """
    Displays the main menu to user, where they can choose how to proceed
    """
    print("""
        --------------------------------------------------------------------
                                Main Menu
        --------------------------------------------------------------------
        """)
    print("""
        What would you like to do today?

        1. Add new expense
        2. View statement
        3. Exit
        """)
    while True:
        try:
            user_input = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "        >"
                               + Fore.WHITE)
            if user_input == "1":
                print(f"        You chose option: {user_input}")
                print()
                typingPrint(Fore.BLUE + """
                    Add new expense form is loading, please wait..."""
                            + Fore.WHITE)
                clear_screen()
                add_new_expense()
            elif user_input == "2":
                print(f"        You chose option: {user_input}")
                print()
                typingPrint(Fore.BLUE + """
                    View statement is loading, please wait...""" + Fore.WHITE)
                clear_screen()
                view_statement()
            elif user_input == "3":
                print(f"        You chose option: {user_input}")
                print()
                typingPrint(Fore.YELLOW + """
                            Exiting, please wait...""" + Fore.WHITE)
                clear_screen()
                pennywise_program()
            else:
                raise ValueError("")
        except ValueError as e:
            print(Fore.RED + f"""
            Invalid input: Please choose one of the options above"""
                  + Fore.WHITE)


def pennywise_program():
    """
    Runs Pennywise program
    """
    welcome_page()
    delayed_clear()
    main_menu()


pennywise_program()
