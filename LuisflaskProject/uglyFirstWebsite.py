from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '548b8164d29197e8d08e68f7bb43fa94'

posts = [
    {
        'author': 'Samarth Jain',
        'title': 'Blog Post 1',
        'content': 'hello, my name is Sam.',
        'date_posted': 'October 18, 2018'
    },
    {
    'author': 'Luis Rendon',
    'title': 'Blog Post 2',
    'content': 'Hello, this is my blog post.',
    'date_posted': 'April 20, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)