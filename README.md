#**Battleships**

[View the live project here.](https://star-command.herokuapp.com/)

This program is a command-line version of the classic board game Battleships, deployed via the Heroku app. 
It is a single-player version of the game, playing against a computerised player. 

---

![Heroku](docs/screenshots/heroku.png)

___

##**Table of Contents**
* [**Battleships**](#battlehips)


## Features

-   Responsive on all device sizes

-   Interactive elements




### Languages 

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries 

    For this project to work successfully, I used the following imported libraries:

1. random:
    - randint used to generate a random integer between 0 and 9 for automated placement of craft and the computer hit guess.

1. time:
    - importing the sleep function from the this library enabled me to delay the typed reposnse to the console for a nicer game flow. It also enabled certain hit or miss statements to be viewed before the terminal was cleared for the reprinting of the boards. 

1. string:
    - I used the ".capwords()" function when a User enters their name to give them correct casing. 

1. os:
    - Used to clear the terminal so the screen could reset between input and keep everything clean.

---

## Testing

PEP8 online [(here)](http://pep8online.com/) was used to run through and check code met all validations and conventions. All pages passed with no issues, except for the "no newline at end of file" warning which is a known issue with this particualr CI template that I am using. 

---


### Further Testing

-   The app was tested on Google Chrome, Firefox, Microsoft Edge and Safari browsers.
-   A large amount of testing was done to ensure that functionality was working as expected.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-  If the User inputs their coordinates whilst it is the Computer's turn, their choice will still register. This will either result in an 'automatic' shot when it comes to their turn, or if they type more digits, a validation error. 

### Improvements

-   I would like to implement addditional difficulty AI settings using a checkerboard technique for initial placement [(view)](https://www.youtube.com/watch?v=jMpbYpaKtao&ab_channel=KeithGalli), and an awareness to take shot at surrounding tiles once they have a hit. 
-   A 2-player functionality. 
-   The introduction of more colours in the game, with craft, hits and misses all being a different colour.

---
  
# **Deployment**

## ***Playing on a Local machine or via Gitpod Terminal:***
This project was developed by forking a [specialized Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser. Due to this, I optimized the game to work via the [final Heroku deployment](https://dnlbowers-battleship.herokuapp.com/), and I do not recommend playing it locally. That said, I have included this section to give you a choice.  

1. Navigate to the [GitHub repository](https://github.com/dnlbowers/battleships), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.   
   
   * **Gitpod** only **requires** you to have the **web extension** installed and **click** the **green Gitpod button** from the repositories main page. If you are **using Gitpod** please **skip step 2** below as you do not require a virtual environment to protect your machine.  
  
1. **Create** the **virtual environment** with the terminal command **"python3 -m venv venv".** Once complete add the "venv" file to you're ".gitignore" file and use the terminal command **"venv\Scripts\activate.bat" to activate it.**
   
   * ***IMPORTANT*** If developing locally on your device, ensure you **set up/activate the virtual environment before installing/generating the requirements.txt file**; failure to do this will pollute your machine and put other projects at 
 
1. **Install the requirements** listed in requirements.txt using the terminal command  **"pip3 install -r requirements.txt"**
   * Kindly note that since I developed the project from scratch and installed the required libraries as progressed **I have already included a requirements.txt for this app** by using the terminal command **"pip3 freeze > requirements.txt"** to generate it.

## ***Final Deployment to Heroku:***  
  
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
1. **Log in to Heroku** or create an account if required.
1. **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
1. From the drop-down menu **select "Create new app"**.
1. **Enter a unique app name**. I combined my GitHub user name and the game's name with a dash between them (dnlbowers-battleship) for this project.
1. Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Malta.
1.  When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
1. This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
1. **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
1. Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
1. **Repeat step 11 but** this time **add "node.js" instead of python**. 
   * ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
1. Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
1. From the deploy tab **select Github as the deployment method**.
1. **Confirm** you want to **connect to GitHub**.
1. **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
1. From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   * Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   * Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 
---

# **Credits**
* Everything you need to know about Classes in Python by Keith Galli was an extremely useful resource for me - [Here](https://youtu.be/tmY6FEF8f1o) 
* The idea to decorate the board with numbers for indexing the shots was from [Knowledge Mavens youtube channel](https://youtu.be/alJH_c9t4zw)
* Clear console function came from [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/)
* [lucid chart.com](https://www.lucidchart.com/) was used to create the logic flow chart "flowchart.jpeg"
* [ASCII Art text generator](http://www.network-science.de/ascii/) used for the welcome screen text.
* To understand the game logic and how to go ahead with the build, I used this video on the [Devpost Youtube channel](https://youtu.be/zSQIGzmcp2I)  
* To better understand the enumerate() and zip() fucntions I came to [nkmk](https://note.nkmk.me/en/python-for-enumerate-zip/)


# **Code**

-   The idea for the project was inspired by a video by [Robert Heaton](https://www.youtube.com/watch?v=Gi0Fdyhk1_0&t=616s&ab_channel=RobertHeaton)

### Content

-   All content was written by the Author, Matt Cooper, except where commented in the code or mentioned above. 


### Acknowledgements

-   My Mentor Antonio Rodriguez for his continuous helpful feedback.

-   My partner Mor for her testing, suggestions and support throughout this build. 

-   The tutors at Code Institute for assisting me at the midnight hour of submission. 




## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

