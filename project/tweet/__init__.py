"""
The `tweet` blueprint handles displaying tweet posts.
"""
from flask import Blueprint

tweet_blueprint = Blueprint('tweet', __name__, template_folder='templates')

from . import routes
