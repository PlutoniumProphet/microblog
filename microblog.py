"""A microblog tutorial from https://blog.miguelgrinberg.com/"""
# from app package import app (instance of Flask class)
from app import app, db
from app.models import User, Post
from app import cli


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# FLASK_APP=microblog.py doesn't persist across terminal session
# so install python-dotenv and add to .flaskenv at top level file
