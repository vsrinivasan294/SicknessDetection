from flask import render_template, url_for, flash, redirect
from InfoBlog import app, db, bcrypt
from InfoBlog.forms import RegistrationForm, LoginForm
from InfoBlog.models import User, Post
from flask_login import login_user, current_user

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/HIV-Information")
def HIV():
    return render_template('HIV-Information.html', title='Information')