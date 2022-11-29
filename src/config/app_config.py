import os
from flask import Flask

class Config:
    SECRET_KEY='dev'
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI', None)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # JWT_SECRET_KEY=''
    # JWT_ACCESS_TOKEN_EXPIRES=''
    # JWT_REFRESH_TOKEN_EXPIRES=''
    print("Environment created successfully!!!")