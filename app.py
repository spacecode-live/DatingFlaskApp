from flask import Flask, render_template, url_for

app = Flask(__name__)

cards = [
{ 'name': 'Selina Mangaroo', 'age': '20'},
{ 'name': 'Alexandra Baybay', 'age': '21'}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', cards=cards)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
