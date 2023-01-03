from flask import Flask, render_template
from flask_migrate import Migrate
from src.config.app_config import Config
from src.models import models_list
from src.middleware import CustomMiddleWare
from src.blueprint import blueprint_list
from src.db import db
# from src.learning.views import testing
from src.celery_woker import celery
from src.mail import mail
from flask_login import LoginManager
from src.authentication.models import User
from flask_jwt_extended.jwt_manager import JWTManager
from src.social_login.github_login import make_github_blueprint
from datetime import timedelta
import logging
from logging import FileHandler

# Set up logging
# file_handler = FileHandler('app.log')
# logger = logging.getLogger('werkzeug')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)

### Flask extension objects instantiation ###
### Instantiate Celery ###

def create_app():
    app = Flask(__name__) 

    JWTManager(app)
    
    # app.config.from_mapping(
    #     JWT_SECRET_KEY='secret_key',
    #     JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1),
    #     JWT_REFRESH_TOKEN_EXPIRES=timedelta(hours=5))
    config = Config()
    app.config.from_object(config)      
    
    # celery.conf.update(app.config) 
    celery.conf.update(app.config)
    
    mail.init_app(app)
    
    #Registering Blueprints
    for bp in blueprint_list:
        app.register_blueprint(bp)  
    # blueprint_list.append(github_blueprint)

    # login_manager = LoginManager(app)

    Migrate(app, db)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    #Registering middleware
    app.wsgi_app = CustomMiddleWare(app.wsgi_app)
    
    #Set up logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    return app

app = create_app()
# login_manager = app.login_manager
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# def initialize_extensions(app):
    # Configure celery
    
