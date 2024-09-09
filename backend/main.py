from flask import request, jsonify, redirect, url_for, render_template
from config import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from models import UserAccount


def get_accounts():
    accounts = UserAccount.query.all()
    # gets a list of all UserAccount objects
    return accounts

@app.route("/create-user", methods=["POST"])
def create_user():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    if not first_name or not last_name or not username or not email or not password:
         info = """You must include:
        - First name 
        - Last name
        - Username
        - Email
        - Password"""
         return render_template('signup.html', info=info)
    
    new_user = UserAccount(first_name=first_name, last_name=last_name, email=email, username=username, password=generate_password_hash(password))
    #SQLAlchemy models inherit from db.Model, which includes a default __init__ method. This method allows you to set attributes directly 
    #by passing keyword arguments that correspond to the column names in the model.
    #the keyword arguments match the column names defined in the model. The default constructor sets these attributes directly.
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        info=f"Error: {str(e)}"
        return render_template('signup.html', info=info)
    
    info = "User Created Successfully!"
    info += f"User ID: {new_user.getID()}"
    info += f" First Name: {new_user.getFirstName()}"
    info += f" Last Name: {new_user.getLastName()}"
    info += f" Username: {new_user.getUserName()}"
    info += f" Email: {new_user.getEmail()}"
    info += f" Password: {new_user.getPassword()}"

    return render_template('signup.html', info=info)

    # these are all returned as json objects so the frontend can retrieve and display it
@app.route('/login', methods=['POST'])
def login():
    entered_username = request.form.get('username')
    entered_password = request.form.get('password')

    attempted_user = None
    accounts = get_accounts()

    for user in accounts:
        if user.getUserName() == entered_username:
            attempted_user = user
    if attempted_user == None:
        return "Username not found"
    
    if check_password_hash(attempted_user.getPassword(), entered_password):
        # firs argument is a stored hash and the second is the hashed version of the other password
        return "The username is correct, successful login!"
    else:
        return "Please enter the correct password"

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