from flask import Flask
from config import Config

# defined as an instance of Flask class making it a member of app package
app = Flask(__name__)
app.config.from_object(Config)

# imported at the bottom as a work around for circular imports
from app import routes
