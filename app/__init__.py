from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from .config import Config
from .database import db
from .auth import auth
from .ideas import ideas
from .users import users
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(username):
    return UserModel.get(username)

def create_app():
    """ Método para la creación de la app de Flask. """
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    fa = FontAwesome(app)
    
    app.config.from_object(Config)
    app.register_blueprint(auth)
    app.register_blueprint(ideas)
    app.register_blueprint(users)

    login_manager.init_app(app)
    
    db.init_app(app)
    return app
