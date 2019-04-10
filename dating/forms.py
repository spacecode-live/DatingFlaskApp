from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dating.models import *

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min = 1, max = 100)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min = 1, max = 100)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    date_of_birth = StringField('Date Of Birth (MM/DD/YYYY)', validators=[DataRequired(), Length(min = 2, max = 20)] )
    city = StringField('City', validators=[DataRequired(), Length(min = 2, max = 300)] )
    phone = StringField('Phone (XXX)-(XXX)-(XXXX)', validators=[DataRequired(), Length(min = 10, max = 12)] )
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('RememberMe')
    submit = SubmitField('Login')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    city = StringField('City', validators=[DataRequired(), Length(min = 2, max = 300)] )
    phone = StringField('Phone (XXX)-(XXX)-(XXXX)', validators=[DataRequired(), Length(min = 10, max = 12)] )
    profilepic = FileField('Add Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

class InterestForm(FlaskForm):
    book_genres = StringField('Book Genre', validators=[DataRequired(), Length(min = 2, max = 200)] )
    movie_genres = StringField('Movie Genre', validators=[DataRequired(), Length(min = 2, max = 200)])
    music_genre = StringField('Music Genre', validators=[DataRequired(), Length(min = 2, max = 200)])
    fav_cuisine = StringField('Favorite Cuisine', validators=[DataRequired(), Length(min = 2, max = 200)])
    hobby = StringField('Hobby', validators=[DataRequired(), Length(min = 2, max = 200)])
    outdoors = StringField('Outdoors', validators=[DataRequired(), Length(min = 2, max = 200)])
    religion = StringField('Religion', validators=[DataRequired(), Length(min = 2, max = 200)])
    submit = SubmitField('Submit')
