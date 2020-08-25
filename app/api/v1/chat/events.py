from flask_socketio import emit, join_room, leave_room
from uuid import uuid4
from app import socketio


@socketio.on('send_message', namespace='/chat')
def get_message(message):
    print('received message: ' + message)
    broadcast_message = {
        'user': {
            'username': 'John Doe',
            'avatarUrl': 'http://127.0.0.1:3000/static/media/avatar.1bdfd1be.svg',
        },
        'message': {
            'id': str(uuid4()),
            'messageSender': 'myMessage',
            'messageBody': message
        }
    }
    emit('send_message', broadcast_message, json=True, broadcast=True)

