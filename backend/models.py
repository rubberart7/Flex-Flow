from config import db
#imports the db object from the config module and db is an instance of SQLAlchemy

class UserAccount(db.Model):
    # this class UserAccount inherits from db.Model and UserAccount becomes an SQLAlchemy model, meaning each instance is a table in the database
    # below defines columns for each value, it stores the type, primary_key=true ensures that each user has a unique primary key
    # nullable=false means that it cannot be left empty and unique=false means it can be the same which means multiple users can have the same first and last names
    #multiple users in the table cannot have the same email though
    id = db.Column(db.Integer, primary_key=True)
    #in sqlachemy when a column is defined as a primary key and uses an integer type its automatically set to auto-increment by defulat, new row starts at 1 and increments for each row
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    # add stuff for the username and password later

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getEmail(self):
        return self.email

    def getUserName(self):
        return self.username

    def getPassword(self):
        return self.password
    
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.password,
            "email": self.email
        }

class WorkoutPlan():
    def __init__(self, name, description, muscle_groups, sets, reps):
        self.__name = name
        self.__description = description
        self.__muscle_groups = muscle_groups
        self.__sets = sets
        self.__reps = reps
        

class Exercise():
    def __init__(self, name, description, muscle_groups, sets, reps):
        self.__name = name
        self.__description = description
        self.__muscle_groups = muscle_groups
        self.__sets = sets
        self.__reps = reps
    # allows me to send a json representation of the object to the frontend