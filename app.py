from logging import debug
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


@app.route("/")
@app.route("/home")
def home():
    """
    Home page displays the 4 latest recipes
    """
    latest_recipes = mongo.db.recipes.find().sort('_id', DESCENDING).limit(4)
    return render_template(
        "index.html", latest_recipes=latest_recipes, title="Home")


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
            {"username": request.form.get("username").lower()}
        )
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
        flash("Welcome, Baker {}!".format(request.form.get("username")))
        return redirect(url_for("home", username=session["user"]))
    return render_template("register.html")


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """
    Displays the full recipe
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe.html", recipe=recipe, title="Recipe")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # MAKE SURE IT IS FALSE

