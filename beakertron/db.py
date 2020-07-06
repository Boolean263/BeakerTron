import click
from flask import current_app, g
from flask.cli import with_appcontext

from .models import db


def get_db(app=current_app):
    if 'db' not in g:
        g.db = db
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        if callable(getattr(db, "close", None)):
            db.close()


def init_db():
    db = get_db()
    db.create_all()
    return db


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
