<h1 align="center">
     <a href="https://bake-it-til-you-make-it.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/k99xn4b/bakeit-banner.png" alt="Bake It 'Til You Make It"></a>
</h1>

<div align="center">
<p><strong><em>Bake It 'Til You Make It</em></strong> is a community-based web application for those who love the art of baking. Users can search and share their favourite creations.</p>
 
<p>Inspired by the old-school baking book (full to the brim with loose paper and notes), the application features hand-drawn graphics and fonts designed to bring the users back to a time of scribbled recipes, in a more organised fashion, through a simplistic and intuitive user interface. </p>
 
<p>The recipe database encourages users to create an account that will allow them to upload and store their favourite baking recipes as well as find new inspiration from other users, saving their favourites for later.</p>

[View the live project here](https://bake-it-til-you-make-it.herokuapp.com/)
<hr>
</div>

![Bake It 'til You Make It Responsiveness](static/images/readme-files/responsive.png)

***

## UX 
### Project Goals
The primary goal of **Bake It 'Til You Make It** is to provide a web-based application, that is simplistic and intuitive in design, that allows users to **create**, **search**, **save** and share their **favourite** baking recipes in one place.

This is the third of four Milestone Projects that the developer must complete during their Full Stack Web Development Program at The Code Institute. 

The main requirements were to build a full-stack website allowing users to manage a common dataset (in this instance, baking recipes) using **HTML5**, **CSS3**, **JavaScript**, **Python**, **Flask** and **MongoDB**.

#### User Goals
The user is looking for:
- A searchable database to locate recipes of their choice.
- An easy-to-use user management system with **CRUD** conventions to:

    - Create a user account.
    - See their user information, as applicable.
    - Edit their user account.
    - Delete their user account.

- An easy-to-use dataset management system with **CRUD** conventions to:

    - Create recipes.
    - Read recipe dashboards.
    - Edit their own recipe creations.
    - Delete their own recipe creations.

- An  intuitive and aesthetically pleasing interface.

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
     - Returning Users **(Registered)**

- **Demographic:**
     - Passion for baking
     - Food lovers
     - All ages

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
- Edit their account
- Delete their account
- Search Recipe database by:
    - Name/Phrase
    - Category
    - Level
- View Recipe Dashboard with the following information:
    - Name
    - Image
    - Recipe Source
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

A scope was defined to identify what needed to be done in order to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
        - Customisable and Editable account:
            - Custom Username/Password
            - Custom User Image
            - Manage their account
            - Upload their own recipes
            - Manage their own recipes
            - Save favourite recipes
        - Easy Navigation
        - Aesthetic and identifiable theme
        - Recipe dashboard:
            - Name
            - Image URL
            - Recipe Source
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
        - Customise and edit their profile:
            - Customise Username/Password
            - Customise User Image
            - Edit and Delete their account
            - Upload their own recipes
            - Edit and delete their recipes
            - Save favourite recipes
        - Navigate to recipes:
            - Search by name, category or level
            - My Recipes Page
            - My Favourites Page
        - Create their recipes, providing:
            - Name
            - Image URL
            - Recipe Source
            - Description
            - Category
            - Serving Size
            - Time
            - Level
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

Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/dNAkS4orUIJwt5yptbgRqP/Bake-It-Til-You-Make-It "Link to Bake It Figma Workspace") with providing a positive user experience in mind:

- Home Page (Non-User links Example):

     ![Home Page Wireframe](static/images/readme-files/wireframes/home-non.png "Home Page Wireframe")

- Home Page (User links Example):

     ![Home Page Wireframe](static/images/readme-files/wireframes/home-user.png "Home Page Wireframe")

- Sign Up Page:

     ![Sign Up Page Wireframe](static/images/readme-files/wireframes/register.png "Sign Up Page Wireframe")

- Log In Page:

     ![Log In Page Wireframe](static/images/readme-files/wireframes/login.png "Log In Page Wireframe")

     (Edit Profile and Edit Accounts pages are styled like this in order to remain consistent)

- Find Recipes Page:

     ![Find Recipes Page Wireframe](static/images/readme-files/wireframes/find-recipe.png "Find Recipes Page Wireframe")

- My Recipes Page:

     ![My Recipes Page Wireframe](static/images/readme-files/wireframes/recipes.png "My Recipes Page Wireframe")

- My Favourites Page:

     ![My Favourites Page Wireframe](static/images/readme-files/wireframes/faves.png "My Favourites Page Wireframe")

- Individual Recipes Page:

     ![Recipe Page Wireframe](static/images/readme-files/wireframes/recipe.png "Recipe Page Wireframe")

- Create Recipe Page:

     ![Create Recipe Page Wireframe](static/images/readme-files/wireframes/create-recipe.png "Create Recipe Page Wireframe")

- Edit Recipe Page:

     ![Edit Recipe Page Wireframe](static/images/readme-files/wireframes/edit-recipe.png "Edit Recipe Page Wireframe")

- Contact Modal:

     ![Modal Wireframe](static/images/readme-files/wireframes/contact.png "Modal Wireframe")

     (All modals were styled the same, using their unique content, in order to remain consistent)

**Post Mock-Up Design Changes:** </br>
While the developer relied heavily on these Wireframes in order to maintain the desired design, there are differences between the Mockups and the final product:
- Most notably, the graphics were changed on the header images for readability purposes to create a better User Experience.
- The colouring for the buttons were altered to distinguish their purpose:
     - *Brown* for normal functionality.
     - *White* for 'cancel' actions (return or logout).
     - *Red* for 'danger' actions (delete or alter account and recipes).
- A quick-links menu for logged in users, providing them with links to the most used pages:
     - Edit Profile
     - Create Recipe
     - Log Out
- A 'breadcrumbs' button was added to the Recipes page, returning the user to their previous page.
- Dynamic Ingredients and Directions allowing users to add input fields as needed creating an array for better readability.
- The decision was made to hide the disclaimer information by default. Providing users with a button where they can reveal it as they wish.


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

     - The charismatic combination of both handwritten and typed typefaces compliments the soft and familiar theme set by the colour palette and overall appearance of the site while also maintaining readability.

- <strong>Imagery</strong>

     - The imagery used was created by the developer using the application [Procreate](https://procreate.art/ "Link to Procreate") in order to create a consistency of the elements while maintaining the look and feel of the application.

     - The background texture effects used were created on [Transparent Textures](https://www.transparenttextures.com/ "Link to Transparent Textures"). Each one was customised with the colours set out in the colour palette in order to remain consistent. The following textures were used: 
          - The [Purty Wood](https://www.transparenttextures.com/purty-wood.html "Link to Purty Wood Texture") texture was used as the screen background.
          - The [Paper 2](https://www.transparenttextures.com/paper-2.html "Link to Paper 2 Texture") texture was used as the background for the 'notebook' effect.
          - The [Lined Paper](https://www.transparenttextures.com/lined-paper.html "Link to Lined Paper Texture") texture was used as the background for the card and image panels.

[Back to top ⇧](#table-of-contents)

## Data Schema

For this project, the NoSQL database [MongoDB](https://www.mongodb.com/ "Link to MongoDB") was used to store the dataset. Within the created database, four collections were created, as illustrated below:

![Data Schema](static/images/readme-files/db-schema.png "Data Schema")

### Users Collection
- When registering an account, the user provides:
     - Username (unique identifier)
     - Email Address
     - Password (hashed)
     - User Image (not required, default used in its place)

- The remaining fields (**favourite_recipes** and **is_admin**) are provided default values, ensuring that, on registration:
     - **favourite_recipes** array is empty. 
     - **is_admin** value is **False**.

- If a user favourites a recipe, that Recipe's **_id** will be included in the **favourite_recipes** array.

### Recipes Collection
- When creating a recipe, the user provides:
     - Recipe Name
     - Recipe Image (not required, default used in its place)
     - Recipe URL Source (not required in the event it is not an online recipe)
     - Description
     - Category
     - Difficulty Level
     - Serving
     - Time
     - Ingredients
     - Directions
- The Ingredients and Directions are entered dynamically to create an array.

- The remaining fields (**baker** and **favourite_count**) are provided default values, ensuring that:
     - **baker** is automatically the current user (**session.user**), storing their **ObjectId** and **username**.
     - **favourite_count** is empty.

- When a user favourites the recipe, the number is incremented.

### Categories Collection
- There are four specified categories that the developer chose from researching multiple baking sources.
     - **Bread**
     - **Cake**
     - **Biscuit**
     - **Pastry**

- They were selected to refer to a broad spectrum of baking recipes.
- Each category has a corresponding icon used throughout to provide visual distinction for each.

### Levels Collection
- The Recipe's difficulty level is distinguished by:
     - **Easy**
     - **Medium**
     - **Hard**
     
- This was reflective of the user stories, appealing to bakers of all levels.

## Features

### Design Features
Each page of the website features a consistently responsive and intuitive navigational system:
- There is a conventionally placed **navbar** on the top of each page with easily accessible and identifiable navigation links with a clickable logo, redirecting users back to the home page.
     - On mobile and tablet screens, the navbar is located in a conventionally placed 'hamburger' menu.
- There is a **banner image with title** on each page providing users with the necessary feedback of their current position on the site.
     - An `active` class is used in the `navbar` to provide this feedback as well.
- The **Footer** contains a disclaimer that is hidden, using a **toggler** function to display the information regarding the use of copyrighted material on the website.
- The **Footer** contains the appropriate **icons** to allow users to:
     - Link to the developers GitHub Page.
     - Link to the developers LinkedIn Page.
     - Open a **Contact Modal** to send a message to the Developer. 
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information") was used to extend the `base.html` page, allowing for the utmost consistency and preservation of functionality across all pages. The extended block elements created the same basic layout for each page:

     ```
     <nav>
          <!-- Navigational content -->
     </nav>

     <section>

          {% block header %}
               <!-- Page Banner Image and Title -->
          {% endblock %}

          {% block flash %}
               <!-- Appropriate flash messages -->
          {% endblock %}

          {% block content %}
               <!-- Content unique to each page -->
          {% endblock %}

     </section>

     <footer>
          <!-- Footer content -->
     </footer>
     ```

- If the user is in session, there will be additional links added to the `navbar`:
     - Edit Profile
     - Create Recipe
     - Logout

- These links allow users to get straight to where they want to be. The additions are broken down as follows:

     - On mobile and tablet screens, the extra buttons will appear on the navigation (hamburger) menu in order to provide quick access.

     - On larger devices a conventionally placed `user_img` will appear on the right side of the navigation menu, with a dropdown list of the additional links.

- Recipe **Cards** are used throughout the website, providing users with a snapshot of the recipe and it's information before they view the entire recipe page. Each card is designed the same for consistency purposes and allows the user to either click on the recipe **image** or **name** in order to be directed to the recipe page.
 

### Existing Features

**[Home Page](http://bake-it-til-you-make-it.herokuapp.com/home "Link to Home page")**
| Feature      | Description  |
|--------------|--------------|
| Carousel     | Bootstrap Carousel Component that displays the last four uploaded recipes |
| Call to Action | Buttons connecting users to **Sign Up** or **Login** pages (**if not signed in**) or **My Recipes** or **My Favourites** pages (**if signed in**)|


**[Find A Recipe Page](http://bake-it-til-you-make-it.herokuapp.com/find_recipes "Link to Find A Recipe page")**
| Feature       | Description  |
|---------------|--------------|
| Search Bar    | Search bar function allowing users to **search** for their preferred recipes. Using a text search will direct users to the `search.html` page |
| Dropdown Menu | Nested dropdown menu to **refine** the users search by either **Category** or **Level**|
| Pagination    | The **Pagination** functionality will be activated once the amount of recipes to be displayed is over `6`. This was to avoid overwhelming the user.|

**Search Results**
| Feature       | Description  |
|---------------|--------------|
| Call to Action | There is a **Search Again** button allowing users to reset the search. This is conditional. If there **is** results from their search, the button is placed at the bottom of the page, allowing the users to view their results first. If there is **not** any results, the button is placed at the top of the page for their convenience (above the recommendations).

**[Sign Up Page](http://bake-it-til-you-make-it.herokuapp.com/register "Link to Sign Up page")**
| Feature       | Description  |
|---------------|--------------|
| Input Fields    | The **input** fields allow users to enter their information. The user can enter a profile image if they wish, or a default image will be used instead.|
| Image Preview | On adding an image url to the `Profile Picture` field, the user can preview their image to ensure that the link is correct and it is the image they would like to use. |
| Password Authentication | The **password** field uses [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information") to hash the password on entry and **confirm password** is validated using **Javascript**. If the passwords do not match, a `disabled` class is added to the **Register** button, preventing a password error. |
| Call to Action | Once the input fields are completed as required, the user can click to **Register** or, if they already have an account, they can **Login**. |

**[Login Page](http://bake-it-til-you-make-it.herokuapp.com/login "Link to Login page")**
| Feature       | Description  |
|---------------|--------------|
| Input Fields    | The **input** fields allow users to enter their username. |
| Password Authentication | The **password** field uses [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information") to un-hash the salted password for login authentication|
| Call to Action | Once the input fields are completed as required, the user can click to **Login** or, if they do not already have an account, they can **Register**. |

**My Recipes Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Call to Action    | The User's **My Recipes** provides multiple actions the user can take: **Edit Profile**, **Create Profile**, link to **My Favourites** and the **logout** function. If they have no recipes in their repository, the user will be provided with addtional links to **get inspired** (search recipes) or **get creative** (create a recipe).|

**My Favourites Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Call to Action    | The User's **My Favourites** provides multiple actions the user can take: **Edit Profile**, **Create Profile**, link to **My Recipes** and the **logout** function. |

**Edit User Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Input Fields | The user is able to edit their profile image as they see fit. Their current information is used as the **default** value for the fields |
| Image Preview | The `Profile Image` field allows the user to preview their current profile image. Changing the image url calls a `JavaScript` function, allowing the user to get real-time feedback as they change the image.|
| Call to Action | The user can choose to **Cancel** their actions or **Save** their new information. Another button directs the user to the **Account Settings** page for user to take further action |

**Edit Account Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Input Fields | On this page the user is able to change their password if they wish, their current password is *not* set as the default value.|
| Password Authentication | The **password** field uses [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information") to hash the password on entry and **confirm password** is validated using **Javascript**, with user feedback. If the passwords do not match, a `disabled` class is added to the **Save** button, preventing a password error|
| Call to Action | The user can choose to go **Back** to the previous page (**Edit User**) or **Save** their new information. Another button (**Delete Account**) opens the `delete_user` **modal** |
| Modal | The `delete_user` **modal** is defensively designed allowing the user to confirm their actions before proceeding with the deletion. |

**Create Recipe Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Input Fields | The **input fields** allow the user to input the recipe information as necessary. All fields are appropriately **validated**, with the exception of `Recipe Image` and `Recipe URL` to allow for the upload of recipes not available online.|
| Image Preview | Addint to the `Recipe Image` field calls a `JavaScript` function, allowing the user to get real-time feedback of the image.|
| Dropdown Menu| User can refine their recipe using the dropdown menu|
| Dynamic Input Fields| The fields for `Ingredients` and `Directions` allow for dynamic input. The user can use the **Add Ingredient**, **Add Direction** or **Delete** buttons to add or remove fields as necessary. This was used in order to create a dynamic array of both lists for a much cleaner and readable display.|
| Call to Action | As well as the **Add Ingredient** and **Add Direction** buttons, there is a **Cancel** and **Add Recipe** button, directing the user to their **Recipes** page.|

**Edit Recipe Page** (This page requires login authentication)
| Feature       | Description  |
|---------------|--------------|
| Input Fields | The **input fields** allow the user to edit the recipe information as necessary. All fields use the current values as their default, allowing the user to only change the information they need to.|
| Image Preview | The `Recipe Image` field allows the user to preview their current recipe image. Changing the image url calls a `JavaScript` function, allowing the user to get real-time feedback as they change the image.|
| Dynamic Input Fields| The fields for `Ingredients` and `Directions` allow for dynamic input. The user can use the **Add Ingredient**, **Add Direction** or **Delete** buttons to add and remove fields as necessary, with the exception of the first in each list, in order to preserve the array.|
| Call to Action | As well as the **Add Ingredient** and **Add Direction** buttons, there is a **Cancel** and **Add Recipe** button, directing the user to the appropriate page. A **Delete** button, opens the `delete_recipe` modal |
| Modal | The `delete_recipe` **modal** is defensively designed allowing the user to confirm their actions before proceeding with the deletion. |

**[Recipe Page (Apple Tart Recipe)](http://bake-it-til-you-make-it.herokuapp.com/recipe/60b8d90f21c54a83d5c121e1 "Link to Apple Tart Recipe Page")**

The **Call to Action** buttons on the recipe page are conditional to the user's role on the website, with the following break down:

| Role       | Conditional Buttons  |
|---------------|--------------|
| Not Logged in| **Login To Add Favourites** - directing the user to login in, in order to save the recipe to their favourites|
| Logged in user is **not** author | **Add To Favourites** - directing the user to add the recipe to their favourites. They are then redirected back to the recipe page with a new **Remove from Favourites** button.|
| Logged in user is **Author** | **Edit** and **Delete** buttons direct the user to **Edit Recipe Page** and `delete_recipe` **modal** respectively.|
| Logged in user is **Admin** | The administrative user has access to **Edit** and **Delete** buttons as well as the **Add To Favourites** or **Remove from Favourites** (should they want to save it)|
| **All Users**| A **breadcrumb** button (powered by `JavaScript`) allows the user to return to their previous page, giving them more control.|

### Features to Implement in the future
- **Recipe PDF Download** 
     - A feature that would allow the user to download a **PDF** copy of the recipe for their own personal records.
     - The developer researched the possibilities of this feature, and know it is possible using the `pdfkit` library import but they held off from implementing it in this release in order to further develop their skills to be able to implement the feature properly. A simplified version could have been implemented but it would not be to the standard the developer would like.

- **Image Upload**
     - A feature that would allow the user to upload a file image, rather than using an image url, avoiding the issues they encountered in the validation stages.
     - It was on the suggestion of the Code Institute Student Care team that the developer did not implement this feature in this release.

- **Image Processing**
     - A feature that would allow for validation of properties on images used.
     - The developer did try to implement this feature using [Pillow](https://pillow.readthedocs.io/en/stable/ "Link to Pillow doc") but they were unsuccessful in getting it to work, so it was suggested to them to use the `pattern` attribute on the image input field in this release.

- **More Community Capabilities**
     - A feature that would allow users to share ideas and help other users on the site, creating a more dynamically involved community focus.
     - This idea was in the original plans but the developer chose to scale the scope down, excluding this feature, as they knew their present capabilities would give it the justice the feature deserved.

- **Email Verification**
     - A feature that would allow for the developer to send an automated email to users on registration, verifying their email and account.
     - This, too, was in the original plans and the developer tried their best to be able to implement it in this release, but it was not meant to be. 

[Back to top ⇧](#table-of-contents)

## Issues and Bugs 
The developer ran into a number of issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

**Base.html** <br>
The `base.html` page uses Jinja templates in order to extend its components (e.g. page design, `navbar` & `footer`) to all other pages. In trying to implement an pseudo `active` class on the anchor links in the navigation bar, an issue arose where the special state would be applied to all links, not just the active link. It was through a post of a similar problem on [Stack Overflow](https://stackoverflow.com/questions/29902575/highlight-menu-item-based-on-current-view "Solution to problem on Stack Overflow") that the developer found a solution, using `block` elements for each class.

**Recipe Cards** <br>
The recipe card panel used throughout the website (for consistency) was implemented using the Bootstrap Card Component. Very early into development, the developer noted there was a styling issue with the `ul` element whereby the `li` elements nested would not conform to the styling that was needed to be readable. The `li` elements, due to the Bootstrap styling, would only display in a `inline` format, which caused padding issues within the card. In order to avoid this, and to maintain the design, the `ul` was removed and replaced with Bootstrap grid styling. This was done after researching similar issues.

**Home Page** <br>
The Homepage uses a Bootstrap Carousel feature to highlight the four latest baking recipes added to the database. An issue arose with the carousel whereby only one recipe would be called on repeat. In their endless Google searching, the developer found a helpful article on [Stack Overflow](http://www.zhishibo.com/articles/30623.html "Solution to problem on Stack Overflow") that recommended using a `loop.index` method on the `active` class of the carousel in order to loop through the latest recipes.

**Edit User Page** <br>
In order to make the `edit_user.html` functionality more user-friendly, the developer tried to create a possibility that the user would not have to change their password if they did not wish to (e.g. if they only wanted to change their user image). The problem with this was that should the user leave the password field blank (choosing not to change it), it would automatically change the users password to 'blank' on the database. This was insufficient and in no ways user-friendly, so the developer researched other methods. Their first thought was to use the user's password value as the default value for the field but, as the password is hashed and salted using `werkzeug.security` import, this would not work. The alternative, and the conclusive solution, was to create a separate accounts settings page, where the user has the freedom to change their password or delete their account.

**Password Authentication** <br>
The developer encountered a bug in authenticating passwords on both **Edit User** and **Register** page. The `password` and `confirm password` fields are validated using a `JavaScript` function to confirm that the values match. The problem with this was that it did not matter to either the **Save** button or the **Register** whether the passwords match and so a user could accidentally create a faulty password, losing access to their account. In order to fix this bug, the developer, on the advice of their mentor, created a conditional `disabled` class for the buttons alongside the `JavaScript` function, preventing the user submitting a password error.

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

**Reverted Commits Note** <br>
The developer was forced to revert two commits ([1](https://github.com/rebeccatraceyt/bake-it-til-you-make-it/commit/4a410cb11de6f90f3fb4a698e61818b1724e7cd6) and [2](https://github.com/rebeccatraceyt/bake-it-til-you-make-it/commit/7a1f64dd73470a54868ffbea1eeb8c6a54770d47)) on the 8th of June in order to backtrack to a previous commit, preserving the functionality that was lost. After trying to implement a `partials` directory, that would store extendable blocks to be used on all pages, the developer noticed that, in doing so, vital functions, including **user authentication** were throwing an error. Having already pushed these commits to Github, the developer reverted the commit that implemented the creation of the `@login_decorator` in `app.py`, as they believed this to be the cause. Once this was reverted, it was clear that it was not the cause, the commit previous to that (the implementation of the `partials` directory) was reverted as well. In doing this, the functionality was restored. The developer chose not to re-implement the `partials` directory but was successful in re-implementing the `@login_decorator` functionality at a later date. 

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
- [Heroku](https://id.heroku.com/login "Link to Heroku login page")
     -  Heroku was used in order to deploy the website.
- [Figma](https://www.figma.com/ "Link to Figma homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to validate the responsiveness of the design throughout the process, and to generate mockup imagery to be used.
- [Procreate](https://procreate.art/ "Link to ProCreate homepage")
     - Procreate was used to create and edit images as well as using the colour picker tool to ensure consistency throughout.
- [Imgbb](https://imgbb.com/ "Link to Imgbb site") 
     - ImgBB was used to externally host images used.
- [Transparent Textures](https://www.transparenttextures.com/ "Link to Transparent Texures site")
     - Transparent Textures was used to create the textured background heavily featured on the website.
- [Font Awesome](https://fontawesome.com/ "Link to Font Awesome site")
     - Font Awesome was used in conjunction with Iconify for icons used throughout the website.
- [Iconify](https://iconify.design/ "Link to Iconify Design site")
     - Iconify was used in conjunction with Font Awecome for icons used throughout the website.

     *The developer made the decision to use both websites for icons as neither had **all** the icons the developer needed to use for UI purposes. Although this may not be best practice, it provided the necessary design functionality for several items, most notably the conditional icons for each category.*

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
     - SweetAlert2 was used to customise the **Contact Form** success message for UX purposes.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Link to Flask Homepage")
     - Flask was used as the web framework for the application.
- [PyMongo](https://pypi.org/project/pymongo/ "Link to PyMongo information")
     - `flask_pymongo` was used a communication line between the MongoDB database and Python.
- [Pagination](https://flask-paginate.readthedocs.io/en/master/ "Link to flask-paginate documentation")
     - `flask_paginate` extension was used to implement pagination functionality on select pages.
- [BSON](https://bsonspec.org/ "Link to BSon documentation")
     - `bson.objectid` is a required dependency for MongoDB management system.
- [Jinja](http://jinja.pocoo.org/docs/2.10/ "Link to Jinja information")
     - Jinja templating language was used to simplify and display backend data in html.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/ "Link to Werkzeug information")
     - Werkzeug was used for password hashing and authentication.

### Database Management
- [MongoDB](https://www.mongodb.com/ "Link to MongoDB site")
     - MongoDB was the chosen NoSQL database for this website.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas "Link to MongoDB Atlas site")
     - MongoDB Atlas was the cloud database service used to host the database.


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
The developer consulted multiple sites in order to better understand the code they were trying to implement. 

The [Code Institute Task Manager Mini Project](https://github.com/Code-Institute-Solutions/TaskManagerAuth) mini project was used as a reference point for the developer in the development of the core **CRUD** functionality of the website. The lessons included with the mini-project helped the developer to get a better understanding of each functionality and how to customise it to suit their project.

For code that was copied and edited, the developer made sure to reference this within the code. The following sites were used on a more regular basis:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [JSfiddle](https://jsfiddle.net/ "Link to JSfiddle page")

[Back to top ⇧](#table-of-contents)

## Acknowledgements
The developer would like to thank the following:
- Fellow CI students, for the inspiration and guidance.
- Tim Nelson for the walkthrough videos on the Code Institute platform.
- Their mentor Seun for her consistent guidance and support.
- Their family and friends for providing a limitless amount of encouragement and suggestions during the entire process of development.

[Back to top ⇧](#table-of-contents)

***

## Technical Support

If you encounter any issues with this website, or require any further clarification or support, please email the [developer](mailto:rebecca.traceytimoney@gmail.com?subject=[Bake%It%Support]). Thank you!

[Back to top ⇧](#table-of-contents)

***
