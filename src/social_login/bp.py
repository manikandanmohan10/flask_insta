import os

from flask import Blueprint
from src.social_login.github_login import GithubLogin, GithubVerify


class SocialBlueprint(Blueprint):
    def __init__(self):
        super(SocialBlueprint, self).__init__("social_login", __name__, url_prefix='/api/v1/login')
        self.add_url_rule('/github', view_func=GithubLogin.as_view('github'))
        self.add_url_rule('/verify', view_func=GithubVerify.as_view('verify'))
