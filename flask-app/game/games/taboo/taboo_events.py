from game.games.taboo.taboo import TabooState, Taboo
import json
import enum
from flask_login import current_user
from game.app import db


class TabooMessageType(enum.Enum):
    NEXT_CARD = "next_card"
    GUESS_WORD = "guess_word"
    REQUEST_STATE = "request_state"


def handle_event(message, game):
    type = message['type']
    print(f"hanlde event for game {game} of type {type} {TabooMessageType.REQUEST_STATE.value}")
    state_dict = json.loads(game.game_state)
    state = TabooState(prev_state=state_dict)
    print(f"state: {state.as_dict()}")
    type = message['type']
    giver_id = state.get_giver()
    if type == TabooMessageType.REQUEST_STATE.value:
        return [message for message in Taboo.get_messages(state)
                if message[0] == current_user.id]
    if type == TabooMessageType.NEXT_CARD.value \
       and current_user.id == giver_id:
        state.next_card()
    if type == TabooMessageType.GUESS_WORD.value \
       and not current_user.id == giver_id:
        state.guess_word(message['guess'])

    game.game_state = json.dumps(state.as_dict())
    db.session.commit()
    return Taboo.get_messages(state)
