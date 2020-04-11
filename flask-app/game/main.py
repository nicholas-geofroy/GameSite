import os
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user
from game.user import User
from game.app import app
from db import init_db_command
import click
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

    from game.app import db
    db.create_all()

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
            print(f'user {current_user.username} is connected')
        else:
            return False  # not allowed here

    @socketio.on('disconnect')
    def test_disconnect():
        print(f'user: {current_user.username} disconnected')

    socketio.on_event("join_room", lobby.join)

    socketio.run(app, debug=True)


cli.add_command(init)
cli.add_command(run)
cli()
