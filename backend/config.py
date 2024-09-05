from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# allows us to connect the frontend and backend
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# stores a file that is a sqlite database and saved to the name
db = SQLAlchemy(app)