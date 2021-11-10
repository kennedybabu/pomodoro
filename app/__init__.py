from flask import Flask
from .config import DevConfig

#initialising the app
app = Flask(__name__)

#setting up configurations
app.config.from_object(DevConfig)

from app import views