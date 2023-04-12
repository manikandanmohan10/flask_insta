from asgiref.wsgi import WsgiToAsgi
from flask import render_template
from src import create_app
import asyncio
from werkzeug.middleware.profiler import ProfilerMiddleware

app = create_app()
# app.wsgi_app = ProfilerMiddleware(app.wsgi_app)

# asyncio.run(serve(application, Config()))

# asgi_app = WsgiToAsgi(application)
# @app.route('/home')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
    
from src.chat.models import Chat
from flask_socketio import emit, SocketIO
from src.db import db
from src import socket

socketio = SocketIO(app, cors_allowed_origins='*')

# @socketio.on('connection')
# def index(socket):
#     print(socket)

@socketio.on('connect-io')
def test_connect(msg):
    print('Client connected')

    text_history = [{'sent_text': [chat.sent_text], 'received_text': [chat.received_text]} for chat in Chat.query.all()]

    emit('my-response', {'data': text_history})

@socketio.on('message')
def handle_message(message):
    send_message = {'message': f"from server: {message['message']}"}
    data = {'sent_text': send_message['message'], 'received_text': message['message']}

    data_ = Chat(**data)
    db.session.add(data_)
    db.session.flush()
    db.session.commit()

    emit('message', send_message, broadcast=True)

@socketio.on('clear')
def clear(msg):
    Chat.query.delete()
    db.session.commit()

if __name__ == "__main__":
    socketio.run(app, debug=True)