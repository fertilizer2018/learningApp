from flask import Blueprint

home = Blueprint('homesite', __name__)

from . import views