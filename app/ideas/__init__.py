from flask import Blueprint

ideas = Blueprint('ideas', __name__, url_prefix='/ideas', template_folder='templates')

from . import views