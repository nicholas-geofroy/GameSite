from game.games.game import Game as BaseGame
from game.models.game import Game
from game.app import db


class TabooState:
    def __init__(self, prev_state=None, players=[[]]):
        turn = 0

        if prev_state is None:
            self.players = players
        else:
            self.players = prev_state.players

    def get_current_team(self):
        return self.turn % 2


class PlayerState:
    pass


class Taboo(BaseGame):
    type = 1

    def get_state(prev_state):
        pass

    def type():
        return 1

    def init(settings):
        new_game = Game(
            type=type,
            num_players=4,
            num_teams=2,
            game_state="{}"
        )
        db.session.add(new_game)
        db.session.commit()
        return new_game
