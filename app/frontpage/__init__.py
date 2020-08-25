from flask import Blueprint

bp = Blueprint('frontpage', __name__)

from . import routes
