# ------- Library Imports -------

import os
from flask import (
        Flask, flash, render_template, 
        redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# ------- Flask App Configuration -------

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------- Pagination -------

"""
Pagination adapted from:
    https://github.com/Sharon-B/Recipe-Box/blob/master/app.py
"""

PER_PAGE = 6

def paginated(recipes):
    
    # Set pagination configuration
    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")
    
    offset = page * PER_PAGE - PER_PAGE
    
    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    
    # Set pagination configuration
    page, per_page, offset = get_page_args(page_parameter="page",
                                           per_page_parameter="per_page")
    
    total = len(recipes)
    
    return Pagination(page=page,
                      per_page=PER_PAGE,
                      total=total,
                      css_framework="bootstrap4")


# ------- Check User Login Function -------

def user_logged_in(username):
    """
    Function checks login status of current user.
        credit: https://github.com/Nicola2309/MS3/blob/master/app.py
    """
    
    if "user" in session:
        if session["user"] == username:
            return True
    
    return False


# ------- Home Page -------

@app.route("/")
@app.route("/home")
def home():
    """
    Home page displays the 4 latest recipes
    """
    latest_recipes = mongo.db.recipes.find().sort("_id", -1).limit(4)
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        return render_template("index.html", 
                               recipes=latest_recipes, 
                               user=user, 
                               title="Bake It Til You Make It")
    
    else:
        return render_template("index.html", 
                               recipes=latest_recipes, 
                               title="Bake It Til You Make It")
        

# ------- Find Recipes Page -------
@app.route("/find_recipes")
def find_recipes():
    
    recipes = list(mongo.db.recipes.find())
    
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        return render_template("recipe/find_recipes.html", 
                               user=user,
                               recipes=recipes_paginated,
                               pagination=pagination, 
                               title="Find Recipes")
        
    return render_template("recipe/find_recipes.html", 
                           recipes=recipes_paginated,
                           pagination=pagination, 
                           title="Find Recipes")


# ------- Search for Recipes -------
@app.route("/search", methods=['GET', 'POST'])
def search():
    
    query = request.form.get("query")
    
    recipes = list(mongo.db.recipes.find({
        "$text": {"$search": str('query')}}
    ))
    
    recommended = mongo.db.recipes.find().sort(
                "favourite_count", -1).limit(6)
    
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        return render_template("recipe/find_recipes.html", 
                               recipes=recipes_paginated, 
                               user=user, 
                               recommended=recommended, 
                               query=query, 
                               pagination=pagination,
                               title="Search Results")
    
    return render_template("recipe/find_recipes.html", 
                           recipes=recipes_paginated, 
                           recommended=recommended, 
                           query=query, 
                           pagination=pagination,
                           title="Search Results")


# ------- Filtered Search for Recipes -------
@app.route("/category_filter/<id>")
def category_filter(id):
    recipes = list(mongo.db.recipes.find({"category": id}))
    
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        return render_template("recipe/find_recipes.html", 
                               recipes=recipes_paginated, 
                               user=user, 
                               pagination=pagination,
                               title="Search Results")
        
    return render_template("recipe/find_recipes.html", 
                           recipes=recipes_paginated,
                           pagination=pagination, 
                           title="Search Results")


@app.route("/difficulty_filter/<id>")
def difficulty_filter(id):
    recipes = list(mongo.db.recipes.find({"difficulty": id}))
    
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        return render_template("recipe/find_recipes.html", 
                               recipes=recipes_paginated, 
                               user=user,
                               pagination=pagination, 
                               title="Search Results")
        
    return render_template("recipe/find_recipes.html", 
                           recipes=recipes_paginated,
                           pagination=pagination, 
                           title="Search Results")


# ------- Register Page -------

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows user to register an account on the database,
    rendering register.html.
    
    Prevention of username duplicates included.
    """
    
    if "user" in session:
    
        return redirect(url_for("my_recipes", 
                                username=session["user"]))
    
    if request.method == "POST":
        # Checks if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get(
                "username").lower()})
        
        # Prevents duplicates
        if existing_user:
            flash("Username already exists, try another")
            return redirect(url_for("register"))
        
        # Sends collected data to user collection
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
            "user_img": request.form.get("user_img"),
            "favourite_recipes": [],
            "is_admin": False
        }
        mongo.db.users.insert_one(register)
        
        # Welcomes user to session
        session["user"] = request.form.get("username").lower()
        flash("Welcome, Baker {}! Let's get started!".format(
            request.form.get("username")))
        return redirect(url_for("my_recipes", 
                                username=session["user"]))
        
    return render_template("user/register.html", 
                           title="Sign Up")


# ------- Login Page -------

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows users to login to account
    """
    
    if "user" in session:
    
        return redirect(url_for("my_recipes", 
                                username=session["user"]))
    
    if request.method == "POST":
        # checking if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username".lower())})
        
        if existing_user:
            # stored hash password must match user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back, {}! Let's get started!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                # if the password does not match
                flash(
                    "Incorrect Username and/or Password, please try again")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash(
                "Incorrect Username and/or Password, please try again")
            return redirect(url_for("login"))
    
    return render_template("user/login.html", 
                           title="Login")


# ------- Logout Page -------

@app.route("/logout")
def logout():
    """
    Allows current session user to log out.
    """
    
    flash("Logged out. See you soon!")
    # User session cookies removal
    session.pop("user")
    return redirect(url_for("login"))


# ------- Edit User Page -------

@app.route("/edit_user/<username>", methods=["GET", "POST"])
def edit_user(username):
    """
    Allows user to edit profile
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    if "user" in session:
        
        # Update profile function
        if request.method == "POST":
            current_user = {
                "username": user["username"],
                "email": user["email"],
                "password": user["password"],
                "user_img": user["user_img"],
                "favourite_recipes": user[
                    "favourite_recipes"],
                "is_admin": user["is_admin"]
            }
            update_user = {
                "username": request.form.get("username"),
                "email": user["email"],
                "password": user["password"],
                "user_img": request.form.get("user_img"),
                "favourite_recipes": user[
                    "favourite_recipes"],
                "is_admin": user["is_admin"]
            }
            
            mongo.db.users.replace_one(
                current_user, update_user, True)
            
            flash("{}'s Profile Updated!".format(
                    request.form.get("username")))
            return redirect(url_for("my_recipes", 
                                    username=session["user"]))
    else:
        return redirect(url_for("login"))

    return render_template("user/edit_user.html", 
                           user=user, 
                           title="Edit User")


# ------- Edit Account Page -------

@app.route("/edit_account/<username>", methods=["GET", "POST"])
def edit_account(username):
    """
    Allows user to edit their account settings
        - Change Password
        - Delete Account
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session:
        
        user = mongo.db.users.find_one(
        {"username": session["user"]})
        
        # Update profile function
        if request.method == "POST":
            current_user = {
                "username": user["username"],
                "email": user["email"],
                "password": user["password"],
                "user_img": user["user_img"],
                "favourite_recipes": user[
                    "favourite_recipes"]
            }
            update_user = {
                "username": user["username"],
                "email": user["email"],
                "password": generate_password_hash(
                    request.form.get("password")),
                "user_img": user["user_img"],
                "favourite_recipes": user[
                    "favourite_recipes"]
            }
            
            mongo.db.users.replace_one(
                current_user, update_user, True)
            
            flash("{}'s Password Updated!".format(
                    request.form.get("username")))
            session.pop("user")
            return render_template("user/login.html", 
                                   title="Login")
    else:
        return redirect(url_for("login"))

    return render_template("user/edit_account.html", 
                           user=user, 
                           title="Edit Account")


# ------- Delete Profile -------

@app.route("/delete_user/<username>")
def delete_user(username):
    """
    Allows user to delete profile
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session:
        mongo.db.users.remove(
            {"username": username.lower()})
        flash("Profile Deleted")
        session.pop("user")
        
        return redirect(url_for("register"))
    
    else:
        return redirect(url_for("login")) 


# ------- My Recipes Page -------

@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    Displays User's recipes page
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session:
        user = mongo.db.users.find_one(
        {"username": session["user"]})
        
        if session["user"] == username:
            recipes = list(
                mongo.db.recipes.find(
                    {"baker": username.lower()}))
            
            recipes_paginated = paginated(recipes)
            pagination = pagination_args(recipes)
        
    else:
        return redirect(url_for("login"))
    
    return render_template("user/my_recipes.html", 
                           user=user, 
                           recipes=recipes_paginated,
                           pagination=pagination, 
                           title="My Recipes")


# ------- My Favourites Page -------

@app.route("/my_favourites/<username>", methods=["GET", "POST"])
def my_favourites(username):
    """
    Displays recipes the user has 'favourited'
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session:
        
        user = mongo.db.users.find_one(
                {"username": session["user"]})
        
        if session["user"] == username:
            recipes = user["favourite_recipes"]
            
            favourites = mongo.db.recipes.find(
                {"_id": {"$in": recipes}})
            
            recommended = mongo.db.recipes.find().sort(
                "favourite_count", -1).limit(4)
            
            recipes_paginated = paginated(favourites)
            pagination = pagination_args(recipes)
    else:
        flash("You must be logged in to see favourites")
        return redirect(url_for("login"))
    
    return render_template("user/my_favourites.html", 
                           user=user, 
                           recommended=recommended, 
                           favourites=recipes_paginated,
                           recipes=recipes,
                           pagination=pagination, 
                           title="My Favourites")
          

# ------- Add to Favourites -------

@app.route("/add_to_favourites/<recipe_id>", methods=["GET", "POST"])
def add_to_favourites(recipe_id):
    """
    Added recipe to the current users 'favourites'
    """
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        
        favourite_recipes = user["favourite_recipes"]
        
        if ObjectId(recipe_id) not in favourite_recipes:
            mongo.db.users.update_one({"username": session["user"]},
                                      {"$push": {
                                          "favourite_recipes" : ObjectId(recipe_id)}})

            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                        {"$inc": {"favourite_count": 1}})
        else: 
            flash("Already Added to favourites")
            return redirect(url_for("recipe", 
                                    recipe_id=recipe_id))
        
    else:
        flash("You must be logged in to add to favourites!")
        return redirect(url_for('login'))
    
    flash("Recipe added to My Favourites")
    
    return redirect(url_for("recipe", 
                            recipe_id=recipe_id))


