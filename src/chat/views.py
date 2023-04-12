from src.chat.models import Chat
from flask_socketio import SocketIO, send, emit
from src import socket
from src.db import db

socketio = socket()

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

    emit('message', message, broadcast=True)

@socketio.on('clear')
def clear(msg):
    Chat.query.delete()
    db.session.commit()
