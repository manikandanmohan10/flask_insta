from flask import Blueprint
from src.authentication.views import RegisterAPI, LoginAPI

class AuthBlueprint(Blueprint):
    def __init__(self):
        super(AuthBlueprint, self).__init__('auth', __name__, url_prefix='/api/v1')
        self.add_url_rule('/register', view_func=RegisterAPI.as_view('register'))
        self.add_url_rule('/login', view_func=LoginAPI.as_view('login'))