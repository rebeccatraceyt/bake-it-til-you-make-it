import os
from functools import wraps
from flask import (
        Flask, flash, render_template, 
        redirect, request, session, url_for)
from flask_pymongo import PyMongo
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

def login_required(f):
    """
    Function checks login status of current user.
    Referenced from CI/UCD Masterclass
    https://github.com/TravelTimN/flask-task-manager-project/tree/demo
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not "user" in session:
            flash("You must log in to view this page")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ------- Home Page -------

@app.route("/")
@app.route("/home")
def home():
    """
    Home page displays the 4 latest recipes
    """
    
    latest_recipes = mongo.db.recipes.find().sort("_id", 1).limit(4)
    
    return render_template(
        "index.html", 
        recipes=latest_recipes, title="Home")


# ------- Find Recipes Page -------
@app.route("/find_recipes")
def find_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipe/find_recipes.html", recipes=recipes)


# ------- Search for Recipes -------
@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({
        "$text": {"$search": query}}
    ))
    recommended = mongo.db.recipes.find().sort(
                "favourite_count", -1).limit(6)
    
    if len(recipes) == 0:
        flash(f"No recipe results for {query}")
        
    else:
        flash(f"Your search for {query} returned {len(recipes)} result(s)!")
    
    return render_template("find_recipes.html", recipes=recipes, recommended=recommended)


# ------- Filtered Search for Recipes -------
@app.route("/category_filter/<id>")
def category_filter(id):
    recipes = list(mongo.db.recipes.find({"category": id}))
    return render_template("recipe/find_recipes.html", recipes=recipes)


@app.route("/difficulty_filter/<id>")
def difficulty_filter(id):
    recipes = list(mongo.db.recipes.find({"difficulty": id}))
    return render_template("recipe/find_recipes.html", recipes=recipes)


# ------- Register Page -------

@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows user to register an account on the database,
    rendering register.html.
    
    Prevention of username duplicates included.
    """
    if "user" not in session:
        
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
                "favourite_recipes": []
            }
            mongo.db.users.insert_one(register)
            
            # Welcomes user to session
            session["user"] = request.form.get("username").lower()
            flash("Welcome, Baker {}!".format(
                request.form.get("username")))
            return redirect(url_for(
                "my_recipes", username=session["user"]))
        return render_template("user/register.html")

    return redirect(url_for("my_recipes", username=session["user"]))


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
    
    return render_template("user/login.html")


# ------- Logout Page -------

@app.route("/logout")
@login_required
def logout():
    """
    Allows current session user to log out.
    """
    
    flash("See you soon Baker {}".format(
        request.form.get("username")))
    # User session cookies removal
    session.pop("user")
    return redirect(url_for("login"))


# ------- Edit User Page -------

@app.route("/edit_user/<username>", methods=["GET", "POST"])
@login_required
def edit_user(username):
    """
    Allows user to edit profile
    """
    
    if session["user"].lower() == username.lower():
        
        user = mongo.db.users.find_one(
            {"username": username})
    
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
                "username": request.form.get("username"),
                "email": user["email"],
                "password": generate_password_hash(
                    request.form.get("password")),
                "user_img": request.form.get("user_img"),
                "favourite_recipes": user[
                    "favourite_recipes"]
            }
            
            mongo.db.users.replace_one(
                current_user, update_user, True)
            
            flash("Profile Updated!")
            return render_template(
                "user/login.html", user=user)

    return render_template(
        "user/edit_user.html", user=user)


# ------- Delete Profile -------

@app.route("/delete_user/<username>")
@login_required
def delete_user(username):
    """
    Allows user to delete profile
    """
    
    if session["user"].lower() == username.lower():
        
        mongo.db.users.remove(
           {"username": username.lower()})
        flash("Profile Deleted")
        session.pop("user")
        
        return redirect(url_for("register"))
    
    return redirect(url_for("login")) 


# ------- My Recipes Page -------

@app.route("/my_recipes/<username>", methods=["GET", "POST"])
@login_required
def my_recipes(username):
    """
    Displays User's recipes page
    """
    
    if session["user"].lower() == username.lower():
        user = mongo.db.users.find_one(
            {"username": username})
        recipes = list(
            mongo.db.recipes.find(
                {"baker": username.lower()}))
        
        return render_template(
            "user/my_recipes.html",
            user=user, recipes=recipes)
    
    # Takes user to their own account (if not their's) 
    return redirect(url_for("my_recipes", username=session["user"]))


