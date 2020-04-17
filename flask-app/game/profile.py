from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flask_login import login_required

bp = Blueprint('profile', __name__)


@bp.route('/profiles/<int:id>', methods=('GET', 'POST'))
@login_required
def get_profile(id):
    return render_template('menu/profile.html.j2')
