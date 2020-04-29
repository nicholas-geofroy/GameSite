from game.app import db
from game.models.game import Game


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(Game.id), nullable=True)
    members = db.relationship('User', backref='session', lazy=True)
