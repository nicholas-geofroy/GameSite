from game.app import db


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    members = db.relationship('User', backref='session', lazy=True)
