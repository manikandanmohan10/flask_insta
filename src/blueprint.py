from src.authentication.bp import AuthBlueprint
from src.learning.bp import TestingBlueprint
from src.social_login.bp import SocialBlueprint
from src.social_login.github_login import github_blueprint
from src.sql_alchemy_practice.bp import FruitBlueprint
from src.form_practice.bp import FormBlueprint

blueprint_list = []
blueprint_list.append(AuthBlueprint())
blueprint_list.append(TestingBlueprint())
blueprint_list.append(github_blueprint)
blueprint_list.append(SocialBlueprint())
blueprint_list.append(FruitBlueprint())
blueprint_list.append(FormBlueprint())
