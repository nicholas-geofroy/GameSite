from flask_login import current_user
from game.models.game import Game


def init(socketio):
    socketio.on_event('game_updates', game_update)


def game_update(message):
    print(f"recieved game update {message} from {current_user.username}")
    if not current_user.is_authenticated:
        return False
    if current_user.session_id is None:
        return False

    message_type = message['type']
    if message_type is None:
        return False

    # try to start game
    if current_user.session.game is None:
        if message_type != 'start_game':
            return False
        else:
            start_game(message)


def start_game(data):
    print(f"start the game with data: {data}")
    
