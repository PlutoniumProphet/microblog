"""This is the routing module for flask application"""
from flask import render_template
from app import app

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
