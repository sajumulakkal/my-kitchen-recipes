# recipes1/__init__.py
"""
The `recipes1` blueprint handles displaying recipes.
"""
from flask import Blueprint

recipes1_blueprint = Blueprint('recipes1', __name__, template_folder='templates')

# Import the routes module
from . import routes

# Rest of the code remains the same
