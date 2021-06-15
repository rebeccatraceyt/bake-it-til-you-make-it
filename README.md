<h1 align="center">
     <a href="https://github.com/rebeccatraceyt/bake-it-til-you-make-it" target="_blank"><img src="https://i.ibb.co/jfFtJNB/logo-readme.png" alt="Bake It 'Til You Make It tagline"></a>
</h1>
<div align="center">

<strong><em>Bake It 'Til You Make It</em></strong> is a community-based web application for those who love the art of baking to search and share their favourite creations.

Inspired by the old-school baking book (filled with scrap paper and notes), the application features hand-drawn graphics and fonts designed to bring the users back to a time of scribbled recipes, in a more organised fashion, through a simplistic and intuitive user interface. 

The recipe database encourages users to create an account that will allow them to upload and store their favourite baking recipes as well as find new inspiration from other users, saving their favourites for later.

[View the live project here](https://bake-it-til-you-make-it.herokuapp.com/)

</div>

## Table of contents
1. [UX](#UX)
    1. [Project Goals](#Project-Goals)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
2. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
3. [Issues and Bugs](#Issues-and-Bugs)
4. [Information Architecture](#Information-Architecture)
5. [Technologies Used](#Technologies-Used)
     1. [Languages](#Languages)
     2. [Tools](#Tools)
     2. [Libraries](#Libraries)
6. [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
7. [Deployment](#Deployment)
     1. [1. Database Creation](#1-Database-Creation)
     2. [1. Local Copy Creation](#2-Local-Copy-Creation)
     3. [1. Heroku App Creation](#3-Heroku-App-Creation)
8. [Credits](#Credits)
9. [Acknowledgements](#Acknowledgements)
***

![Bake It 'til You Make It Responsiveness](assets/readme-files/responsive.png)

***

## UX 
### Project Goals
The primary goal of **Bake It 'Til You Make It** is to provide a web-based application, that is simplistic and intuitive in design, that allows users to create, search, save and share their favourite baking recipes on a database.

This is the third of four Milestone Projects that the developer must complete during their Full Stack Web Development Program at The Code Institute. 

The main requirements were to build a full-stack website allowing users to manage a common dataset (in this instance, baking recipes) using **HTML5**, **CSS3**, **JavaScript**, **Python**, **Flask** and **MongoDB**.

#### User Goals
The user is looking for:
- A searchable database to locate recipes of their choice.
- A easy-to-use user management system with **CRUD** conventions to:

    - Create a user account.
    - See their user information, as applicable.
    - Edit their user account.
    - Delete their user account.

- A easy-to-use dataset management system with **CRUD** conventions to:

    - Create recipes.
    - Read recipe dashboards.
    - Edit their own recipe creations.
    - Delete their own recipe creations.

- A intuitive and aesthetically pleasing interface.

#### Developer / Site Owner Goals
The Developer is looking to:

- Create an inviting, community-drive application that they themselves would use to share their passion for baking.
- Demonstrate their proficiency in a variety of software development skills, using newly learned languages and libraries as well as a document database system.
- Deploy a project they are proud and excited to have on their portfolio.


### User Stories
**As a General User, I want to:**

1. Intuitively find recipes on the database. 
2. View the selected recipe's dashboard to get necessary information.
3. Seek contact information to send useful feedback to Developer / Site Owner.

**As a Non-Registered User, I want to:**

1. Navigate to Sign-Up page to Register an account.

**As a Registered User, I want to:**

1. Log into my account to gain access to the full functionality of the site.
2. Navigate to my user profile to edit my account information.
3. Navigate to my account settings to delete my account information.
4. Navigate to my recipes page to view my uploaded recipes.
5. Navigate to upload page to add my recipe to the database.
6. View my own recipe's dashboard to edit recipe as needed.
7. View my own recipe's dashboard to delete recipe.
8. Use a save function to save my favourite recipes from other users.
9. Navigate to my favourites page to view the recipes I have saved from other users.

**As an Administrative Account holder, I want to:**

1. View **any** recipe dashboard to edit recipe as needed.
2. View **any** recipe dashboard to delete recipe as needed.
3. Still maintain a save function to save my favourite recipes from other users.

### Development Planes

In order to design and create a web-based interactive application, the developer distinguished the required functionality of the site and how it would answer the user stories, as described above, using the **Five Development Planes**:

<strong>1. <u>Strategy</u></strong>

Broken into three categories, the website will focus on the following target audiences:
- **Roles:**
     - Bakers of all levels
     - New Users **(Non-Registered)**
     - Return Users **(Registered)**

- **Demographic:**
     - Passion for baking
     - Food lovers
     - All ages (encouraging family fun-time)

- **Psychographics:**
     - Personality & Attitudes:
          - Organised
          - Creative
     - Values:
          - Community
          - Nostalgia
     - Lifestyles:
          - Food interests
          - Outgoing

The website needs to enable the **user** to:
- Register/Login to an account
- Search Recipe database by:
    - Name
    - Category
    - Level
- View Recipe Dashboard with the following information:
    - Name
    - Image URL
    - Description
    - Category
    - Serving Size
    - Time
    - Level
    - Ingredients
    - Directions
- Upload and access their own recipes
- Save and access their favourite recipes from other users
- Get in contact with site owner

The website needs to enable the **client** to:
- Provide a community-driven recipe database
- Use the website themselves:
    - Share their favourite recipes
    - Find new recipes
    - Connect with a community that shares their interests
    - Have control of the recipes shared
- Allow for user feedback and suggestions

With these goals in mind, a strategy table was created to determine the trade-off between importance and viability with the following results:

**Strategy Table for User Management:**
![Strategy Table for User Management](static/images/readme-files/user-management-st.png "User Management Strategy Table")

**Strategy Table for Baking Respository Management:**
![Strategy Table for Baking Respository Management](static/images/readme-files/baking-repo-st.png "Baking Repository Strategy Table")

<strong>2. <u>Scope</u></strong>

A scope was defined in order to clearly identify what needed to be done in order to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
        - Customisable account
            - Custom Username/Password
            - Upload their own recipes
            - Save favourite recipes
        - Easy Navigation
        - Aesthetic theme (typography, imagery, colour palette)
        - Recipe dashboard:
            - Name
            - Image URL
            - Description
            - Category
            - Serving Size
            - Time
            - Level
            - Ingredients
            - Directions
        - Searchable database system
        - Developer contact information
- **Functionality Requirements**
     - The user will be able to:
        - Register/Login to account
        - Customise their profile
            - Custom Username/Password
            - Upload their own recipes
            - Save favourite recipes
        - Navigate to recipes:
            - Search by name, category or level
            - My Recipes Page
            - My Favourites Page
        Create recipes:
            - Tags
            - Image Url
            - Ingredients
            - Directions
        - Get in contact with the Developer

<strong>3. <u>Structure</u></strong>

The information architecture was organized in order to ensure that users could navigate through the site with ease and efficiency, with the following results: 

**Information Architecture for User Management:**
![Information Architecture for User Management](static/images/readme-files/user-management-ia.png "User Management Information Architecture")

**Information Architecture for Baking Respository Management:**
![Information Architecture for Baking Respository Management](static/images/readme-files/baking-repo-ia.png "Baking Repository Information Architecture")

<strong>4. <u>Skeleton</u></strong>

Wireframe mockups were created in a [Figma Workspace]( "Link to Bake It Figma Workspace") with providing a positive user experience in mind:

- Home Page:

     ![Strategy Table for Baking Respository Management](static/images/readme-files/.png "Baking Repository Strategy Table")


<strong>5. <u>Surface</u></strong>


- <strong>Colour Scheme</strong>

     - The chosen colour scheme was specifically selected in order to define the tone of the application.

     - Drawing from research conducted on food-related imagery and online sites, a colour palette was developed to create an ambient and familiar environment throughout the site.

     - The selected colours are widely used in baking (e.g. in icing and decoration) and, therefore, reflects a sense of nostalgic familiarity.

          ![Colour Palette](static/images/readme-files/palette.png "Colour Palette")


- <strong>Typography</strong>

     - The primary font chosen is [Work Sans](https://fonts.google.com/specimen/Work+Sans "Link to Work Sans Google Fonts page"). A sans-serif typeface, Work Sans is simplistic in design and optimised for screen display, making it easily readable.

        ![Work Sans Typeface Example](static/images/readme-files/worksans-ex.png "Work Sans Typeface Example")

     - The Secondary font (accent font) chosen is [Indie Flower](https://fonts.google.com/specimen/Indie+Flower "Link to Indie Flower Google Fonts page"). A handwritten script typeface, it has bubbly, rounded edges to emphasis the homely-handmade recipe book nostalgia.

        ![Indie Flower Typeface Example](static/images/readme-files/indieflower-ex.png "Indie Flower Typeface Example")

     - The charismatic combination of the two typefaces compliments the soft and familiar theme set by the colour palette and overall appearance of the site.

- <strong>Imagery</strong>

     - The imagery used was created by the developer using the application [Procreate](https://procreate.art/) in order to create a consistency of the elements while maintaining the look and feel of the application.

[Back to top ⇧](#table-of-contents)

## Features

### Design Features
Each page of the game features a consistently responsive and intuitive navigational system:
- There is a conventionally placed **Logo** on the top-left of each page. Clicking on the logo will redirect players back to the home page.
- To ensure the player has full control of the game, there are two **Toggle** functions conventionally located at the top-right corner of each page. These allow the users to control the sound and page theme to their preference.
- On larger screens, the **Footer** is conventionally placed at the bottom of the screen, allowing users to navigate to the social icon of their choosing.
- On smaller screens, the **Footer** is placed within a sliding function, where users can click the appropriate icon in order to reveal the footer. This was to ensure that the footer would not interfere with the game-play.

<dl>
     <dt>
          <a href="https://rebeccatraceyt.github.io/WhatTheBlank/" target="_blank" alt="Blank! Home Page">Home Page</a>
     </dt>
     <dd>
          There is a conditional class in place that determines what content the user will see when they enter the website. Based on whether the user has already provided a <strong>Player Name</strong>, the user will see one of the following:
               <ul>
                    <li>
                         <strong>Welcome Menu</strong> - A full-screen welcome menu, introducing the user to the game, providing the basics in how the game works and prompting them to enter a player name of their choice. 
                    </li>
                    <li>
                         <strong>Home Page</strong> - When the user has entered their chosen name, or if they have previously already entered this information, the user will see the home page. Again, a full-screen page, the home page provides a point of navigation for the players to start the game in the category of their choosing.
                    </li>
               </ul>
     </dd>
</dl>

### Existing Features
- **EXAMPLE** - 

### Features to Implement in the future
- **EXAMPLE** - 

[Back to top ⇧](#table-of-contents)

## Issues and Bugs 
The developer ran into a number of issues during the development of the websites, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

**Base.html** <br>
The `base.html` page uses Jinja templates in order to extend its components (e.g. page design, `navbar` & `footer`) to all other pages. In trying to implement an pseudo `active` class on the anchor links in the navigation bar, an issue arose where the special state would be applied to all links, not just the active link. It was through a post of a similar problem on [Stack Overflow](https://stackoverflow.com/questions/29902575/highlight-menu-item-based-on-current-view "Solution to problem on Stack Overflow") that the developer found a solution, using `block` elements for each class.

**Home Page** <br>
- On the recipe card panel of the Homepage, there was a styling issue with the `ul` element whereby the `li` elements nested would not conform to the styling that was needed to be readable. The `li` elements, due to the Bootstrap styling, would only display in a `inline` format, which caused padding issues within the card. In order to avoid this, and to maintain the design, the `ul` was removed and replaced with Bootstrap grid styling. This was done after researching similar issues.
- The Homepage uses a Bootstrap Carousel feature to highlight the four latest baking recipes added to the database. An issue arose with the carousel whereby only one recipe would be called on repeat. In their endless Google searching, the developer found a helpful article on [Zhishibo.com](http://www.zhishibo.com/articles/30623.html "Solution to problem on Zhishibo") that recommended using a `loop.index` method on the `active` class of the carousel in order to loop through the latest recipes.

**Edit User Page** <br>
- In creating the edit functionality on the `edit_user.html`, the initial code used was `update_one` in order to change the user information. A problem arose because the developer wanted only select user information to change but, in using `update_one`, the entire collection changed and the fields that the developer did not allow to change would be wiped from the system and cause value errors. In looking for solutions, the developer found a similar issue on [Stack Overflow](https://stackoverflow.com/questions/30605638/why-does-upsert-a-record-using-update-one-raise-valueerror "Solution to problem on Stack Overflow") that suggested using `replace_one` as an alternative, with the `upsert` equal to `True` in order to update the specified fields only.
- In order to make the `edit_user.html` functionality more user-friendly, the developer tried to create a possibility that the user would not have to change their password if they did not wish to (e.g. if they only wanted to change their user image). The problem with this was that should the user leave the password field blank (choosing not to change it), it would automatically change the users password to 'blank' on the database. This was insufficient and in no ways user-friendly, so the developer researched other methods. Their first thought was to use the user's password value as the default value for the field but, as the password is hashed and salted using `werkzeug.security`import, this would not work. The alternative, and the conclusive solution, was to create a separate accounts settings page, where the user has the freedom to change their password or delete their account.

**Pagination** <br>
In implementing the pagination functionality, a linting error was raised in the terminal due to the developer using the `Pylint` extension in their IDE. The message was:

```
"owner": "python",
"code": "unbalanced-tuple-unpacking",
"severity": 4,
"message": "Possible unbalanced tuple unpacking with sequence defined at line 237 of flask_paginate: left side has 3 label(s), right side has 2 value(s)",
"source": "pylint",
"startLineNumber": 32,
"startColumn": 5,
"endLineNumber": 32,
"endColumn": 5
```
In order to avoid this error, the developer installed and selected `Flake8` to lint through `app.py`.

[Back to top ⇧](#table-of-contents)

## Information Architecture

[Back to top ⇧](#table-of-contents)

## Technologies Used
### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://www.python.org/ "Link to Python Homepage")

### Tools
- [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/ "Link to download Visual Studio Code Insiders") 
     - VSCode was used as the preferred IDE.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control to commit to Git and push to Heroku.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project repository, after pushing.
- [Figma](https://www.figma.com/ "Link to Figma homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to validate the responsiveness of the design throughout the process, and to generate mockup imagery to be used.
- [Procreate](https://procreate.art/ "Link to ProCreate homepage")
     - Procreate was used to create and edit images as well as using the colour picker tool to ensure consistency throughout.
- [Imgbb](https://imgbb.com/ "Link to Imgbb site") 
     - ImgBB was used to externally host images used.


### Libraries
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [jQuery](https://jquery.com/ "Link to jQuery page")
     - jQuery was used to simplify the JavaScript code used.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts "Indie Flower" and "Work Sans" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons for UX purposes.
- [jQuery Validation](https://jqueryvalidation.org/ "Link to jQuery Validation page")
     - jQuery Validation was used to simplify form validation for the **Suggestions Form**.
- [SweetAlert2](https://sweetalert2.github.io/ "Link to Sweet Alert 2 page")
     - SweetAlert2 was used to customise the **Suggestions Form** success message for UX purposes.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Link to Flask Homepage")
     - Flask was used as the web framework for the application.
- [PyMongo](https://pypi.org/project/pymongo/ "Link to PyMongo information")
     - `flask_pymongo` was used a communication line between the MongoDB database and Python.
- [Pagination](https://flask-paginate.readthedocs.io/en/master/ "Link to flask-paginate documentation")
     - `flask_paginate` extension was used to implement pagination functionality on select pages. 
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information")
     - Jinja templating language was used to simplify and display backend data in html.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information")
     - Werkzeug was used for password hashing and authentication.

[Back to top ⇧](#table-of-contents)

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment
To further develop this project, a clone can be made using the following steps:
### 1. Database Creation
The application is connected to a [MongoDB Atlas](https://mongodb.com/ "Link to MongoDB Homeapage") Cluster. A Project database can be created using the following steps:

1. Log into [MongoDB](https://account.mongodb.com/account/login "Link to MongoDB login page") or [create an account](https://account.mongodb.com/account/register "Link to MongoDB sign-up page").
2. Locate and select the `New Project` button on the right side of the page, and give your project a name. Navigate to the project page.
3. Locate and select the `Create a New Cluster` button on the right side of the page. Once selected:
     - Choose **Shared Cluster** which is a free option.
     - Select your **Cloud Provider** and **Region** (in this instance: **AWS** and **Ireland**).
     - Click on **Cluster Tier** and select tier of preference (in this instance: **Basic M0 tier**).
     - Click on **Cluster Name** and create your cluster name.
4. Locate and select `Database Access` on the left side of the page. Once selected, click `Add New Database User`:
     - Choose `Password` for the **Authentication Method**
     - Enter a username and password of your choosing
     - Ensure `Read and write to any database` is selected in **Database User Privileges**
     - Add User
5. Locate and select `Network Access` under `Database Access` on the left side of the page. Once selected, click `Add IP Address`:
     - Select `Allow Access from anywhere` (This is not recommended for full-production applications).
     - Select `Confirm`.
6. Locate and select `Clusters` on the left side of the page (must be provisioned first).
7. Click `Collections`, then `+ Create Database` to start adding documents to your database collections:
     - Enter chosen `Database Name`
     - Enter chosen `Collection Name`
     - Select `Create`
8. Click `Create Collection` and create the necessary collections. See [Information Architecture](#Information-Architecture) for reference of the collections created for this project.

### 2. Local Copy Creation
A Local Clone of the repository can be made in two ways:

- **Forking the Repository:**

     By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. At the top of the repository, on the right side of the page, select "Fork".
     4. You should now have a copy of the original repository in your GitHub account.

-  **Creating a Clone**

     How to run this project locally:
     1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
     2. After installation, restart the browser.
     3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     5. Click the green "GitPod" button in the top right corner of the repository.
     This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

     How to run this project within a local IDE, such as VSCode:

     1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
     2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to GitHub Repo").
     3. Under the repository name, click "Clone or download".
     4. In the Clone with HTTPs section, copy the clone URL for the repository.
     5. In your local IDE open the terminal.
     6. Change the current working directory to the location where you want the cloned directory to be made.
     7. Type 'git clone', and then paste the URL you copied in Step 3.
     ```
     git clone https://github.com/USERNAME/REPOSITORY
     ```
     8. Press Enter. Your local clone will be created.

     (Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting"))

Once a local clone is created, the environment variables have to be set:

1. Create a `.gitignore` file in the project's root directory.
2. In the terminal window, type `touch env.py` to create the file that will contain the environment variables. 
3. Add `env.py` to the `.gitignore` file.
4. Within the `env.py` file, enter the project's environment variables:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", <your_secret_key>)
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority" )
os.environ.setdefault("MONGO_DBNAME", <your_mongo_db_name>)
```
For the `MONGO_URI` ensure to replace `<username>`, `<password>`, `<cluster_name>` and `<database_name>` with the appropriate alternatives.



### 3. Heroku App Creation
The website requires back-end technology, including a server, application and database. It is because of this that the project was deployed on **Heroku**, a container-based cloud Platform as a Service. There are two ways to deploy on Heroku:

- Using the Heroku Command Line Interface
- Connect to GitHub Repository (the developer recommends this method)

Before deployment can be carried out on Heroku, the following steps must be carried out:

1. Create a `requirements.txt` file to install all requirements. In the terminal window, type the following command:
```
pip3 install -r requirements.txt
```
2. Create a `Procfile` file so that Heroku knows which file runs the app. In the terminal window, type the following command:
```
echo web: python app.py > Procfile
```
*Remove the blank line that may occur at the end of the Procfile to avoid any issues*


3. Push the two files to the repository:
```
git add requirements.txt
git commit -m "Add requirements.txt"

git add Procfile 
git commit -m "Add Procfile"

git push
```
Once these steps are completed, continue with the process:

1. Log into [Heroku](https://id.heroku.com/login "Link to Heroku login page") or [create an account](https://signup.heroku.com/login "Link to Heroku sign-up page").
2. Select the `New` button on the top-right of the page, and choose `Create New App`. Give your app a unique name and set the region (in this instance: **Europe**). Then click `Create App`.
3. Navigate to the `Deploy` tab on the dashboard and select `Connect to GitHub`.
4. Search for the repository name (ensuring it is spelled correctly). Once located, click `Connect`. 
5. Navigate to the `Setting` tab on the dashboard and select `Reveal Config Vars`, entering the necessary key/values as below:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | `<your_secret_key>`
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
MONGO_DBNAME | `<your_mongo_db_name>`

6. Navigate back to the `Deploy` tab and scroll down to `Automatic Deploys`.
7. Ensure that the `master` branch is selected, then select `Enable Automatic Deploys`.

Heroku will receive the pushed code from the GitHub repository and host the application with the required packages set out. 

The deployed version can now be viewed by selecting `View App` in the top-right of the page.


[Back to top ⇧](#table-of-contents)

## Credits 
The developer consulted multiple sites in order to better understand the code they were trying to implement. For code that was copied and edited, the developer made sure to reference this within the code. The following sites were used on a more regular basis:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [JSfiddle](https://jsfiddle.net/ "Link to JSfiddle page")

[Back to top ⇧](#table-of-contents)

## Acknowledgements
- I would like to thank my mentor Seun for her unwavering encouragement and guidance throughout.
- I would like to thank my family and friends for their never-ending encouragement and valued opinions during the entire process of development.

[Back to top ⇧](#table-of-contents)

***