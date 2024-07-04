# Pennywise
budget tracker explanation

Welcome to <a href="https://pennywise-budget-tracker-ce1c05dc8133.herokuapp.com/">Pennywise</a>


![Responsive Mockup](media/responsive-mockup.png)

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
    * [Welcome Message Modal](#welcome-message-modal)
    * [How To Play Modal](<#how-to-play-modal>)
    * [Main Game Page](<#main-game-page>)
    * [Main Heading](<#main-heading>)
    * [Home Button](<#home-button>)
    * [Username](<#username>)
    * [Start Game Button](<#start-game-button>)
      * [Restart Button](<#restart-button>)
    * [Main Game Area](<#main-game-area>)
      * [Question Counter](<#question-counter>)
      * [Question Area](<#question-area>)
      * [Answer Buttons](<#answer-buttons>)
      * [Score Area](<#score-area>)
    * [Footer](<#footer>)
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

### Design Choices

 - ### Typography
   Due to Pennywise being a terminal based application, no specific typography has been used. The standard font is being used in the terminal.

 - ### Colour Scheme
   Pennywise is back-end program therefore not much styling or visual design has been implementes. 

   * [Ansi](https://pypi.org/project/ansi/) library for Python was used to add colour to the program to give visual feedback to the user.
   

 [Back To Top](<#contents>)

# Features
  ## Existing Features

  - ### Welcome Message Modal
    When the user first enters the site, a welcome message modal appears with two buttons, the 'How To Play' button which takes the user to the instructions for the quiz and the 'Let's get Started' button which closes the modal and takes the user to the [Main Game Page](<#main-game-page>).

    Welcome Message Modal Desktop:\
    ![Welcome Message Modal Desktop](media/site-screenshots/welcome-modal.png)

    Welcome Message Modal Mobile:\
    ![Welcome Message Modal Mobile](media/site-screenshots//welcome-modal-mobile.png)

  - ### How To Play Modal
    This modal gives instructions to the user on how to play the quiz. When exiting this pop-up they will be taken back to the [Welcome Message Modal](<#welcome-message-modal>).

    How To Play Modal Desktop:
    ![How To Play Modal Desktop](media/site-screenshots/howtoplay-modal.png)

    How To Play Modal Mobile: \
    ![How To Play Modal Mobile](media/site-screenshots/howtoplaymodal-mobile.png)

  - ### Main Game Page
    - #### Main Heading
      A large stylized font which is fully responsive to different screen sizes.

      Desktop Main Heading:
      ![Main Heading Desktop](media/site-screenshots/main-heading.png)

      Mobile Main Heading:\
      ![Main Heading Mobile](media/site-screenshots//main-heading-mobile.png)
    
    - #### Home Button
      The home button will take the user back to the welcome message modal where that can access the instructions. 

      ![Home Button](media/site-screenshots/home-button.png)

    - #### Username 
      In order for a user to play the quiz, a username must be entered. The username has to be 3 - 10 characters long and must be letters.

      Username Desktop:
      ![Username Area Desktop](media/site-screenshots/username.png)

      Username Mobile: \
      ![Username Area Desktop](media/site-screenshots/username-mobile.png)

      Invalid Username Alert: \
      ![Invalid Username Alert](media/site-screenshots/invalid-username.png)

    - #### Start Game Button
      Once a username has been entered, a good luck message is shown and the 'Start' Button appears for the user to begin.

      Successful Username Input Message and Start Button: 
      ![Successful Username Input Message and Start Button](media/site-screenshots/successful-input.png) 

      Button Hover Effect:\
      ![Button Hover Effect](media/site-screenshots/button-hover.png)

      - ##### Restart Button
        Once the start button has been pressed, the text changes to 'Restart. This allows the user to restart the game any time they want. Once pressed, the score board and question counter will reset and a new set of random questions will be allocated to the round.

        Restart Button:\
        ![Restart Button](media/site-screenshots/restart-button.png)

    - #### Main Game Area

      Main Game Area Desktop:\
      ![Main Game Area Desktop](media/site-screenshots/game-area-desktop.png)

      Main Game Area Mobile: \
      ![Main Game Area Mobile](media/site-screenshots/game-area-mobile.png)

      The main game area consists of 4 parts:

      - ##### Question Counter 
        It will display 0/10 until the user starts the quiz. For every question that appears on screen, the counter will increase by 1 until it reaches 10, this has been generated through JavaScript.

      - ##### Question Area 
        It is generated from a JavaScript array. The questions are chosen randomly out of a possible 50 questions. When the user has finished their quiz, a final 'Well done' or 'Bad luck' message appears depending on the score of the user. Six questions and above correct out of ten warrants the user a well done message, five correct answers and below receive a bad luck message.

        Well Done Message:
        ![Well Done Message](media/site-screenshots/well-done.png)

        Bad Luck Message:
        ![Bad Luck Message](media/site-screenshots/bad-luck.png)

      - ##### Answer Buttons
        Each of the answer buttons display the name of the country they represent as well as the flag. The flag was chosen as the background for more visual users and is faded out to improve contrast and readability.

        The answer buttons have a hover effect when the user moves their mouse over them. If the correct answer is chosen, the text and border will highlight green for two seconds, if the incorrect answer is chosen, the text and border will highlight red for two seconds. In both cases there is also a corresponding sound.

        After much consideration, it was decided not to highlight the correct answer if the user gets the answer wrong. This was chosen to allow the user to play the quiz more times until they get the answer correct.

        Correct Answer Visual Feedback:
        ![Correct Answer Visual Feedback](media/site-screenshots/correct-answer.png)

        Incorrect Answer Visual Feedback:
        ![Incorrect Answer Visual Feedback](media/site-screenshots/incorrect-answer.png)

      - ##### Score Area
        The score area tracks both the number of correct answers and incorrect answers.

    - #### Footer
      The footer consists of two links to the LinkedIn and GitHub profiles of myself, respectively.
      ![The Footer](media/site-screenshots/footer.png)
  
 [Back To Top](<#contents>)

### Future Features

  - Have difficulty levels, ranging from easy to expert.
  - Have a high score functionality for users to play many times and track their scores.
  - Have different topics, for example, a quiz on the countries in Africa or Asia.

 [Back To Top](<#contents>)

# Technologies Used

### Languages

The following languages were used to create and develop this website:

* [HTML5](https://html.spec.whatwg.org/) - provides the content and structure for the website.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - provides the styling.
* [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript) - provides the responsive quiz elements.

### Resources and Tools
* [Balsamiq](https://balsamiq.com/wireframes/)
* [Gitpod](https://www.gitpod.io/#get-started) 
* [Github](https://github.com/)
* [Favicon](https://favicon.io/)
* [DevTools](https://developer.chrome.com/docs/devtools)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [Am I Responsive](https://ui.dev/amiresponsive)
* [CloudConvert](https://cloudconvert.com/png-to-webp)
* [TinyPNG](https://tinypng.com/)

 [Back To Top](<#contents>)

# Testing
Please refer [**_here_**](TESTING.md) for more information about testing on The Country Quiz.

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

* Wireframes: [Balsamiq](https://balsamiq.com)
* Favicon: [Favicon](https://favicon.io/)
* Fonts: [Google Fonts](https://fonts.google.com/)
* Icons: [Fontawesome](https://fontawesome.com/)
* Colour Palettes: [Coolors](https://www.bbcgoodfood.com/)
* Mock-up: [Am I Responsive](https://ui.dev/amiresponsive)
* Chrome for Developers: [Dev Tools](https://developer.chrome.com/docs/devtools)

* The code to create the modals was inspired by [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp).
* The code to implement audio in JavaScript  by [Noah Ekin](https://noaheakin.medium.com/adding-sound-to-your-js-web-app-f6a0ca728984).
* This YouTube tutorial was followed for the basic setup of the quiz [James Q Quick](https://www.youtube.com/watch?v=zZdQGs62cR8&list=PLDlWc9AfQBfZIkdVaOQXi1tizJeNJipEx&index=4).
* The code to randomize quiz questions was inspired by [She Codes](https://www.shecodes.io/athena/10246-how-to-show-random-questions-in-a-quiz-using-javascript).
* The code for the score area was inspired by the Code Institute Love Maths Project.

[Back To Top](<#contents>)

### Content

* The majority of the quiz question and answer content came from myself. A few questions were fact checked with [Visit South America](https://visitsouthamerica.co/)


[Back To Top](<#contents>)

### Media

The images are from [Pixabay](https://pixabay.com/) and [Flag Colour Codes](https://www.flagcolorcodes.com/).

The llama graphic is from [Pixabay](https://pixabay.com/) and I created the background in [Canva](https://www.canva.com/).

The flag images were made opaque with [OnlinePNGTools](https://onlinepngtools.com/change-png-opacity#:~:text=World's%20simplest%20online%20Portable%20Network,%2C%20quick%2C%20and%20very%20powerful.).

The images were optimised with [Tinypng](https://tinypng.com/).

[Back To Top](<#contents>)

## Acknowledgements

The Country Quiz has been completed as a Portfolio 2 Project, part of the Full Stack Software Developer Diploma at Code Institute. I would like to thank my Code Institute mentor,  Precious Ijege for his advice and support, the Slack community, and everyone at Code Institute for their feedback and guidance. 

Stephanie Bell 2024.

 [Back To Top](<#contents>)