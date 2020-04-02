from flask import Blueprint

auth = Blueprint('auth', __nam__)

from . import views