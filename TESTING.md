<h1 align="center">
     <a href="https://bake-it-til-you-make-it.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/k99xn4b/bakeit-banner.png" alt="Bake It 'Til You Make It"></a>
</h1>

<h1 align="center"> Testing </h1>

[Main README.md file](README.md "Link to README file")

[View live project](https://bake-it-til-you-make-it.herokuapp.com/ "Link to Live project")

[View project Repository](https://github.com/rebeccatraceyt/bake-it-til-you-make-it "Link to Repository")

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
    1. [Common Elements Testing](#Common-Elements-Testing)
    2. [Page Elements Testing](#Page-Elements-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
     - [Lighthouse Auditing](#Lighthouse-Auditing)
4. [User Testing](#User-Testing)

***

![Bake It 'til You Make It Responsiveness](static/images/readme-files/responsive.png)

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

**Administrative Account Holder:**

1. As an Administrative Account holder, I want to view **any** recipe dashboard to edit recipe as needed.
    - The Administrative Accounts have 'admin privileges' that allow them to monitor all recipes entered.
    - If the  Administrative Account holder is viewing a **Recipe Page**, the conditional buttons displayed will allow them to **edit** the recipe.
    - Clicking **Edit** will bring them to the **Edit Recipe** page.
2. As an Administrative Account holder, I want to view **any** recipe dashboard to delete recipe as needed.
    - If the  Administrative Account holder is viewing a **Recipe Page**, the conditional buttons displayed will allow them to **delete** the recipe.
    - Clicking **Delete** will open the **Delete Modal**.
3. As an Administrative Account holder, I want to still maintain a save function to save my favourite recipes from other users.
    - - If the  Administrative Account holder is viewing a **Recipe Page**, the conditional buttons displayed will allow them to **Add to favourites** or **Remove from Favourites**.
    - Clicking either will redirect the user back to the **Recipe Page**.

[Back to top ⇧](#table-of-contents)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Clicking the Logo located on the top-left of the screen will redirect the user back to the **Home Page**:

    ![Logo Click](static/images/testing-files/manual/logo-click.gif)

- Hovering over the **Navigation Links** will trigger the hover effect, confirming the page the user is on:

    ![Navigation Bar Hover class](static/images/testing-files/manual/nav-hover.gif)

- Collapsible `hamburger` button on mobile and tablet devices reveals **Navigation** menu:

    ![Collapsible Navigation Bar](static/images/testing-files/manual/nav-mob.gif)

- Hovering over the **Footer** icons will trigger the hover effect, confirming the action the user is about to take:
    
    ![Footer Hover class](static/images/testing-files/manual/footer-hover.gif)

- Clicking the **Footer Social Icons** opens the Developers social platform in a new tab:

    - **GitHub:**
    ![Github Link](static/images/testing-files/manual/github.gif)

    - **LinkedIn:**
    ![LinkedIn Link](static/images/testing-files/manual/linkedin.gif)

- Clicking the **Footer Contact Icon** opens the contact modal, with the appropriate user feedback:

    ![Contact Form](static/images/testing-files/manual/contact.gif)

- Clicking the **Disclaimer** icon triggers the disclaimer notice: 

    ![Disclaimer](static/images/testing-files/manual/disclaimer.gif)

- The user can log out from numerous points:

    - My Recipes:

        ![Log out @ My Recipes](static/images/testing-files/manual/lo-recipes.gif)
    
    - My Favourites:

        ![Log out @ My Favourites](static/images/testing-files/manual/lo-faves.gif)
    
    - Quick Links:

        ![Log out @ Quick Links](static/images/testing-files/manual/lo-quicklink.gif)
    
    - On Mobile Devices:

        ![Log out on mobile](static/images/testing-files/manual/lo-mobile.gif)

- Recipes can be accessed by clicking:

    - Image

        ![Recipe Image Click](static/images/testing-files/manual/recipe-img.gif)

    - Name

        ![Recipe Image Name](static/images/testing-files/manual/recipe-name.gif)

### Page Elements Testing

#### Home Page

Manual testing was conducted on the following elements on the **Home** Page:

- Using the **Carousel Controls**, the user can browse the featured recipes (the last four to be uploaded):

    ![Carousel Controls](static/images/testing-files/manual/carousel.gif)

- Hovering over the **Call to Action** buttons will provide feedback to the user: 

    ![Home Page Buttons](static/images/testing-files/manual/home-btns.gif)

- The Responsiveness of the **Home Page**:

    ![Home Page Responsiveness](static/images/testing-files/manual/home-res.gif)

#### Find A Recipe Page

Manual testing was conducted on the following elements on the **Find A Recipe** Page:

- The Search Bar allows users to enter their search query:

    - When Results are found:
    
        ![Search Results](static/images/testing-files/manual/search-results.gif)

    - No Results Found:
    
        ![No Search Results](static/images/testing-files/manual/search-no-results.gif)

- The **Dropdown** Menus allow the user to filter their search:

    - Category Search:
    
        ![Category Filter Search](static/images/testing-files/manual/category.gif)

    - Difficulty Search:
    
        ![Level Filter Search](static/images/testing-files/manual/level.gif)

- The **Pagination** function only displays 6 recipes at a time, allowing the user to browse through pages:

    ![Pagination](static/images/testing-files/manual/paginate.gif)

- The Responsiveness of the **Find A Recipe Page**:

    ![Find A Recipe Responsiveness](static/images/testing-files/manual/search-res.gif)

#### Sign Up Page

Manual testing was conducted on the following elements on the **Sign Up** Page:

- User can intuitively create an account: 

    ![Registration Process](static/images/testing-files/manual/register.gif)

- Clicking **Login** redirects user to login page:

    ![Sign Up to Log in](static/images/testing-files/manual/reg-log.gif)

- The Responsiveness of the **Sign Up Page**:

    ![Sign Up Page Responsiveness](static/images/testing-files/manual/register-res.gif)

#### Login Page

Manual testing was conducted on the following elements on the **Login** Page:

- User can intuitively enter their details to log into their account:

    ![Login Process](static/images/testing-files/manual/login.gif)

- Clicking **Sign Up** redirects user to registration page:

    ![Log in to Sign Up](static/images/testing-files/manual/log-reg.gif)

- The Responsiveness of the **Login Page**:

    ![Login Page Responsiveness](static/images/testing-files/manual/login-res.gif)

#### My Recipes Page

Manual testing was conducted on the following elements on the **My Recipes** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![My Recipes buttons hover class](static/images/testing-files/manual/recipe-btns.gif)

- The Responsiveness of the **My Recipes Page**:

    ![My Recipes Responsiveness](static/images/testing-files/manual/myrecipes-res.gif)

#### My Favourites Page

Manual testing was conducted on the following elements on the **My Favourites** Page:

- Hovering over **Call to Action** buttons provide user feedback: 

    ![My Recipes buttons hover class](static/images/testing-files/manual/fave-btns.gif)

- The Responsiveness of the **My Favourites Page**:

    ![My Recipes Responsiveness](static/images/testing-files/manual/faves-res.gif)

#### Edit User Page

Manual testing was conducted on the following elements on the **Edit User** Page:

- User can intuitively edit their profile: 
    
    ![Edit User Process](static/images/testing-files/manual/edit-user.gif)

- Clicking **Cancel** redirects user to My Recipes page:

    ![Edit User - Cancel button](static/images/testing-files/manual/edit-user-cancel.gif)

- The Responsiveness of the **Edit User Page**:

    ![Edit User Page Responsiveness](static/images/testing-files/manual/edit-user-res.gif)

#### Edit Accounts Page

Manual testing was conducted on the following elements on the **Edit Accounts** Page:

- User can intuitively edit their account:

    ![Edit Account Process](static/images/testing-files/manual/edit-acc.gif)

- Clicking **Back** redirects user to Edit Profile page:

    ![Edit Account - Back button](static/images/testing-files/manual/edit-acc-back.gif)

- Clicking **Delete Account** opens **Delete Modal**:

    ![Delete Account Modal](static/images/testing-files/manual/delete-acc.gif)

- The Responsiveness of the **Edit Accounts Page**:

    ![Edit Account Page Responsiveness](static/images/testing-files/manual/edit-acc-res.gif)

#### Create Recipe Page

Manual testing was conducted on the following elements on the **Create Recipe** Page:

- The creative process for entering recipe details is as follows:
    
    - Enter Recipe name

        ![Enter Recipe Name](static/images/testing-files/manual/create-name.gif)

    - Enter image url, an image preview will be displayed:
    
        ![Enter Recipe Img URL](static/images/testing-files/manual/create-img.gif)

    - User can use **Dropdown** menus to refine recipe:

        ![Refine Recipe by Dropdowns](static/images/testing-files/manual/create-dropdown.gif)

    - Add and remove ingredients **dynamically**:

        ![Add and Remove Ingredients](static/images/testing-files/manual/create-ingred.gif)

    - Add and remove directions **dynamically**:

        ![Add and Remove Directions](static/images/testing-files/manual/create-direct.gif)

- Clicking **Save** will redirect the user to My Recipes page: 

    ![Click Save](static/images/testing-files/manual/create-save.gif)

- Clicking **Cancel** will return the user back to the previous page: 

    ![Click Cancel](static/images/testing-files/manual/create-cancel.gif)

- The Responsiveness of the **Create Recipe Page**:

    ![Create Recipe Page Responsiveness](static/images/testing-files/manual/create-res.gif)

#### Edit Recipe Page

Manual testing was conducted on the following elements on the **Edit Recipe** Page:

- Current information will be the default value, User can edit as needed:

    ![Edit Recipe Process](static/images/testing-files/manual/edit-rec.gif)

- Clicking **Cancel** will return the user back to the recipe page: 

    ![Edit Recipe Cancel button](static/images/testing-files/manual/edit-cancel.gif)

- Clicking **Delete** opens **Delete Modal**:

    ![Edit Recipe Delete Modal](static/images/testing-files/manual/edit-delete.gif)

- The Responsiveness of the **Edit Recipe Page**:

    ![Edit Recipe Page Responsiveness ](static/images/testing-files/manual/edit-rec-res.gif)
 
#### Recipe Page

Manual testing was conducted on the following elements on the **Recipe** Page:

- Clicking the **Back** button will return the user to the previous page: 

    ![Recipe Page Back button](static/images/testing-files/manual/rec-back.gif)

- If the user is not logged in, the **Login To Add Favourites** Button will redirect them to the **Login** page: 

    ![Non-User on Recipe Page](static/images/testing-files/manual/rec-non.gif)

- If the user is **not** the recipe author, they can add the recipe to, or remove it from their Favourites:

    ![Not Author on Recipe Page](static/images/testing-files/manual/rec-user.gif)

- If the user **is** the author, they can edit or delete the recipe:

    ![Author on Recipe Page](static/images/testing-files/manual/rec-auth.gif)

    - **Edit** directs to **Edit Recipe Page**:
    
        ![Recipe to Edit Recipe](static/images/testing-files/manual/rec-edit.gif)

    - **Delete** opens the **Delete Modal**:
    
        ![Recipe Delete Modal](static/images/testing-files/manual/rec-delete.gif)

- The Responsiveness of the **Recipe Page**:

    ![Recipe Page Responsiveness](static/images/testing-files/manual/rec-res.gif)


[Back to top ⇧](#table-of-contents)

## Automated Testing

### Code Validation

- [W3C Markup Validator](https://validator.w3.org/ "Link to W3C Markup Validator") was used to validate the `HTML` code used, using the `Validate by URI` method.

    - All errors highlighted and resolved, with the exception of the errors thrown by Jinja.


-  [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "Link to W3C CSS Validator") was used to validate the `CSS` code used.

    ![Style sheet validation results](static/images/testing-files/automated/css-val.png)


- [JSHint](https://jshint.com/ "Link to JSHint") was used to validate the `JavaScript` and `JQuery` code used.

    - Errors highlighted in `script.js` pertain to [SweetAlert2](https://sweetalert2.github.io/ "Link to Sweet Alert 2 page") and [jQuery Validation](https://jqueryvalidation.org/ "Link to jQuery Validation page") as well as the `onclick` functions:

        ![Script Validation Results](static/images/testing-files/automated/js-val.png) 


    - There were no errors highlighted in `recipe.js` file

- [PEP8 Online](http://pep8online.com/ "Link to PEP8 Online") was used to validate `Python` code.
    
    - All highlighted errors and warnings resolved.

### Browser Validation
**Chrome:**

![Chrome test image](static/images/testing-files/automated/chrome.png)

**Safari:**

![Safari test image](static/images/testing-files/automated/safari.png)

**Edge:**

![Edge test image](static/images/testing-files/automated/edge.png)


**Opera:**

![Opera test image](static/images/testing-files/automated/opera.png)

**Firefox:**

![Firefox test image](static/images/testing-files/automated/firefox.png)

### Lighthouse Auditing

#### Desktop
| Page | Performance | Accessibility | Best Practice | SEO |
|------|:-------------:|:---------------:|:---------------:|:-----:|
| Home Page | 86% | 100% | 80% | 100% |
| Find Recipes | 99% | 92% | 80% | 90% |
| Login | 97% | 100% | 80% | 100% |
| Register | 99% | 100% | 80% | 100% |
| Edit User | 99% | 100% | 80% | 100% |
| Edit Account | 99% | 100% | 80% | 100% |
| My Recipes | 97% | 100% | 80% | 100% |
| My Favourites | 98% | 100% | 80% | 90% |
| Create Recipe | 99% | 100% | 80% | 100% |
| Edit Recipe | 98% | 90% | 80% | 100% |
| Recipe Page | 96% | 100% | 80% | 90% |

#### Mobile
| Page | Performance | Accessibility | Best Practice | SEO |
|------|:-------------:|:---------------:|:---------------:|:-----:|
| Home Page | 86% | 100% | 93% | 100% |
| Find Recipes | 73% | 92% | 93% | 90% |
| Login | 93% | 100% | 87% | 100% |
| Register | 92% | 100% | 87% | 100% |
| Edit User | 70% | 100% | 87% | 100% |
| Edit Account | 92% | 100% | 87% | 100% |
| My Recipes | 79% | 100% | 93% | 100% |
| My Favourites | 89% | 100% | 93% | 90% |
| Create Recipe | 92% | 100% | 87% | 100% |
| Edit Recipe | 82% | 90% | 87% | 100% |
| Recipe Page | 74% | 100% | 87% | 92% |

#### Breakdown of Results

| Page | Error / Warning | Comment |
|:-----:|:---------------:|:-------|
| All Pages | Largest Contentful Paint | The images rendered on each page threw this error due to a number of reasons. The developer was able to pre-load images rendered using the `rel="preload"` attribute in **HTML** and using `-webkit-image-set()` in **CSS** ([Source](https://web.dev/preload-responsive-images/)). The problem still persists due to the use of third party images throughout the site.|
| All Pages | Render-blocking resources | This warning stems from the use of `emailJS` for the contact form. The developer attempted to resolve this issue using the `defer` attribute within the script tag, but this only created an issue whereby the function sending the email was not called. |
| Home Page | Tap targets not sized appropriately | Relating to the carousel controls. Issue was resolved by resizing the anchor tag of the controls. |
| Home Page | Defer offscreen images | This relates to the carousel feature of the home page. The researched solution was to 'lazy-load' the images but that is not an option in this release due to the use of image urls, in lieu of uploads. |
| My Favourites | Links are not crawlable | Relating to the `.page-link` class in the Bootstrap Pagination controls. |
| All Pages | Avoid enormous network payload | This warning relates to the use of external images throughout the site. The payload size fluctuated significantly because of this. The solution to this would be to upload images directly to the site, but this feature is not included in this release |
| Find Recipes | Size Images | This issue (like many others before) pertains to the use of external images, where the resource size is far greater than the displayed size. |
| All Pages | Does not use HTTPS | In researching this error, the only conclusive reason for it is the use of mixed content throughout the site. |


[Back to top ⇧](#table-of-contents)

## User testing 
Family members and friends were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to many UX changes in order to create a better experience. 

It was through this testing that the following changes were made:
- Update to Logo to be more conventionally positioned. The original designs were for a floating logo but that was quickly replaced due to the issues it cause.
- Change to Recipe Card `font-size` and `max-length` in order to create consistency across all recipes. It was noted that some of the recipe names were longer than others, creating a spacing issue.
- Create conditional buttons for each category in order to better distinguish the differences.
- Create a 'quick-links' function for users to create a more streamline experience.
- Create a separate **Accounts Settings** page just for changing password or deleting account, in order to avoid the "danger" zone as much as possible.
- Create a live image preview window, allowing the user to see the current image on the **Edit User** and **Edit Recipe** pages.
- A **breadcrumbs** button on the Recipe page, allowing the users to return to their previous page for convenience. 
- Create a *Search Again* button on the **Find Recipes** search results in order to provide the user with easy return access.

[Back to top ⇧](#table-of-contents)

***