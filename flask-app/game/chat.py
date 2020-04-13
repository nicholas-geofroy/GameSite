from flask_login import current_user
from flask_socketio import emit, join_room


def init(socketio):
    socketio.on_event('send_message', message_recieved)


def message_recieved(message):
    print(f"recieved message {message} from {current_user.username}")
    if not current_user.is_authenticated:
        return False

    message = {
        "user": current_user.username,
        "message": message
    }

    if current_user.session_id is None:
        return

    print(f"sending message {message} to room {current_user.session_id}")

    emit("message", message, room=current_user.session_id, include_self=True)
