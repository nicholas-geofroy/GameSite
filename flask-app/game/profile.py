from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from game.auth import login_required
from game.db import get_db

bp = Blueprint('profile', __name__)


@bp.route('/profiles/<int:id>', methods=('GET', 'POST'))
@login_required
def get_profile(id):
    return render_template('menu/profile.html.j2')


@bp.route('/sessions', methods=('POST',))
@login_required
def create_session():
    return render_template('menu/index.html.j2')