# ------- Remove From Favourites -------
@app.route("/remove_from_favourites/<recipe_id>", methods=['GET', 'POST'])
def remove_from_favourites(recipe_id):
    """
    Allows user to remove favourited recipe from favourites
    """
    
    user = mongo.db.users.find_one({"username": session["user"]})
    
    favourites = user["favourite_recipes"]
    
    if ObjectId(recipe_id) in favourites:
        mongo.db.users.update({"username": session['user']},
                              {"$pull": {
                                  "favourite_recipes": ObjectId(recipe_id)
                              }})
        
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)},
                                {'$inc': {
                                    'favourite_count': -1
                                }})
        
        flash("Recipe removed from My Favourites")
        return redirect(url_for('recipe', 
                                recipe_id=recipe_id))
    
    else:
        flash("You must be logged in!")
        return redirect(url_for("login"))


# ------- Individual Recipe Page -------

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Displays the full recipe
    """
    
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})

    
    # checking that the user is in session
    if "user" in session:
        user = mongo.db.users.find_one({"username": session["user"]})
        
        favourites = user['favourite_recipes']
        
        if ObjectId(recipe_id) in favourites:
            favourited = True

        else:
            favourited = False

        return render_template("recipe/recipe.html", 
                               recipe=recipe,
                               favourited=favourited, 
                               user=user, 
                               title="Recipe")
        
    else:
        favourited = False
        
    return render_template("recipe/recipe.html", 
                           recipe=recipe, 
                           favourited=favourited, 
                           title="Recipe")


# ------- Create Recipe Page -------

@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    """
    Registered users can upload their favourite recipes.
    """
    
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_img": request.form.get("recipe_img"),
            "recipe_url": request.form.get("recipe_url"),
            "description": request.form.get("description"),
            "category": request.form.get("category"),
            "difficulty": request.form.get("difficulty"),
            "serving": request.form.get("serving"),
            "total_time": request.form.get("total_time"),
            "ingredients": request.form.getlist("ingredients"),
            "directions": request.form.getlist("directions"),
            "baker": session["user"],
            "favourite_count": int(0)
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Shared! Let's get baking!")
        return redirect(url_for(
            "my_recipes", username=session["user"]))
    
    # checking that the user is in session
    if "user" in session:
        
        username = session["user"].lower()
        
        if username == session["user"].lower():
            categories = mongo.db.categories.find().sort("category", 1)
            difficulty = mongo.db.level.find().sort("difficulty", 1)
            return render_template("recipe/create_recipe.html", 
                                   categories=categories, 
                                   difficulty=difficulty, 
                                   user=user, 
                                   title="Create Recipe")
        
        else:
            return redirect(url_for("home"))
    
    else:
        return redirect(url_for("login"))


# ------- Edit Recipe Page -------

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    User can edit the recipe they uploaded
    """
    
    recipe_author = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    if not user_logged_in(recipe_author["baker"]):
        return redirect(url_for("login"))
    
    if request.method == "POST":
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {
                '$set': {
                   "recipe_name": request.form.get("recipe_name"),
                    "recipe_img": request.form.get("recipe_img"),
                    "recipe_url": request.form.get("recipe_url"),
                    "description": request.form.get("description"),
                    "category": request.form.get("category"),
                    "difficulty": request.form.get("difficulty"),
                    "serving": request.form.get("serving"),
                    "total_time": request.form.get("total_time"),
                    "ingredients": request.form.getlist("ingredients"),
                    "directions": request.form.getlist("directions"), 
                }
            })
        flash("{} Recipe Updated!".format(
                    request.form.get("recipe_name")))
        
        return redirect(url_for("recipe", recipe_id=recipe_id))
    
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    
    if "user" in session:
        username = session["user"].lower()
        
        if username == session["user"].lower():
            categories = mongo.db.categories.find().sort("category", 1)
            difficulty = mongo.db.level.find().sort("difficulty", 1)
            return render_template("recipe/edit_recipe.html", 
                                   recipe=recipe, 
                                   categories=categories, 
                                   difficulty=difficulty, 
                                   user=user, 
                                   title="Edit Recipe")
        
        else:
            return redirect(url_for("home"))
    
    else:
        return redirect(url_for("login"))


# ------- Delete Recipe -------

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Allows user to delete their uploaded
    """
    
    if "user" in session:
        
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        
        mongo.db.users.update({},
                              {"$pull": {
                                  "favourite_recipes": ObjectId(recipe_id)}},
                              multi=True)
    else: 
        flash("You must be logged in!")
        return redirect(url_for('login'))
    
    flash("Recipe Deleted")
    return redirect(url_for("my_recipes", 
                            username=session["user"]))


# ------- Error Handlers -------
# adapted from: https://flask.palletsprojects.com/en/1.1.x/errorhandling/

@app.errorhandler(404)
def page_not_found (e):
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("error_handlers/404.html", user=user), 404
    else:
        return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("error_handlers/500.html", user=user), 500
    else:
        return render_template("error_handlers/500.html"), 500


# ------- Declaration of special variables -------

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # MAKE SURE IT IS FALSE

