import os
#gets the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'app.db')
    #Flask-SQLAlchemy extension takes location of the application's database from SQLALCHEMY_DATABASE_URI configuration variable.
    #takes the database URL from the DATABASE_URL environment variable, if not defined,
    #configure a database named app.db located in the main directory of the application, which is stored in the basedir variable.
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #not signaling application when there are changes in the database
