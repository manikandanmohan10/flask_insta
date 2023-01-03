from flask.views import MethodView
from flask import request, jsonify
from src.db import db
from src.sql_alchemy_practice.models import Fruits
from http import HTTPStatus as status
import logging
logger = logging.getLogger()


class CreateFruitAPI(MethodView):
    def post(self):
        data = request.json
        # fruit = {
        #     "fruit_name": data["fruit_name"]
        # } 
        fruit_name = data.get('fruit_name')
        if fruit_name:
            fruit = Fruits(**data)
            
            db.session.add(fruit)
            # db.session.flush()
            db.session.commit()
            
        return "Created Successfully", status.OK
    
    def get(self):

        fruit_name = request.headers.get('fruit_name')
        fruit = Fruits.query.filter_by(fruit_name=fruit_name).first()
        if not fruit:
            return jsonify(f"{fruit} not found"), status.NOT_FOUND
        
        fruit_list = {}
        fruit = Fruits.query.filter_by(fruit_name=fruit_name)
        for fruit_name in fruit:
            fruit_list[str(fruit_name.id)] = fruit_name.fruit_name
        
        # fruits = db.engine.execute(f"SELECT * FROM tbl_fruits where fruit_name='{fruit_name}'")
        
        # if not fruits:
        #     return jsonify(f"{fruits} not found"), status.NOT_FOUND
        
        # fruit_list = [fruit for fruit in fruits]
        # fruit_dict = {}
        
        # for fruit_name in fruit_list:
        #     fruit_dict[str(fruit_name.id)] = fruit_name.fruit_name
        # logger.debug("Testing")
        return jsonify(fruit_list), status.OK