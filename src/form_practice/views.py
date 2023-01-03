from flask import request, jsonify, render_template
from flask.views import MethodView

class FormAPI(MethodView):
    def get(self):
        return render_template('base.html')
    
    def post(self):
        username = request.form.get('uname')
        password = request.form.get('pass')
        if username == 'Manikandan' and password == 'Mani':
            return "Successfully logged in"
        else:
            return 'Invalid credentials'
