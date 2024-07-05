# Pennywise
Pennywise is a budget tracker that has been created with the user in mind.

Welcome to <a href="https://pennywise-budget-tracker-ce1c05dc8133.herokuapp.com/">Pennywise</a>


![Pennywise](assets/images/welcome_page.png)

## Contents
* [**User Experience UX**](<#user-experience-ux>)
  * [Site Owner's Goal](<#site-owner's-goals>)
  * [User Stories](<#user-stories>)
  * [Site Structure](<#site-structure>)
  * [Flowchart](<#flowchart>)
  * [Data Model](<#data-model>)
  * [Design Choices](<#design-choices>)
    * [Typography](<#typography>)
    * [Colour Scheme](<#colour-scheme>)
* [**Features**](<#features>)
  * [Existing Features](<#existing-features>)
    * [Welcome Page](<#welcome-page>)
    * [Main Menu](<#main-menu>)
    * [Add New Expense](<#add-new-expense>)
      * [Add Date of Transaction](<#add-date-of-transaction>)
      * [Add Category of Transaction](<#add-category-of-transaction>)
      * [Add Description of Transaction](<#add-description-of-transaction>)
      * [Add Amount of Transaction](<#add-amount-of-transaction>)
      * [Confirm Expense](<#confirm-expense>)
      * [Update Worksheet](<#update-worksheet>)
    * [View Statement Menu](<#view-statement-menu>)
      * [By Date](<#by-date>)
      * [By Month](<#by-month>)
      * [By Category](<#by-category>)
  * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
  * [Languages](<#languages>)
  * [Resources and Tools](<#rescources-and-tools>)
* [**Testing**](<#testing>)
  * [Code Validation](<#code-validation>)
  * [Additional Teasting](<#additional-testing>)
  * [Known Bugs](<#known-bugs>)
* [**Deployment**](<#deployment>)
  * [**To Deploy the Project**](<#to-deploy-the-project>)
  * [**To Fork the Project**](<#to-fork-the-project>)
  * [**To Clone the Project**](<#to-clone-the-project>)
* [**Credits**](<#credits>)
  * [**Content**](<#content>)
  * [**Media**](<#media>)
* [**Acknowledgements**](<#acknowledgements>)

# User Experience UX
### Site Owner's Goal
* Site Owner:
    - As a site owner, I want users to easily understand what the program does.
    - As a site owner, I want users to be able to navigate through the program without any issues.
    - As a site owner, I want users to be able to add their expenses, view their expenses and set their budget goals.

### User Stories

 * Site-users:
    - As a user, I want to understand what the program does instantly. 
    - As a user, I want to be able to add my expenses and confirm if they are correct.
    - As a user, I want to be able to track my expenses.
    - As a user, I want to be able to view my expenses in different formats that are easy to understand.
    - As a user, I want to get visual feedback when I've done something wrong.
    - As a user, I want 

[Back To Top](<#contents>)

### Site Structure

Pennywise is a terminal based application that consists of one page.When the program is run, the user is shown the welcome page with the program's name and a short message explaining what it is. After a short while the user is shown the Main Menu. The Main Menu has four option: add new expense, view statement, view budget goals and exit.

Pennywise was structured with the user in mind, whichever option the user chooses, once they have completed that action they are given the option to go back to the Main Menu or in some cases a sub-menu.

At the top left of the page, just above the console screen, there is a Run Program button which will reload Pennywise.

[Back To Top](<#contents>)

### Flowchart

The flowchart for Pennywise was made with the online service [Diagrams.net](https://app.diagrams.net/). The goal was to keep it as simple to understand as possible. It was made prior to starting and was a very helpful guide when coding the logic.

<details><summary>Flowchart</summary>

![Flowchart](assets/images/PP3_Flowchart.webp)

</details>

[Back To Top](<#contents>)

### Data Model

[Google Sheets](https://workspace.google.com/products/sheets/) have been used to store all data. All data the the user inputs and views is retreived from and update to the Google Sheet. The name of the workbook is Pennywise and the name of the worksheet is user1.

The worksheet has 4 columns of data that save the date, category, description and amount of each transaction.

<details><summary>Google Sheet</summary>

![Pennywise Google Sheet](assets/images/PP3_Google_Sheet.png)

</details>


[Back To Top](<#contents>)

### Design Choices

 - ### Typography
   Due to Pennywise being a terminal based application, no specific typography has been used. The standard font is being used in the terminal.

 - ### Colour Scheme
   Pennywise is back-end program therefore not much styling or visual design has been implementes. 

   * [Colorama](https://pypi.org/project/colorama/) library for Python was used to add colour to the program to give visual feedback to the user.
      - Red has been used for invalid input messages.
      - Blue has been used for loading messages.
      - Yellow has been used for messages regarding exiting the program   
        or returning to the Main Menu.
      - Cyan has been used for the please note messages in the view 
        statement section.
      - Light cyan has been used for instructions before user input.
      - Magenta has been for feedback regarding the worksheet being 
        updated successfully.
      - Dim style has been used to give extra information about user input.

 [Back To Top](<#contents>)

# Features
  ## Existing Features

  - ### Welcome Page
    When the user first enters the site, the welcome page greets them. The user sees the logo and a short message explaining what the program does. Whilst the user is viewing this page, the [Main Menu](<#main-menu>) is loading.
  
  <details><summary>Welcome Page</summary>
  
  ![Welcome Page](assets/images/welcome_page.png)
  
  </details>

  [Back To Top](<#contents>)

  - ### Main Menu
    The [Main Menu](<#main-menu>) gives the user 3 choices: [Add New Expense](<#add-new-expense>), [View Statement](<#view-statement>) or Exit. If the user chooses to exit, they will be redirected back to the [Welcome Page](<#welcome-page>).

  <details><summary>Main Menu</summary>
    
  ![Main Menu](assets/images/main-menu.png)

  </details>

  [Back To Top](<#contents>)

  - ### Add New Expense
    The add new expense function collects 4 pieces of information from the user. These are the [date](<#add-date-of-transaction>), [category](<#add-category-of-transaction>), [description](<#add-description-of-transaction>) and [amount](<#add-amount-of-transaction>) of the transaction. Once all 4 details have been collected, the user is shown a summary of that information in the [Confirm Transaction](<#confirm-transaction>) function. If the user confirms all the details are correct. The google worksheet will be updated with the new expense. However, if the user entered something wrong they can choose to add the information again, or even return to the [Main Menu](<#main-menu>).

    [Back To Top](<#contents>)

    - #### Add Date of Transaction
      The user is asked for the date and is shown the format it needs to be in. If the user enters an invalid response an error message appears and the user is asked to re-enter the information in the correct format.
    <details><summary>Add Date of Transaction</summary>
      
    ![Add Date of Transaction](assets/images/add-expense-date)
    
    </details>

    <details><summary>Invalid Input</summary>
      
    ![Add Date of Transaction Invalid Input](assets/images/add_expense_date_invalid_input)
    
    </details>

    [Back To Top](<#contents>)
    
    - #### Add Category of Transaction
      The user is asked for the category of the transaction. If the user enters an invalid response an error message appears and the user is asked to re-enter the information in the correct format.
    <details><summary>Add Category of Transaction</summary>
    
    ![Add Category of Transaction](assets/images/add-expense-category)
    
    </details>

    <details><summary>Invalid Input</summary>
      
    ![Add Category of Transaction Invalid Input](assets/images/add_expense_category_invalid_input)
    
    </details>

    [Back To Top](<#contents>)

    - #### Add Description of Transaction
      The user is asked for the description of the transaction. If the user enters an invalid response an error message appears and the user is asked to re-enter the information in the correct format.
    
    <details><summary>Add Description of Transaction</summary>
      
    ![Add Description of Transaction](assets/images/add-expense-description)
    
    </details>

    <details><summary>Invalid Input</summary>
      
    ![Add Description of Transaction Invalid Input](assets/images/add_expense_description_invalid_input)
    
    </details>

    [Back To Top](<#contents>)

    - #### Add Amount of Transaction
      The user is asked for the amount of the transaction. They are shown the format the input needs to be. If the user enters an invalid response an error message appears and the user is asked to re-enter the information in the correct format.
    <details><summary>Add Amount of Transaction</summary>
      
    ![Add Amount of Transaction](assets/images/add-expense-amount)
    
    </details>

    <details><summary>Invalid Input</summary>
      
    ![Add Amount of Transaction Invalid Input](assets/images/add_expense_amount_invalid_input)
    
    </details>

    [Back To Top](<#contents>)

    - #### Confirm Expense
      Th user is shown all the information they have entered in the previous 4 steps in a format that is easy to read and understand. The user is asked to confirm if this information is correct. 
      
      If the user chooses 'Y', the worksheet will be updated and the user will receive feedback once it has been successful. 
      
      However, if the user chooses 'N' they will be shown a new menu of choices. They can choose to re-enter the informtion and be taken back to the [add new expense](<#add-new-expense>) process, return to [main menu](<#main-menu>) or choose to confirm the information above. The third option is in case the user mis-typed their answer before.

      If the user inputs in invalid response they will be shown an error message and be asked to enter a valid response.
    <details><summary>Confirm Transaction Page</summary>
      
    ![Confirm Transaction](assets/images/confirm_expense.png)
    
    </details>

    <details><summary>Confirm Transaction Invalid Input</summary>
      
    ![Confirm Transaction Invalid Input](assets/images/confirm_expense_invalid_input.png)
    
    </details>

    <details><summary>Confirm Transaction Page if answered 'N'</summary>
      
    ![Confirm Transaction Page if answered 'N'](assets/images/confirm_expense_no_input.png)
    
    </details>

    [Back To Top](<#contents>)

    - #### Update Worksheet
      Onces the user has been shown the worksheet has been updated successfully, they are shown another menu. They have 2 choices, to add another expense of to return to the main menu. The user will be shown an error message and asked to a valid response if they enter an invalid answer. 

    <details><summary>Worksheet Updated</summary>
      
    ![Worksheet Updated](assets/images/updating_worksheet.png)
    
    </details>

    <details><summary>Worksheet Menu Invalid Input</summary>
      
    ![Worksheet Menu Invalid Input](assets/images/updating_worksheet_invalid_response.png)
    
    </details>

    [Back To Top](<#contents>)

  
  - ### View Statement Menu
    The view statement page displays to the user 3 ways in which they can see their statement: [by date](<#by-date>), [by month](<#by-month>) or [by category](<#by-category>). They are also given the option to return to the [main menu](<#main-menu>) if they enter 'MM'. If the user enters and invalid reponse they will be shown an error message.

    <details><summary>View Statement Menu</summary>
      
    ![View Statement Menu](assets/images/view_statement_menu.png)
    
    </details>

    <details><summary>View Statement Menu Invalid Input</summary>
      
    ![View Statement Menu Invalid Input](assets/images/view_statement_menu_invalid_response.png)
    
    </details>

    [Back To Top](<#contents>)
    
    - #### By Date
      The user is shown all transactions to date in a format that is easy to read and understand. Under all the transactions the user is asked if they would like to return to the [main menu](<#main-menu>) or the [view statement menu](<#view-statement-menu>). If the user enters and invalid response they are shown an error message and asked to enter their response again.

    <details><summary>View Statement By Date</summary>
      
    ![View Statement By Date](assets/images/by_date_top.png)
    
    </details>

    <details><summary>View Statement By Date Menu Invalid Input</summary>
      
    ![View Statement By Date Menu Invalid Input](assets/images/by_date_invalid_response.png)
    
    </details>

    [Back To Top](<#contents>)

    - #### By Month
      The user is shown the total amount they have spent each month. Below there is a choice menu

    <details><summary>View Statement By Month</summary>
      
    ![View Statement By Month](assets/images/by_month.png)
    
    </details>

    <details><summary>View Statement By Month Menu Invalid Input</summary>
      
    ![View Statement By Month Menu Invalid Input](assets/images/by_month_invalid_response.png)
    
    </details>

    [Back To Top](<#contents>)

    - #### By Category
      The user is shown how much they have spent in each category from the beginnning of the year to date.

    <details><summary>View Statement By Category</summary>
      
    ![View Statement By Category](assets/images/by_category.png)
    
    </details>

    <details><summary>View Statement By Category Menu Invalid Input</summary>
      
    ![View Statement By Category Menu Invalid Input](assets/images/by_category_invalid_response.png)
    
    </details>

  
 [Back To Top](<#contents>)

### Future Features

  - Give the user the ability to delete transactions or edit parts of an expense.
  - Give the user the ability to input any income.
  - Generate an automated total for the View Statement By Month page. Currently the site owner has to add the code for every new month after an expense has been added for that month.
  - The ability to login with a username and password to keep data safe and secure.
  - The ability to add more users with the use of multiple google sheets.
  -  Have a budget goals section when the user can set their target spending for each category.
    - To encourage users to meet their target they would be shown a congratulatory message if they succeed. 
    - On the other hand, if the overspend they would be shown an image of a scary, angry clown. The idea for this comes from the name  'Pennywise', being that it is the name of the clown from the movie 'It'.

 [Back To Top](<#contents>)

# Technologies Used

### Languages

The following languages were used to create and develop this website:

* [Python3](https://www.python.org/)

Provided as part of Code Institute's template:

* [HTML5](https://html.spec.whatwg.org/)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

### RFrameworks, Libraries and Packages
* [Google Sheets](https://workspace.google.com/products/sheets/)
* [Gitpod](https://www.gitpod.io/#get-started) 
* [Github](https://github.com/)
* [Gitbash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
* [Heroku](https://dashboard.heroku.com/)
* [GSpread](https://docs.gspread.org/en/latest/)
* [GoogleOAuth](https://developers.google.com/identity/protocols/oauth2)
* [Patorjk](https://patorjk.com/) - used to create the logo, however it had to be edited as was too large for the console.
* [Time](https://docs.python.org/3/library/time.html)
* [Os](https://docs.python.org/3/library/os.html)
* [Sys](https://docs.python.org/3/library/sys.html)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [Tabulate](https://pypi.org/project/tabulate/)
* [Math](https://docs.python.org/3/library/math.html)
* [Colorama](https://pypi.org/project/colorama/) - used to add colour to the terminal.
* [CloudConvert](https://cloudconvert.com/png-to-webp) - used to convert images to  webp.
* [TinyPNG](https://tinypng.com/) - used to optimize images.
* [PEP8](https://peps.python.org/pep-0008/)

 [Back To Top](<#contents>)

# Testing


 [Back To Top](<#contents>)

# Deployment
This site was deployed to GitHub pages. The steps to deploy are as follows:

  1. In the GitHub repository, navigate to the Settings tab. 
  2. Next, navigate to the Pages tab on the left hand side.
  3. Under Source, select main from the Branch dropdown menu. Then click save.
  4. Once the main branch has been selected, the page will automatically be refreshed with a detailed ribbon display to indicate the successful deployment. 

![How To Deploy](https://github.com/bpstephanie/The_Country_Quiz/blob/main/media/deployment.png)

The live link can be found here - https://bpstephanie.github.io/The_Country_Quiz/ 

### **To Fork the Project**

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changes can be made to the copy without affecting the original repository. The steps to fork the repository are as follows:

  1. Log in to GitHub and locate the repository.
  2. On the right hand side of the page, in line with the repository name, is a button called 'Fork', click on the button to create a copy of the original repository in your GitHub Account.
  
![How To Fork](https://github.com/bpstephanie/The_Country_Quiz/blob/main/media/fork.png)

### **To Clone the Project**

The steps to clone a project from GitHub are as follows:

  1. Under the repository’s name, click on the code tab.
  2. Copy the URL under the Clone with HTTPS section.
  3. In an IDE of your choice, open Git Bash.
  4. Change the current working directory to the location of where the cloned directory will be made.
  5. Type 'git clone' then paste the URL copied from GitHub.
  6. Upon pressing enter, the local clone will be created.

![How To Clone](https://github.com/bpstephanie/The_Country_Quiz/blob/main/media/clone.png)

[Back To Top](<#contents>)

## Credits 

* In the get transaction date function: 
    - The code to convert user date input into datetime object was inspired by the following question and answer in [Stack Overflow](https://stackoverflow.com/questions/53248537/typeerror-not-supported-between-instances-of-datetime-datetime-and-str).

* In the get transaction category function: 
    - The code to remove duplicates from a list was inspired by [Data Quest](https://www.dataquest.io/blog/how-to-remove-duplicates-from-a-python-list/).

* In the get transaction description function: 
    - The code to only accept letters was inspired by [Shiksha](https://www.shiksha.com/online-courses/articles/isalpha-method-in-python/#:~:text=The%20isalpha()%20method%20can,entered%20only%20contains%20alphabetic%20characters.)

    - The code to disallow the user from only entering, starting with or ending with whitespace was inspired by the following question and answer in [Stack Overflow](https://stackoverflow.com/questions/68417120/not-allowing-spaces-in-string-input-python)

* In get transaction amount function:
    - The code for rounding user input to 2 decimal places was inspired by the following question and answer in [Stack Overflow](https://stackoverflow.com/questions/51690770/how-to-restrict-user-to-input-only-upto-two-decimal-point-float-numbers-in-pytho)

* In by date function (part of view statement section):
    - The code for sorting the date by date was inspired by [Python Docs](https://docs.python.org/3/howto/sorting.html)



[Back To Top](<#contents>)

### Content

* All of the content was written by myself.

[Back To Top](<#contents>)

## Acknowledgements

Pennywise has been completed as a Portfolio 3 Project, part of the Full Stack Software Developer Diploma at Code Institute. I would like to thank my Code Institute mentor,  Precious Ijege for his advice and support, the Slack community, and everyone at Code Institute for their feedback and guidance. 

Stephanie Bell 2024.

 [Back To Top](<#contents>)