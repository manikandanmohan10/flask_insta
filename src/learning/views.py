from flask import Flask, request, Response
from flask.views import MethodView
from sqlalchemy import text
from flask.blueprints import Blueprint


testing = Blueprint('testing', __name__, url_prefix='/testing')

@testing.route('', methods=['POST'])
def hello_world():
    return Response("Hello world")

# class Testing(MethodView):
#     def post(self):
#         user_list = []
#         data = request.json
#         sql = text('select * from users')
#         result = db.engine.execute(sql)
#         for i in result:
#             user_list.append(i)
#         return Response('Ok')

# result = db.engine.execute("select * from users")

# user_list = [user[0] for user in result]
