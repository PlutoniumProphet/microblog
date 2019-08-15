"""A microblog tutorial from https://blog.miguelgrinberg.com/"""
# from app package import app (instance of Flask class)
from app import app

# FLASK_APP=microblog.py doesn't persist across terminal session
# so install python-dotenv and add to .flaskenv at top level file
