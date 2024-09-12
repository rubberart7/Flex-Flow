from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
"""
#creates an instance of the flask class __name__ argument helps Flask determine the 
#root path of the application and locate resources such as templates and static files.
"""
CORS(app)
# allows us to connect the frontend and backend, allows Flask application to accept requests from diff origins(domains) useful for backend and frotend being hosted on diff domains or ports
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# This specifies that you are using SQLite as the database engine, and the database file will be named mydatabase.db in the root directory of your project.

db = SQLAlchemy(app)
#Creates an instance of SQLAlchemy and binds it to the Flask application instance (app). 
# This sets up the connection between Flask and SQLAlchemy and allows you to interact with the database