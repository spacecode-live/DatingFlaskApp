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
from dating import db, login_manager
from flask_login import UserMixin

db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
>>>>>>> 19a43678fb50b47788319bd99772e72fd928341c
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
