from flask import Flask, render_template, url_for
from app.models import User, example_data

app = Flask(__name__)

cards = [
{ 'name': 'Daenerys Targaryen', 'age': '18'},
{ 'name': 'Jon Snow', 'age': '22'},
{ 'name': 'Tyrion Lannister', 'age': '24'},
{ 'name': 'Missandei', 'age': '22'},
{ 'name': 'Podrick Payne', 'age' : '18'}
]

@app.route("/")
def index():
    return render_template('home.html', cards=cards)

@app.route("/home")
def home():
    return render_template('home.html', cards=cards)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
