from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from dating.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2, max = 20)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min = 1, max = 100)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min = 1, max = 100)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
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

class Profile(FlaskForm):
    firstname = StringField('First name', validators = [DataRequired()])
    lastname = StringField('Last name', validators = [DataRequired()])
    age = IntegerField('Age', validators = [DataRequired()])
    birth_day = StringField('Birth day', validators = [DataRequired()])
    about_me = StringField('About me', Length(min = 100, max = 500))
