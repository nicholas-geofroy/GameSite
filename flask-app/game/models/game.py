from game.app import db
import enum


class GameTypes(enum.Enum):
    TABOO = 1


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(enum.Enum(GameTypes), nullable=False)
    num_players = db.Column(db.Integer, nullable=False)
    num_teams = db.Column(db.Integer, nullable=False)
    game_state = db.Column(db.Text, nullable=True)
    teams = db.relationship('Team', backref='game', lazy=True)

    def __repr__(self):
        return f'<Game {self.id}: {self.type}>'
