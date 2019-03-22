from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
<<<<<<< HEAD
from flask_migrate import Migrate
from flask_login import LoginManager
from dating.config import Config

app = Flask(__name__)

app.config.from_object(Config)

=======
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '7ba88159506e7b84bff4420080f75a92'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
>>>>>>> 19a43678fb50b47788319bd99772e72fd928341c
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

<<<<<<< HEAD
from dating import routes , models

def main():
    db.create_all()
=======
db.init_app(app)

def main():
    db.create_all()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from dating import routes
>>>>>>> 19a43678fb50b47788319bd99772e72fd928341c
