from flask import (
    Blueprint, g, redirect, render_template, url_for, session
)
from flask_login import login_required, current_user
from game.db import get_db
from flask_socketio import join_room

bp = Blueprint('lobby', __name__)


def join(data):
    print(data)
    print(g)
    print(session.get('id'))
    join_room(data['room'])
    print(f"{current_user.name} has entered the room {data['room']}")


@bp.route('/sessions', methods=('POST',))
@login_required
def create_session():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO session (host_id) '
        'VALUES (?)',
        (g.user['id'], )
    )
    db.commit()
    return redirect(url_for('lobby.load_session', id=cursor.lastrowid))


@bp.route('/sessions/<int:id>', methods=('GET', ))
@login_required
def load_session(id):
    return render_template('menu/lobby.html.j2', room=id)
