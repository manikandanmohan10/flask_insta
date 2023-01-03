import os
from flask import (Flask, request, Response, get_template_attribute, render_template,
    send_file, escape, redirect, jsonify, current_app)
from werkzeug.utils import secure_filename
from werkzeug.urls import url_encode
from flask.views import MethodView

# testing = Blueprint('testing', __name__, url_prefix='/testing')

# @testing.route('', methods=['POST'])
# def hello_world():
#     return Response("Hello world")

class TestingAPI(MethodView):
    def get(self):
        # file = send_file('/home/softsuave/Prog/flask/flask_insta/Billie-Eilish-Happier-Than-Ever.webp', as_attachment=True)
        # return 'file'
        
        # uname = escape("<script>alert('XSS')</script> &")
        # return render_template('base.html', uname=uname)
        # resp = send_file.
        # query_string = url_encode({"param1": "value1", "param2": "value2"})
        res = {"param1": "value1", "param2": "value2"}
        # return redirect("http://example.com/route?" + query_string)
        return jsonify(res)
    
    def post(self):
        # file = request.files['file']
        # file_name = secure_filename(file.filename)
          
        # value = get_template_attribute('base.html')
        # file.save(os.path.join("/", file_name))
        
        return 'Hey'


