import sqlite3
#
import click
from game.app import app
from flask import current_app, g


def get_db():
    if 'db' not in g:
        print(f"connect, database: {current_app.config['DATABASE']}")
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db
#
#
# def close_db(e=None):
#     db = g.pop('db', None)
#
#     if db is not None:
#         db.close()
#
#


def init_db():
    with app.app_context():
        db = get_db()

        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))

        db.commit()
#
#


def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
#
#
# def init_app(app):
#     app.teardown_appcontext(close_db)
