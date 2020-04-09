from game.db import get_db


class User():
    def __init__(self, id, name):
        self.id = id
        self.authenticated = False
        self.name = name

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get(user_id):
        userObj = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

        if userObj is None:
            return userObj

        return User(userObj['id'], userObj['username'])