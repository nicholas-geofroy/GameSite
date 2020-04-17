import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_login import login_user, logout_user

from werkzeug.security import check_password_hash
from game.app import db
from game.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif User.query.filter_by(username=username).first() is not None:
            error = f'User {username} is already registered'

        if error is None:
            User.new(username, password)
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html.j2')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            user.is_authenticated = True
            db.session.commit()
            session.clear()
            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for('profile.get_profile', id=user.id))

        flash(error)

    return render_template('auth/login.html.j2')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.get(user_id)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
