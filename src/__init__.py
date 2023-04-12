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
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_socketio import SocketIO

# Set up logging
# file_handler = FileHandler('app.log')
# logger = logging.getLogger('werkzeug')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)

### Flask extension objects instantiation ###
### Instantiate Celery ###

def create_app():
    sentry_sdk.init(
        dsn="https://432f5de8a8784e9c811b13a9e18553e9@o1423025.ingest.sentry.io/4504576404094976",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        environment='local',
        send_default_pii=True
    )
    app = Flask(__name__) 
    CORS(app, resources={r"/*": {"origins": r"http://localhost/*"}})
    
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
    # app.wsgi_app = CustomMiddleWare(app.wsgi_app)
    
    #Set up logging
    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    return app

# app = create_app()

def socket():
    socketio = SocketIO(create_app(), cors_allowed_origins='*')
    return socketio




