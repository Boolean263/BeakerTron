# This app uses the Application Factory model. For more information:
# https://hackersandslackers.com/flask-application-factory/
# https://github.com/hackersandslackers/flask-sqlalchemy-tutorial

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))


def create_app(override_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Default configuration if nothing else given
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(
            app.instance_path, 'beakertron.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if override_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(override_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from . import routes

        from . import db
        db.init_app(app)

    app.add_url_rule('/', endpoint='index')
    return app
