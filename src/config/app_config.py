import os
import uuid
from datetime import timedelta

class Config:
    SECRET_KEY=os.getenv('SECRET_KEY', default='')
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', default='')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    JWT_SECRET_KEY='secret_key'
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(hours=5)
    # JWT_EXPIRATION_DELTA = timedelta(days=10)
    
    BROKER_URL = os.getenv('CELERY_BROKER_URL', default='')
    RESULT_BACKEND = os.getenv('RESULT_BACKEND', default='')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_USE_TLS =  True
    # MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', default=True)
    print("Environment created successfully!!!")
    