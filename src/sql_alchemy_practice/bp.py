from flask import Blueprint
from src.sql_alchemy_practice.views import CreateFruitAPI


class FruitBlueprint(Blueprint):
    def __init__(self):
        super(FruitBlueprint, self).__init__("fruit", __name__, url_prefix="/api/v1/fruit")
        self.add_url_rule('/create', view_func=CreateFruitAPI.as_view('fruit'))