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

Find out how much you have spent this month and if you've done enough to hold off Pennywise...

    ''')
    typingPrint("                                     Loading, please wait...")
    time.sleep(12)
    clear_screen()

def main_menu():
    """
    
    """

def main():
    welcome_page()
    main_menu()

main()