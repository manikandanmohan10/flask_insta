from flask import Blueprint
from src.authentication.views import RegisterAPI, LoginAPI, GetUserAPI, DeleteUserAPI

class AuthBlueprint(Blueprint):
    def __init__(self):
        super(AuthBlueprint, self).__init__('auth', __name__, url_prefix='/api/v1')
        self.add_url_rule('/register', view_func=RegisterAPI.as_view('register'))
        self.add_url_rule('/login', view_func=LoginAPI.as_view('login'))
        self.add_url_rule('/getUser', view_func=GetUserAPI.as_view('get_user'))
        self.add_url_rule('/deleteUser', view_func=DeleteUserAPI.as_view('delete_user'))