"""
The `recipes2` blueprint handles displaying recipes.
"""
from flask import Blueprint

recipes2_blueprint = Blueprint('recipes2', __name__, template_folder='templates')

from . import routes
