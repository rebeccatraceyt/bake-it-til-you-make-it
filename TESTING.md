<h1 align="center">
     <a href="https://bake-it-til-you-make-it.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/jfFtJNB/logo-readme.png" alt="Bake It 'Til You Make It"></a>
</h1>

<h1 align="center"> Testing </h1>

[Main README.md file](README.md "Link to README file")

[View live project](https://bake-it-til-you-make-it.herokuapp.com/ "Link to Live project")

[View project Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to Repository")

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
     - [Lighthouse Auditing](#Lighthouse-Auditing)
4. [User Testing](#User-Testing)

***

![Bake It 'til You Make It Responsiveness](assets/readme-files/responsive.png)

***

## Testing User Stories

**General User**

1. As a General User, I want to intuitively find recipes on the database. 
    - On all pages, the **Find a Recipe** page is visible.
    - Clicking the **Find a Recipe** page, users will be able to view all recipes.
    - Using the search bar allows users to pinpoint their search.
    - Using the dropdown menu allows the user to refine their search.
2. As a General User, I want to view the selected recipe's dashboard to get necessary information.
    - Clicking either the **Recipe Image** or **Recipe Name** will direct the user to the recipe page.
    - There, all information pertaining to the recipe can be found.
3. As a General User, I want to seek contact information to send useful feedback to Developer / Site Owner.
    - On all pages the **Footer** is visible.
    - Selecting one of the **social** icons directs the user to:
        - The Developers LinkedIn page.
        - The Developers GitHub page.
        - The Contact Modal.

**Non-Registered User**

1. As a Non-Registered User, I want to navigate to Sign-Up page to Register an account.
    - A Non-Register User can click the **Sign Up** button on the **Home Page** or in the **Navigation Links** to be directed to the **Sign Up Page**.
    - There, they can enter their details and submit their registration.
    - On registering, they will be directed to the **My Recipes Page**.

**Registered User**

1. As a Registered User, I want to log into my account to gain access to the full functionality of the site.
    - Users can click the **Login** button on the **Home Page** or in the **Navigation Links** to be directed to the **Login Page**.
    - There, they can enter their login details.
    - On Login, they will be directed to the **My Recipes** page.
    - The conditional links will allow the user the full functionality of the site (Create, Read, Update, Delete).
2. As a Registered User, I want to navigate to my user profile to edit my account information.
    - On **My Recipes Page**, **My Favourites Page** and the user **quicklinks dropdown menu** (on larger screens only), the user can navigate to the **Edit Profile** page.
    - There, they can edit their account details (**username** and **image**).
    - Their current details will be the default values.
    - On clicking **Save**, they will be directed to **My Recipes**.
    - On clicking **Cancel**, they will be directed to **My Recipes**.
    - On clicking **Account Settings**, they will be directed to the **Edit Account** page.
3. As a Registered User, I want to navigate to my account settings to delete my account information.
    - On the **Edit Profile** page, the user can navigate to **Account Settings** in order to edit their password or delete their account.
    - On clicking **Save**, they will be directed to **Login**.
    - On clicking **Back**, they will be directed to **Edit Profile Page**.
    - On clicking **Delete Account**, the **Delete Modal** will open.
4. As a Registered User, I want to navigate to my recipes page to view my uploaded recipes.
    - If is user is logging in, they will be directed to **My Recipes**.
    - **My Recipes** can also be accessed through the **Navigation Links** or **My Favourites** page.
5. As a Registered User, I want to navigate to upload page to add my recipe to the database.
    - On **My Recipes Page**, **My Favourites Page** and the user **quicklinks dropdown menu** (on larger screens only), the user can navigate to the **Create Recipe** page.
6. As a Registered User, I want to view my own recipe's dashboard to edit recipe as needed.
    - If the user is viewing a **Recipe Page** where they are the recipe's author, the conditional buttons displayed will allow them to **edit** or **delete** the recipe.
    - Clicking **Edit** will bring them to the **Edit Recipe** page.
7. As a Registered User, I want to view my own recipe's dashboard to delete recipe.
    - If the user is viewing a **Recipe Page** where they are the recipe's author, the conditional buttons displayed will allow them to **edit** or **delete** the recipe.
    - Clicking **Delete** will open the **Delete Modal**.
8. As a Registered User, I want to use a save function to save my favourite recipes from other users.
    - If the user is viewing a **Recipe Page** where they are **NOT** the recipe's author, the conditional buttons displayed will allow them to **Add to favourites** or **Remove from Favourites**.
    - Clicking either will redirect the user back to the **Recipe Page**.
9. As a Registered User, I want to navigate to my favourites page to view the recipes I have saved from other users.
    - - **My Favourites** can be accessed through the **Navigation Links** or **My Recipes** page.

**As an Administrative Account holder, I want to:**

1. View **any** recipe dashboard to edit recipe as needed.
2. View **any** recipe dashboard to delete recipe as needed.
3. Still maintain a save function to save my favourite recipes from other users.


[Back to top ⇧](#table-of-contents)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Clicking the Logo located on the top-left of the screen will redirect the user back to the **Home Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Hovering over the **Navigation Links** will trigger the hover effect, confirming the page the user is on:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Collapsible `hamburger` button on mobile and tablet devices reveals **Navigation** menu:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Hovering over the **Footer** icons will trigger the hover effect, confirming the action the user is about to take:
    
    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking the **Footer Social Icons** opens the Developers social platform in a new tab:

    **GitHub:**
    ![Example](assets/testing-files/manual/inserthere.gif)

    **LinkedIn:**
    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking the **Footer Contact Icon** opens the contact modal, with the appropriate user feedback:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking the **Disclaimer** icon triggers the disclaimer notice: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- If the User is logged in, their **user image** will be visible in the top-right of larger screens. Clicking on this will trigger the **dropdown** quick-links menu: 

    ![Example](assets/testing-files/manual/inserthere.gif)

### Home Page
Manual testing was conducted on the following elements on the **Home** Page:

- Using the **Carousel Controls**, the user can browse the featured recipes (the last four to be uploaded):

    ![Example](assets/testing-files/manual/inserthere.gif)

- Hovering over the **Call to Action** buttons will provide feedback to the user: 

    ![Example](assets/testing-files/manual/inserthere.gif)


- The Responsiveness of the **Home Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Find A Recipe Page
Manual testing was conducted on the following elements on the **Find A Recipe** Page:

- The Search Bar allows users to enter their search query:

    Results Found:
    ![Example](assets/testing-files/manual/inserthere.gif)

    No Results Found:
    ![Example](assets/testing-files/manual/inserthere.gif)

- The **Dropdown** Menus allow the user to filter their search:

    Category Search:
    ![Example](assets/testing-files/manual/inserthere.gif)

    Difficulty Search:
    ![Example](assets/testing-files/manual/inserthere.gif)

- The **Pagination** function only displays 6 recipes at a time, allowing the user to browse through pages:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Find A Recipe Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Sign Up Page
Manual testing was conducted on the following elements on the **Sign Up** Page:

- User can enter their details into the input fields: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- On entering the image url, an image preview will be displayed: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Passwords must match: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Hovering over the **Call to Action** buttons provide user feedback:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Login** redirects user to login page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Upon registering, user is directed to **My Recipes** page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Sign Up Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Login Page
Manual testing was conducted on the following elements on the **Login** Page:

- User can enter their details into the input fields:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Sign Up** redirects user to registration page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Upon login, user is directed to **My Recipes** page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Login Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### My Recipes Page
Manual testing was conducted on the following elements on the **My Recipes** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Logout** redirects user back to login page:

    ![Example](assets/testing-files/manual/inserthere.gif)

### My Favourites Page
Manual testing was conducted on the following elements on the **My Favourites** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Logout** redirects user back to login page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **My Favourites Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Edit User Page
Manual testing was conducted on the following elements on the **Edit User** Page:

- The Edit User page is only accessible from *login authenticated* pages: 
    
    My Recipes:
    ![Example](assets/testing-files/manual/inserthere.gif)

    My Favourites:
    ![Example](assets/testing-files/manual/inserthere.gif)

    Quicklinks:
    ![Example](assets/testing-files/manual/inserthere.gif)

- User can enter their details in the input fields (where their current information is the default value):

    ![Example](assets/testing-files/manual/inserthere.gif)

- On entering the image url, an image preview will be displayed: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- **Call to action** buttons provide user feedback: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Cancel** redirects user to My Recipes page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Save** redirects user to My Recipes page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Account Settings** directs user to **Edit Accounts Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Edit User Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Edit Accounts Page
Manual testing was conducted on the following elements on the **Edit Accounts** Page:

- Passwords must match:

    ![Example](assets/testing-files/manual/inserthere.gif)

-   Clicking **Back** redirects user to Edit Profile page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Save** redirects user to Login page:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Delete Account** opens **Delete Modal**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Edit Accounts Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Create Recipe Page
Manual testing was conducted on the following elements on the **Create Recipe** Page:

- User can enter Recipe details:

    ![Example](assets/testing-files/manual/inserthere.gif)

- On adding an image url, an image preview will be displayed:
 
    ![Example](assets/testing-files/manual/inserthere.gif)

- User can use **Dropdown** menus to refine recipe:

    ![Example](assets/testing-files/manual/inserthere.gif)

- User can add and remove ingredients **dynamically**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- User can add and remove directions **dynamically**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Cancel** will return the user back to the previous page: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Save** will redirect the user to My Recipes page: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Create Recipe Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)

### Edit Recipe Page
Manual testing was conducted on the following elements on the **Edit Recipe** Page:

- User can enter Recipe details (current information will be the default value):

    ![Example](assets/testing-files/manual/inserthere.gif)

- On adding an image url, an image preview will be displayed:
 
    ![Example](assets/testing-files/manual/inserthere.gif)

- User can use **Dropdown** menus to refine recipe:

    ![Example](assets/testing-files/manual/inserthere.gif)

- User can add and remove ingredients **dynamically**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- User can add and remove directions **dynamically**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Cancel** will return the user back to the recipe page: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Save** will redirect the user to the recipe page: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- Clicking **Delete** opens **Delete Modal**:

    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Create Recipe Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)
 
### Recipe Page
Manual testing was conducted on the following elements on the **Recipe** Page:

- Clicking the recipe card (image or name) will direct the user to the Individual Recipe Page:

    Home Page:
    ![Example](assets/testing-files/manual/inserthere.gif)

    Find A Recipe:
    ![Example](assets/testing-files/manual/inserthere.gif)

    My Recipes:
    ![Example](assets/testing-files/manual/inserthere.gif)

    My Favourites:
    ![Example](assets/testing-files/manual/inserthere.gif)

- If the user is not logged in, the **Login To Add Favourites** Button will redirect them to the **Login** page: 

    ![Example](assets/testing-files/manual/inserthere.gif)

- If the user is **not** the recipe author, they can add the recipe to, or remove it from their Favourites:

    **Add to Favourites**:
    ![Example](assets/testing-files/manual/inserthere.gif)

    **Remove from Favourites**:
    ![Example](assets/testing-files/manual/inserthere.gif)

- If the user **is** the author, they can edit or delete the recipe:

    **Edit** directs to **Edit Recipe Page**:
    ![Example](assets/testing-files/manual/inserthere.gif)

    **Delete** opens the **Delete Modal**:
    ![Example](assets/testing-files/manual/inserthere.gif)

- The Responsiveness of the **Recipe Page**:

    ![Example](assets/testing-files/manual/inserthere.gif)


[Back to top ⇧](#table-of-contents)

## Automated Testing

### Code Validation

#### [W3C Markup Validator](https://validator.w3.org/ "Link to W3C Markup Validator") was used to validate the `HTML` code used, using the `Validate by URI` method:

**Results:**


#### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "Link to W3C CSS Validator") was used to validate the `CSS` code used:

**Result:**
![Style sheet validation results](assets/testing-files/automated/css-val.png)

#### [JSHint](https://jshint.com/ "Link to JSHint") was used to validate the `JavaScript` and `JQuery` code used:

### Browser Validation
- Chrome: ![test image](assets/testing-files/automated/chrome.png)
- Safari: ![test image](assets/testing-files/automated/safari.png)
- Edge: ![test image](assets/testing-files/automated/edge.png)
- Opera: ![test image](assets/testing-files/automated/opera.png)
- Firefox: ![test image](assets/testing-files/automated/firefox.png)

### Lighthouse Auditing
- Welcome Menu: 

![DevTools - Welcome Menu](assets/testing-files/automated/player-info.png)


Issues were related to render-blocking resources. No recommendations in this report have been implemented in this release but will be taken into consideration for future releases.

[Back to top ⇧](#table-of-contents)

## User testing 
Family members and friends were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to many UX changes in order to create a better experience. 

It was through this testing that the following changes were made:
- Update to the Heads-up display to be more gamer-friendly.
- Change to Questions and Answers `font-size` in order to maintain readability on all devices
- Complete overhaul of Home Page to avoid dead space and to make the experience more intuitive.
- The addition of minutes to the **time counter** function for better readability.
- The addition of a **home button** along side the **play again** button at game end, allowing users to select where they want to go next.
- Using a star icon to represent the score counter on first entrance of the game play area in order to signify the type of content to be displayed.

[Back to top ⇧](#table-of-contents)

***