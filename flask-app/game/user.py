from game.app import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)

    is_authenticated = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_anonymous = db.Column(db.Boolean, nullable=False)

    socketio_id = db.Column(db.Text, nullable=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.is_authenticated = False
        self.is_active = True
        self.is_anonymous = False

    def __repr__(self):
        return '<User %r>' % self.username

    def get_id(self):
        return self.id

    def get(user_id):
        print("get: user_id:" + str(user_id))
        return User.query.filter_by(id=user_id).first()

    def to_dict(self):
        return {
            "username": self.username,
            "session_id": self.session_id
        }

    def new(username, password):
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return new_user
