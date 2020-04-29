from abc import ABC, abstractmethod


class Game(ABC):
    games = []
    @abstractmethod
    def get_state():
        pass

    @abstractmethod
    def type():
        pass

    @abstractmethod
    def init(settings):
        pass

    def from_state(state):
        for game in Game.games:
            if game.type == state.type:
                return game
        return None
