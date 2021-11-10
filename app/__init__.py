from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#initialising the app
app = Flask(__name__)

#setting up configurations
app.config.from_object(DevConfig)

#Initialise bootstrap
bootstrap = Bootstrap(app)

from app import views