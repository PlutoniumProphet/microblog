"""This is the routing module for flask application"""
from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm


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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
