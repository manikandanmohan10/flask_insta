from src.form_practice.views import FormAPI
from flask import Blueprint

class FormBlueprint(Blueprint):
    def __init__(self):
        super(FormBlueprint, self).__init__("form", __name__, url_prefix="/api/v1")
        self.add_url_rule('/form', view_func=FormAPI.as_view("form"))