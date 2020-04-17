from game.app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=True)
    name = db.Column(db.Text, nullable=False)
    members = db.relationship('User', backref='team', lazy=True)

    def __repr__(self):
        return f'<team {self.name}: {[member for member in self.members]}>'
