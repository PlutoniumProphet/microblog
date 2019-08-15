from flask import Flask

# defined as an instance of Flask class making it a member of app package
app = Flask(__name__)

# imported at the bottom as a work around for circular imports
from app import routes
