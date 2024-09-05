from flask import request, jsonify, redirect, url_for, render_template
from config import app, db
from models import UserAccount



@app.route('/')
def index():
    return render_template('index.html')
    # flask automatically looks in the templates directory

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # checks if we have the database and if we dont we are going to create it

    app.run(debug=True)