from game.games.game import Game as BaseGame
from game.models.game import Game
from game.app import db
from game.gameData.data import taboo_cards
import random
import json


class Card:
    def __init__(self, target_word, banned_words):
        self.target_word = target_word
        self.banned_words = banned_words


class TabooState:
    def __init__(self, **kwargs):
        if "prev_state" not in kwargs:
            print(f"init taboo state with {len(taboo_cards)} cards")
            self.context = {
                'turn': 0,
                'players': kwargs['players'],
                'cur_card': 0,
                'order': random.Random().shuffle(
                    [x for x in range(len(taboo_cards))]
                )
            }
        else:
            self.context = kwargs["prev_state"]

    def get_current_team(self):
        return self.context['turn'] % 2

    def get_giver(self):
        return int(self.context['turn'] / 2) \
             % len(self.context['players'][self.get_current_team()])

    def as_dict(self):
        return self.context

    def get_current_card(self):
        ordering = self.context['order']
        cur_card_idx = self.context['cur_card']
        new_card = taboo_cards[ordering[cur_card_idx]]
        self.context['cur_card'] += 1
        return new_card

    def get_player_states(self):
        cur_team_idx = self.get_current_team()
        cur_giver_idx = self.get_giver()
        players = self.context['players']

        return {
            'shared_state': {
                'giver': players[cur_team_idx][cur_giver_idx].id
            },
            'giver_state': {
                'card': taboo_cards[self.order[self]]
            }
        }


class PlayerState:
    pass


class Taboo(BaseGame):
    type = 1

    def type():
        return 1

    def init(settings):
        # get players and place on teams
        new_state = TabooState()
        new_game = Game(
            type=type,
            num_players=4,
            num_teams=2,
            game_state=json.dumps(new_state.as_dict())
        )
        db.session.add(new_game)
        db.session.commit()
        return new_game, new_state

    def __init__(self, game):
        self.game = game
        self.state = TabooState(json.loads(game.game_state))

    def perform_action(self, action):
        action = getattr(self, action, None)
        if action is not None:
            action()

    def next_card(self):
        pass

    def guess_word(self, guess):
        pass
