"""This is the routing module for flask application"""
from flask import flash, redirect, render_template, request, url_for
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, login_required, logout_user
from app import db
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    """function prescribes behaviour for the index page"""
    posts = [
        {
            'author': {'username': 'John'},
            'body': '''
                    Lorem ipsum dolor sit amet consectetur adipiscing elit
                    orci nulla elementum sagittis id, condimentum curae feugiat
                    fusce sociis maecenas risus arcu convallis posuere mollis.
                    Ut cum nostra dis in lacus consequat eget mattis, eros
                    pellentesque dapibus scelerisque aliquet vehicula tellus
                    primis, nisi commodo parturient malesuada velit massa
                    interdum. At non tortor porttitor faucibus vivamus per
                    placerat, suscipit sed congue penatibus sollicitudin
                    fermentum natoque, auctor molestie nisi nunc et dui.
                    '''
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
