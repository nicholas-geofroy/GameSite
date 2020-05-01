from game.games.game import Game as BaseGame
from game.models.game import Game, GameTypes
from game.app import db
from game.gameData.data import taboo_cards
import random
import json


class BannedGuess(Exception):
    pass


class Card:
    def __init__(self, target_word, banned_words):
        self.target_word = target_word
        self.banned_words = banned_words


class TabooState:
    def __init__(self, **kwargs):
        if "prev_state" not in kwargs:
            print(f"init taboo state with {taboo_cards} cards")
            ordering = [x for x in range(len(taboo_cards))]
            random.Random().shuffle(ordering)
            self.context = {
                'turn': 0,
                'players': kwargs['players'],
                'points': [0, 0],
                'cur_card': 0,
                'order': ordering
            }
            print(f"ordering {self.context['order']}")
        else:
            self.context = kwargs["prev_state"]

    def get_players(self):
        return [player for player in [team for team in self.context['players']]]

    def get_current_team_idx(self):
        return self.context['turn'] % 2

    def get_current_team(self):
        return self.context['players'][self.get_current_team_idx()]

    def get_giver_idx(self):
        return int(self.context['turn'] / 2) \
             % len(self.context['players'][self.get_current_team_idx()])

    def get_giver(self):
        return self.context['players'][self.get_current_team_idx()][self.get_giver_idx()]

    def as_dict(self):
        return self.context

    def get_current_card(self):
        ordering = self.context['order']
        cur_card_idx = self.context['cur_card']
        return taboo_cards[ordering[cur_card_idx]]

    def next_card(self):
        self.context['cur_card'] += 1
        return self.get_current_card()

    def guess_word(self, guess):
        current_card = self.get_current_card()

        if current_card.target_word.lower() == guess.lower():
            self._give_point()
            return True
        elif guess.lower() in [c.lower() for c in current_card.banned_words]:
            self.next_card()
            raise BannedGuess(f"{guess} is a banned word")

    def _give_point(self):
        current_team = self.get_current_team_idx()
        self.context['points'][current_team] += 1

    def get_player_states(self):
        cur_team_idx = self.get_current_team_idx()
        cur_giver_idx = self.get_giver_idx()
        players = self.context['players']

        return {
            'shared_state': {
                'giver': players[cur_team_idx][cur_giver_idx].id,
                'players': players
            },
            'giver_state': {
                'card': self.get_current_card()
            }
        }


class PlayerState:
    pass


class Taboo(BaseGame):
    type = 1

    def type():
        return 1

    def validate(players):
        return len(players) > 1

    def init(settings, players):
        # get players and place on teams
        teams = Taboo.split_players(players)
        print(f"create teams {teams}")
        new_state = TabooState(players=teams)
        new_game = Game(
            type=GameTypes.TABOO,
            num_players=4,
            num_teams=2,
            game_state=json.dumps(new_state.as_dict())
        )
        db.session.add(new_game)
        db.session.commit()
        return Taboo.get_messages(new_state)

    def get_messages(state):
        messages = []
        giver_id = state.get_giver()
        user_messages = state.get_player_states()
        shared_state = user_messages['shared_state']
        messages.append((giver_id, {
            **shared_state,
            **user_messages['giver_state']
        }))

        for player in state.get_players():
            if player != giver_id:
                messages.append((player, shared_state))

        return messages

    def split_players(players):
        mid = int(len(players)/2)
        return [
            [players[i] for i in range(mid)],
            [players[i] for i in range(mid, len(players))]
        ]
