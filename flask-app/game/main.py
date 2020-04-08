import os
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user
from user import User
from db import get_db
from flask import Flask


# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'game.sqlite'),
)
# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from game import db
db.init_app(app)

from game import auth
app.register_blueprint(auth.bp)

from game import profile
app.register_blueprint(profile.bp)
app.add_url_rule('/', endpoint='index')

from game import lobby
app.register_blueprint(lobby.bp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


socketio = SocketIO(app)


@socketio.on('connect')
def connect_handler():
    if current_user.is_authenticated:
        print(f'user {current_user.name} is connected')
    else:
        return False  # not allowed here

        
socketio.on_event("join", lobby.join)

socketio.run(app, debug=True)
