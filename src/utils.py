import os
from fernet import Fernet
from flask_jwt_extended import create_refresh_token, create_access_token, decode_token


class Crypt:
    def __init__(self):
        self.fernet = get_fernet_key()
        if isinstance(self.fernet, str):
            raise Exception(self.fernet)
        
    def encrypt(self, user_data = None):
        if not user_data:
            return "Requires something to encrypt"
        if isinstance(user_data, dict):
            encrypted_data = {}
            for data in user_data:
                encrypted_data[data] = self.fernet.encrypt(user_data[data].encode())
        encrypted_data = self.fernet.encrypt(user_data.encode())
                        
        return encrypted_data
    
    def decrypt(self, data = None):
        if not data:
            return "Requires something to decrypt"

        data = eval(data)
        decrypted_data = self.fernet.decrypt(data).decode()
        return decrypted_data
        
        
def get_fernet_key() -> Fernet: 
    key = os.getenv('FERNET_KEY')
    
    if key:
        fernet = Fernet(eval(key))
        return fernet
    else:
        return "Encrpytion Key not found"
    

class JWTToken:
    def generate_token(self, user):
        refresh_token = create_refresh_token(identity=str(user.user_id))
        access_token = create_access_token(identity=user.user_id)
        
        return [refresh_token, access_token]

    def decode_token(self, token):
        payload = decode_token(token)
        
        return payload