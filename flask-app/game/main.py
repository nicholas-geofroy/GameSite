import os
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user
from game.user import User
from game.db import get_db
from flask.cli import with_appcontext
from game.app import app
import click
from game.db import init_db_command
from lobby import remove_user_from_session
# ensure the instance folder exists

cli = click.Group()


@cli.command("init-db")
def init():
    """reset the database"""
    init_db_command()


@cli.command("run-server")
def run():
    """ run server """
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
    app.add_url_rule('/', endpoint='auth.login')

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

    @socketio.on('disconnect')
    def test_disconnect():
        print(f'user: {current_user.name} disconnected')
        # if current_user.room is None:
            # remove_user_from_session(current_user.room, current_user)

    socketio.on_event("join_room", lobby.join)

    socketio.run(app, debug=True)


cli.add_command(init)
cli.add_command(run)
cli()
