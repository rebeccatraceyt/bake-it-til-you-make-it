import os
from flask import (
        Flask, flash, render_template, 
        redirect, request, session, url_for)
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ------- Check User Login Function -------

def user_logged_in(username):
    """
    Function checks login status of current user.
    """
    if "user" in session.keys():
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
    latest_recipes = mongo.db.recipes.find().sort('_id', DESCENDING).limit(4)
    return render_template(
        "index.html", latest_recipes=latest_recipes, title="Home")


# ------- Register Page -------

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows user to register an account on the database,
    rendering register.html.
    
    Prevention of username duplicates included.
    """
    
    if request.method == "POST":
        # Checks if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        # Prevents duplicates
        if existing_user:
            flash("Username already exists, try another")
            return redirect(url_for("register"))
        
        # Sends collected data to user collection
        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_img": request.form.get("user_img"),
            "favourite_recipes": []
        }
        mongo.db.users.insert_one(register)
        
        # Welcomes user to session
        session["user"] = request.form.get("username").lower()
        flash("Welcome, Baker {}!".format(
            request.form.get("username")))
        return redirect(url_for("profile", username=session["user"]))
    return render_template("/user/register.html")


# ------- Login Page -------

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows users to login to account
    """
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
                flash("Welcome back, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # if the password does not match
                flash("Incorrect Username and/or Password, please try again")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password, please try again")
            return redirect(url_for("login"))
    
    return render_template("/user/login.html")


# ------- Logout Page -------

@app.route("/logout")
def logout():
    flash("See you soon Baker {}".format(
        request.form.get("username")))
    # User session cookies removal
    session.pop("user")
    return redirect(url_for("login"))


# ------- Profile Page -------

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Displays User's recipes page
    """
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session.keys():
        if session["user"] == username:
            recipes = list(
                mongo.db.recipes.find({"baker": username.lower()}))
        
    else:
        return redirect(url_for("login"))
    
    return render_template(
        "/user/profile.html", user=user, recipes=recipes)


# ------- Edit Profile Page -------

@app.route("/edit_user/<username>", methods=["GET", "POST"])
def edit_user(username):
    """
    Allows user to edit profile
    """
    
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session.keys():
        # Update profile function
        if request.method == "POST":
            current_user = {
                "username": user["username"],
                "email": user["email"],
                "password": user["password"],
                "user_img": user["user_img"],
                "favourite_recipes": user["favourite_recipes"]
            }
            update_user = {
                "username": request.form.get("username"),
                "email": user["email"],
                "password": generate_password_hash(request.form.get("password")),
                "user_img": request.form.get("user_img"),
                "favourite_recipes": user["favourite_recipes"]
            }
            
            mongo.db.users.replace_one(
                current_user, update_user, True)
            # replace used - issue with update
            
            flash("Profile Updated!")
            return render_template("/user/login.html", user=user)
    else:
        return redirect(url_for("login"))

    return render_template(
        "/user/edit_user.html", user=user)


# ------- Delete Profile Page -------

@app.route("/delete_user/<username>")
def delete_user(username):
    """
    Allows user to delete profile
    """
    
    if not user_logged_in(username.lower()):
        return redirect(url_for("login"))
    
    if "user" in session.keys():
        mongo.db.users.remove(
            {"username": username.lower()})
        flash("Profile Deleted")
        session.pop("user")
        
        return redirect(url_for("register"))
    
    else:
        return redirect(url_for("login")) 


# ------- Individual Recipe Page -------

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Displays the full recipe
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "/recipe/recipe.html", recipe=recipe, title="Recipe")


# ------- Create Recipe Page -------

@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    """
    Registered users can upload their favourite recipes.
    """
    
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
            "baker": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Shared")
        return redirect(url_for("profile", username=session["user"]))
    
    # checking that the user is in session
    if "user" in session:
        user = session["user"].lower()
        
        if user == session["user"].lower():
            categories = mongo.db.categories.find().sort("category", 1)
            difficulty = mongo.db.level.find().sort("difficulty", 1)
            return render_template("/recipe/create_recipe.html", categories=categories, difficulty=difficulty)
        
        else:
            return redirect(url_for("home"))
    
    else:
        return redirect(url_for("login"))
    

# ------- Declaration of special variables -------

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # MAKE SURE IT IS FALSE

