from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from dating.config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
migrate = Migrate(app, db)
login.login_view = 'login'
login.login_message_category = 'info'


from dating import routes, models

def main():
    db.create_all()
