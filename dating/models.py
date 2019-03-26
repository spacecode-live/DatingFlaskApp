from dating import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):  #This class defines several fields as class variables.
    """ User of the Dating website."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False, unique=True)

    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=True)
    zipcode = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(100), nullable=True)
    profile_picture = db.Column(db.String(250), default = 'default.jpg', nullable=True)

    def _repr_(self): #The __repr__ method tells Python how to print objects of this class
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Profile()(db.Model):
    """ The profile page of a user """
    __tablename__ = 'profiles'
