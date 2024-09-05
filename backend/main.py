from flask import request, jsonify, redirect, url_for, render_template
from config import app, db
from models import UserAccount




@app.route('/')
# the above url '/' is the base url for the website
def index():
    return render_template('index.html')
    # flask automatically looks in the templates directory
    # flask environment is activated and run so it listens for http requests and whenever one is sent it is handled appropriately

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # checks if we have the database and if we dont we are going to create it

    app.run(debug=True)