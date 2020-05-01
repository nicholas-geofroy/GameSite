from game.games.taboo.taboo import TabooState, Taboo
import json
import enum
from flask_login import current_user


class TabooMessageType(enum.Enum):
    NEXT_CARD = 1
    GUESS_WORD = 2


def handle_event(message, game):
    state_dict = json.loads(game.game_state)
    state = TabooState(state_dict)
    type = message['type']
    giver_id = state.get_giver()
    if type == TabooMessageType.NEXT_CARD \
       and current_user.id == giver_id:
        state.next_card()
    if type == TabooMessageType.GUESS_WORD \
       and current_user.id in state.get_current_team():
        state.guess_word(message['guess'])

    return Taboo.get_messages(state)
