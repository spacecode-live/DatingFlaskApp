from dating import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#The purpose of this field is to hold a hash of the user password, which will be used to verify the password entered
#by the user during the login process. werkzeug is a package that implements password hashing.

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
#Flask-Login knows nothing about databases, it needs the application's help in loading a user.
#configure a user loader function that can be called to load a user given the ID.
#The user loader is registered with Flask-Login with the @login.user_loader decorator.

class User(db.Model, UserMixin):  #This class defines several fields as class variables.
    """ User of the Dating website."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    #profile_picture = db.Column(db.String(250), default = 'default.jpg', nullable=True)

    def _repr_(self): #The __repr__ method tells Python how to print objects of this class
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
