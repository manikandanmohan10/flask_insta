from flask import request, render_template, jsonify
from flask.views import MethodView
from src.authentication.models import User
from http import HTTPStatus as status
from copy import deepcopy
from src.constant import RESPONSE_DATA
from src.utils import Crypt, JWTToken
from flask_login import login_user, logout_user
response_data = deepcopy(RESPONSE_DATA)

class RegisterAPI(MethodView):
    def post(self):
        user_data = request.json
        
        to_validate = User.validate()
        validate = to_validate.load(data=user_data)
        encrypt = to_validate.encrypt_data(validate['password'])
        validate['password'] = encrypt
        validate['phone_number'] = str(validate['phone_number'])
        
        data = User.register(validate)
        
        if data[0] is False:
            response_data['statusCode'] = 400
            response_data['message'] = data[1]
            return jsonify(response_data), status.BAD_REQUEST
           
        response_data['statusCode'] = 201
        response_data['status'] = 'Success'
        response_data['message'] = 'User Created Successfully'
        return jsonify(response_data), status.CREATED
    
    
class LoginAPI(MethodView):
    def post(self):
        crypt = Crypt()
        jwt_token = JWTToken()
        user_data = request.json
        user = User.query.filter_by(email=user_data.get('email')).first()
        
        if not user or not crypt.decrypt(user.password) == user_data['password']:
            response_data['message'] = 'Please check your login details and try again'    
            return jsonify(response_data), status.BAD_REQUEST
        
        refresh_token, access_token = jwt_token.generate_token(user)
    
        response_data = dict(
            message='Logged in successfully',
            status=True,
            statusCode=200,
            token={'refresh_token':refresh_token, 'access_token':access_token}
            )
        
        return jsonify(response_data), status.OK

        
class Logout(MethodView):
    def post(self):
        pass