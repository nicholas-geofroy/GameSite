from flask import (
    Blueprint, g, redirect, render_template, url_for, session
)
from flask_login import login_required, current_user
from game.db import get_db
from flask_socketio import join_room, emit
from game.user import User
import uuid

bp = Blueprint('lobby', __name__)


def join(data):
    room = data['room']
    print(f"{current_user.name} joins room {room}")
    join_room(room)
    add_user_to_session(room, current_user)
    users_in_session = get_users_in_session(room)
    emit('user_updates', [vars(user) for user in users_in_session], room)


@bp.route('/sessions', methods=('POST',))
@login_required
def create_session():
    session_id = str(uuid.uuid4())
    print("create session: " + session_id + " for user: " + str(current_user.id))
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO session (sessionId, hostId) '
        'VALUES (?,?)',
        (session_id, current_user.id)
    )
    db.commit()
    print("created session, redirect...")
    return redirect(url_for('lobby.load_session', id=session_id))


@bp.route('/sessions/<id>', methods=('GET', ))
@login_required
def load_session(id):
    return render_template('menu/lobby.html.j2', room=id)


def add_user_to_session(session_id, user):
    current_user.room = session_id
    db = get_db()
    db.execute(
        'INSERT INTO inSession '
        'VALUES (?,?)',
        (user.id, session_id)
    )
    db.commit()


def remove_user_from_session(session_id, user):
    db = get_db()
    db.execute(
        'DELETE FROM inSession '
        'WHERE userId = ? AND sessionId = ?',
        (user.id, session_id)
    )
    db.commit()


def get_users_in_session(session_id):
    db = get_db()
    user_ids = db.execute(
        'SELECT * FROM inSession s '
        'WHERE s.sessionId = ?',
        (session_id, )
    ).fetchall()
    db.commit()
    print("get_users:" + str(user_ids))
    return [User.get(row.userId) for row in user_ids]
