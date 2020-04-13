from flask import (
    Blueprint, redirect, render_template, url_for
)
from flask_login import login_required, current_user
from flask_socketio import join_room, emit, leave_room
from game.user import User
from game.session import Session
from game.app import db

bp = Blueprint('lobby', __name__)


def init(socketio):
    socketio.on_event('join_room', join)
    socketio.on_event('leave_lobby', leave)


def join(data):
    room = data['room']
    print(f"{current_user.username} joins room {room}")
    add_user_to_session(room, current_user)
    join_room(current_user.session_id)
    update_users_in_session(current_user.session_id)


def update_users_in_session(session_id):
    users_in_session = get_users_in_session(session_id)
    print(f"users currently in the room: {users_in_session}")

    emit('user_updates',
         [user.to_dict() for user in users_in_session],
         session_id)


def leave():
    to_leave = current_user.session_id
    print(f"{current_user} leaves the room {to_leave}")
    leave_room(room=to_leave)
    remove_user_from_session(current_user)
    update_users_in_session(to_leave)


@bp.route('/sessions', methods=('POST',))
@login_required
def create_session():
    game = Session()
    db.session.add(game)
    db.session.commit()
    print(f"created session: {game.id} for user: {current_user.username}")
    return redirect(url_for('lobby.load_session', id=game.id))


@bp.route('/sessions/<id>', methods=('GET', ))
@login_required
def load_session(id):
    return render_template('menu/lobby.html.j2', room=id)


def add_user_to_session(session_id, user):
    session = Session.query.filter_by(id=session_id).first()
    user.session = session
    db.session.commit()


def remove_user_from_session(user):
    user.session = None
    db.session.commit()


def get_users_in_session(session_id):
    return User.query.filter_by(session_id=session_id).all()
