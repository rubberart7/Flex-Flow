from flask import request, jsonify, redirect, url_for, render_template
from config import app, db
from models import UserAccount

@app.route("/accounts", methods=["GET"])
def get_accounts():
    accounts = UserAccount.query.all()
    #gets all of the accounts and places them in a list
    json_accounts = list(map(lambda account: account.to_json(), accounts))
    #for each account in the accounts list it turns them into json object and each is in the map object, so the map object is turned into a list instead
    return jsonify({"accounts": json_accounts})
    #converted into json data

@app.route("/create-user", methods=["POST"])
def create_user():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    if not first_name or not last_name or not username or not email or not password:
        return (jsonify({"message": "You must include first name, last name, username, email and password"}), 400)
        #returns error message and response error code is 400
    
    new_user = UserAccount(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    #SQLAlchemy models inherit from db.Model, which includes a default __init__ method. This method allows you to set attributes directly 
    #by passing keyword arguments that correspond to the column names in the model.
    #the keyword arguments match the column names defined in the model. The default constructor sets these attributes directly.
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"messsage": str(e)}), 400
    
    return jsonify({"messasge": "User Created!"}), 201
    # these are all returned as json objects so the frontend can retrieve and display it

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
        db.create_all()
        # checks if we have the database and if we dont we are going to create it

    app.run(debug=True)