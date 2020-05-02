from flask_login import current_user
from game.models.game import GameTypes
from game.games.taboo.taboo_events import handle_event
from games.taboo.taboo import Taboo
from game.models.user import User
from game.games.game_models import Player
from flask_socketio import emit


def init(socketio):
    socketio.on_event('game_updates', game_update)


def send_game_message(user_id, message):
    user = User.get(user_id)
    print(f'sending message to {user}')
    emit('game_updates', message, room=user.socketio_id)


def start_game(settings):
    players = [Player(member.id, member.username) for member in current_user.session.members]
    print(f"start the game with settings: {settings}, players {players}")
    game_type = settings['gamemode']
    messages = []
    if game_type == Taboo.type() and Taboo.validate(players):
        messages = Taboo.init(settings, players)
    return [(message[0], {**message[1], 'type': 'start_game'})
            for message in messages]


def game_event(message, cur_game):
    if cur_game.type == GameTypes.TABOO:
        return handle_event(message, cur_game)


def game_update(message):
    print(f"recieved game update {message} from {current_user.username}")
    if not current_user.is_authenticated:
        return False
    if current_user.session_id is None:
        return False

    message_type = message['type']
    if message_type is None:
        return False

    cur_game = current_user.session.game
    messages = []
    print(f"sending messages {messages}")
    # try to start game
    if cur_game is None:
        if message_type != 'start_game':
            return False
        else:
            messages = start_game(message)
    else:
        messages = game_event(message, cur_game)

    for message in messages:
        send_game_message(message[0], message[1])
