import threading
import uuid
from src.db import db
from flask_security import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from marshmallow import validate, fields, Schema, validates
from src.utils import Crypt
from src.tasks import send_celery_email

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(55), unique=True)
    full_name = db.Column(db.String(55), nullable=True)
    # last_name = db.Column(db.String(55), nullable=True)
    email = db.Column(db.String(55), nullable=True, unique=True)
    phone_number = db.Column(db.String(55), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_superuser = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now())
    otp = db.Column(db.String(12), nullable=True)
    otp_created_at = db.Column(db.DateTime(), onupdate=datetime.now())
    
    @staticmethod
    class validate(Schema):
        username = fields.Str(validate=validate.Length(min=8), required=True, error_messages={"required": "Username is required."})
        full_name = fields.Str(validate=validate.Length(min=3))
        email = fields.Email(validate=validate.Email(), required=False, error_messages={"required": "Email is required."})
        password = fields.Str(validate=validate.Length(min=8), required=True, error_messages={"required": "Password is required."})
        phone_number = fields.Str(required=False, error_messages={"required": "Phone number is required"})
        
        def encrypt_data(self, user_data) -> dict:
            crypt = Crypt()
            data = crypt.encrypt(user_data)
            
            return str(data)
    
    @classmethod
    def register(cls, data):
        try:
            if data.get('email') and cls.query.filter_by(email=data['email']).first():
                raise Exception('Email already registered, Please use different one')
            if cls.query.filter_by(username=data['username']).first():
                raise Exception('username already registered, Please use different one')
            if data.get('phone_number') and cls.query.filter_by(phone_number=data['phone_number']).first():
                raise Exception('Phonenumber already registered, Please use different one')
            
            user = User(**data)
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            
            if data.get('email'):
                try:
                    t1 = threading.Thread(target=user.send_verification_email())
                    t1.start()
                    # user.send_verification_email()
                except Exception as e:
                    print(str(e))

            return True, user
        except Exception as e:
            print(str(e))
            return False, str(e)
    
    def send_verification_email(self):
        message_data = {'recipients': [self.email], 'body': 'Verification email'}
        send_celery_email(message_data)
    
    def __str__(self) -> str:
        return f"User -> {self.email}"
