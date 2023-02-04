from flask import request, render_template, jsonify
from flask.views import MethodView
from src.authentication.models import User
from http import HTTPStatus as status
from copy import deepcopy
from src.constant import RESPONSE_DATA
from src.utils import Crypt, JWTToken
from flask_login import login_user, logout_user
from src.db import db

class RegisterAPI(MethodView):
    response_data = deepcopy(RESPONSE_DATA)
    def post(self):
        user_data = request.json
        
        try:
            if isinstance(eval(user_data['email_phNo']), int):
                user_data['phone_number'] = user_data.pop('email_phNo')
        except:
            user_data['email'] = user_data.pop('email_phNo')
        
        to_validate = User.validate()
        user_data['full_name'] = user_data.pop('fullName', None)
        validate = to_validate.load(data=user_data)
        encrypt = to_validate.encrypt_data(validate['password'])
        validate['password'] = encrypt
        validate['phone_number'] = str(validate['phone_number']) if validate.get('phone_number') else None
        
        data = User.register(validate)
        
        if data[0] is False:
            self.response_data['statusCode'] = 400
            self.response_data['message'] = data[1]
            return jsonify(self.response_data), status.BAD_REQUEST
           
        self.response_data['statusCode'] = 201
        self.response_data['status'] = 'Success'
        self.response_data['message'] = 'User Created Successfully'
        return jsonify(self.response_data), status.CREATED
    
    
class LoginAPI(MethodView):
    response_data = deepcopy(RESPONSE_DATA)
    def post(self):
        crypt = Crypt()
        jwt_token = JWTToken()
        user_data = request.json
        user = User.query.filter_by(username=user_data.get('username')).first()
        
        if not user or not crypt.decrypt(user.password) == user_data['password']:
            self.response_data['message'] = 'Please check your login details and try again'    
            return jsonify(self.response_data), status.BAD_REQUEST
        
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
    

class GetUserAPI(MethodView):
    response_data = deepcopy(RESPONSE_DATA)
    def get(self):
        user_data = []
        # for ind, user in enumerate(User.query.filter(User.is_active == True).all()):
        for ind, user in enumerate(User.query.filter_by(is_active=True).all()):
            user_data.append({'index': ind+1, 'user_id': user.user_id, 'username': user.username, 
                            'email': user.email, 'phone_number': user.phone_number, 'is_active':user.is_active})
        response_data = dict(
            message="Data fetched successfully",
            status=True,
            statusCode=200,
            data=user_data
        )
        return jsonify(response_data), status.OK
    
    
class DeleteUserAPI(MethodView):
    response_data = deepcopy(RESPONSE_DATA)
    def delete(self):
        user_id = request.args.get("id")
        if not user_id:
            self.response_data['message'] = 'User ID not found'
            self.response_data['statusCode'] = 404
            jsonify(self.response_data), status.NOT_FOUND
         
        user_data = User.query.filter_by(user_id=user_id).first()
        if not user_data:
            self.response_data['message'] = 'User not found'
            self.response_data['statusCode'] = 400
            jsonify(self.response_data), status.NOT_FOUND
        user_data.is_active = False
        db.session.commit()
            
        # User.query.filter_by(user_id=user_id).delete()
        self.response_data['message'] = 'User Deleted Successfully'
        self.response_data['statusCode'] = 200
        return jsonify(self.response_data), status.OK