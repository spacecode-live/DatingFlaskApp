<<<<<<< HEAD
from dating import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
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

    def _repr_(self):
=======
from flask_sqlalchemy import SQLAlchemy
from dating import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(100), nullable=True)
    lname = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_picture = db.Column(db.String(250), nullable=True, default='default.jpg')
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=True)
    zipcode = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(100), nullable=True)

    def __repr__(self):
>>>>>>> 19a43678fb50b47788319bd99772e72fd928341c
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
