"""This is the routing module for flask application"""
from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    """function prescribes behaviour for the index page"""
    user = {'username': 'Graham'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)


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
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
