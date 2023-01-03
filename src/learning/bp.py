from src.learning.views import TestingAPI
from flask import Blueprint

class TestingBlueprint(Blueprint):
    def __init__(self):
        super(TestingBlueprint, self).__init__('test', __name__, url_prefix='/api/v1')
        self.add_url_rule('/testing', view_func=TestingAPI.as_view('testing'))