# ------- My Favourites Page -------

@app.route("/my_favourites/<username>", methods=["GET", "POST"])
@login_required
def my_favourites(username):
    """
    Displays recipes the user has 'favourited'
    """
    
    if session["user"].lower() == username.lower():
        user = mongo.db.users.find_one(
            {"username": session["user"]})
    
        favourite_recipes = user["favourite_recipes"]
            
        favourites = mongo.db.recipes.find(
                {"_id": {"$in": favourite_recipes}})
            
        recommended = mongo.db.recipes.find().sort(
                "favourite_count", -1).limit(3)

        return render_template("user/my_favourites.html", user=user, 
                           recommended=recommended, favourites=favourites,
                           favourite_recipes=favourite_recipes)
    
    return redirect(url_for("my_favourites", username=session["user"]))
          

# ------- Add to Favourites -------

@app.route("/add_to_favourites/<recipe_id>", methods=["GET", "POST"])
@login_required
def add_to_favourites(recipe_id):
    """
    Added recipe to the current users 'favourites'
    """
        
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    
    favourite_recipes = user["favourite_recipes"]
        
    if ObjectId(recipe_id) not in favourite_recipes:
        mongo.db.users.update_one({"username": session["user"]},
                        {"$push": {
                            "favourite_recipes" : ObjectId(recipe_id)}})

        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
                                    {"$inc": {"favourite_count": 1}})
        
        flash("Added to my favourites")
        return redirect(url_for("recipe", recipe_id=recipe_id))
    else: 
        flash("Already Added to favourites")
        return redirect(url_for("recipe", recipe_id=recipe_id))
    
    flash("You must be logged in to add to favourites!")
    return redirect(url_for('login'))


# ------- Remove From Favourites -------
@app.route("/remove_from_favourites/<recipe_id>", methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('recipe', recipe_id=recipe_id))

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
        user = mongo.db.users.find_one({"username": session['user']})
        favourites = user['favourite_recipes']
        
        if ObjectId(recipe_id) in favourites:
            favourited = True

        else:
            favourited = False
    
    else:
        favourited = False
        
    return render_template(
        "recipe/recipe.html", recipe=recipe, 
        favourited=favourited, title="Recipe")


# ------- Create Recipe Page -------

@app.route("/create_recipe", methods=["GET", "POST"])
@login_required
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
            "baker": session["user"],
            "favourite_count": int(0)
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Shared")
        return redirect(url_for(
            "my_recipes", username=session["user"]))
    
    categories = mongo.db.categories.find().sort("category", 1)
    difficulty = mongo.db.level.find().sort("difficulty", 1)
    return render_template(
        "recipe/create_recipe.html", 
        categories=categories, difficulty=difficulty)


# ------- Edit Recipe Page -------

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    User can edit the recipe they uploaded
    """
    
    recipe_author = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    
    if session["user"].lower() == recipe_author["baker"].lower():
            
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
            flash("Recipe Updated!")
            return redirect(url_for("recipe", recipe_id=recipe_id))
    
        recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})

        categories = mongo.db.categories.find().sort("category", 1)
        difficulty = mongo.db.level.find().sort("difficulty", 1)
        return render_template(
            "recipe/edit_recipe.html", 
            recipe=recipe, categories=categories, difficulty=difficulty)
        
    
    flash("You do not have access to edit this recipe")
    return redirect(url_for('recipe', recipe_id=recipe_id))


# ------- Delete Recipe -------

@app.route("/delete_recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """
    Allows user to delete their uploaded
    """
    
    recipe_author = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    
    if session["user"].lower() == recipe_author["baker"].lower():    
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        mongo.db.users.update({},
                              {"$pull": {
                                  "favourite_recipes": ObjectId(recipe_id)}},
                              multi=True)
        
        flash("Recipe Deleted")
        return redirect(url_for("my_recipes", username=session["user"]))

    flash("You do not have access to delete this recipe")
    return redirect(url_for('recipe', recipe_id=recipe_id))
    
    


# ------- Declaration of special variables -------

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # MAKE SURE IT IS FALSE

