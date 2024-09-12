from flask import request, jsonify, redirect, url_for, render_template, session, flash
import requests
from .config import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import UserAccount
import os
from dotenv import load_dotenv

load_dotenv()

def handle_workouts_api():
    wger_workouts_key = os.getenv("WGER_API_KEY")
    exercises_url = 'https://wger.de/api/v2/exercise/'

    headers = {
        "Authorization": f"Token {wger_workouts_key}"
    }
    params = {
        "language": 2
    }
    wger_key_response = requests.get(exercises_url, headers=headers, params=params)
    print(wger_key_response.json())

def exercise_obj_creator():
    pass
def wp_obj_creator():
    pass

@app.route("/create-user", methods=["POST"])
def create_user():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    if not first_name or not last_name or not username or not email or not password:
         flash("You must include: ", "error")
         flash("First Name", "info")
         flash("Last Name", "info")
         flash("Email", "info")
         flash("Username", "info")
         flash("Password", "info")
         return redirect(url_for("notifications"))
    
    new_user = UserAccount(first_name=first_name, last_name=last_name, email=email, username=username, password=generate_password_hash(password))
    #SQLAlchemy models inherit from db.Model, which includes a default __init__ method. This method allows you to set attributes directly 
    #by passing keyword arguments that correspond to the column names in the model.
    #the keyword arguments match the column names defined in the model. The default constructor sets these attributes directly.
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('notifications'))
    
    flash("User Created Successfully!", "success")
    flash(f"User ID: {new_user.getID()}", "info")
    flash(f"First Name: {new_user.getFirstName()}", "info")
    flash(f"Last Name: {new_user.getLastName()}", "info")
    flash(f"Username: {new_user.getUserName()}", "info")
    flash(f"Email: {new_user.getEmail()}", "info")

    return redirect(url_for('notifications'))

    # these are all returned as json objects so the frontend can retrieve and display it
@app.route('/login', methods=['POST', "GET"])
def login():
    entered_username = request.form.get('username')
    entered_password = request.form.get('password')

    attempted_user = UserAccount.query.filter_by(username=entered_username).first()
    # the account table represents a table in the database and its filtered by the attempted username and returns the first occurence of it
    if attempted_user == None:
        flash("Username not found.", "error")
        return redirect(url_for('notifications'))
    
    if check_password_hash(attempted_user.getPassword(), entered_password):
        # first argument is a stored hash and the second is the hashed version of the other password
        session["logged_in"] = True
        session["username"] = attempted_user.getUserName()
        flash("The username is correct, successful login!", "success")
        return redirect(url_for('notifications'))
    else:
        flash("Please enter the correct password")
        return redirect(url_for('notifications'))
    
@app.route('/logout')
def logout():
    # comeback to the logout system
    pass
    
@app.route('/notifications')
def notifications():
    return render_template("notifications.html")

@app.route('/')
# the above url '/' is the base url for the website
def index():
    return render_template('index.html')
    # flask automatically looks in the templates directory
    # flask environment is activated and run so it listens for http requests and whenever one is sent it is handled appropriately

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/workout-plans')
def workoutPlans():
    return render_template('workoutplans.html')

@app.route('/meal-plans')
def mealPlans():
    return render_template('mealplans.html')

@app.route('/exercise-library')
def exerciseLibrary():
    return render_template('exercises.html')

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        # checks if we have the database and if we dont we are going to create it

    app.run(debug=True)