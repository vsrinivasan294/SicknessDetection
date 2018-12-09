import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from InfoBlog import app, db, bcrypt
from InfoBlog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from InfoBlog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
def main():
	return render_template('main.html', title='Main')

@app.route("/home")
def home():
    image_file = url_for('static', filename='images/blood_samples/' + current_user.image_file)
    return render_template('home.html', image_file=image_file)

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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = current_user.username + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/blood_samples', picture_fn)
    form_picture.save(picture_path)

    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/blood_samples/' + current_user.image_file)
    return render_template('account.html', title='Account',
                            image_file=image_file, form=form)

@app.route("/HIV-Information")
def HIV():
    return render_template('HIV-Information.html', title='Information')

@app.route("/Leukemia-Information")
def leukemia():
    return render_template('Leukemia-Information.html', title='Information')

@app.route("/Malaria-Information")
def malaria():
    return render_template('Malaria-Information.html', title='Information')

@app.route("/Sickle-Information")
def sickle():
    return render_template('sickle-Information.html', title='Information')
