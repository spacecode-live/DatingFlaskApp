from flask import render_template, url_for, flash, redirect
from dating import app
from dating.forms import RegistrationForm, LoginForm
from dating.models import *

cards = [
{ 'name': 'Daenerys Targaryen', 'age': '18'},
{ 'name': 'Jon Snow', 'age': '22'},
{ 'name': 'Tyrion Lannister', 'age': '24'},
{ 'name': 'Missandei', 'age': '22'},
{ 'name': 'Podrick Payne', 'age' : '18'}
]

@app.route("/")
def index():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route("/home")
def home():
    return render_template('home.html', cards=cards)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
