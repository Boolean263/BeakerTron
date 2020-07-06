# This file exists because it appears in:
# https://github.com/hackersandslackers/flask-sqlalchemy-tutorial
# I'm still learning this as I go, so I'm not yet sure this is
# better than defining the routes directly in __init__.py .

"""
The routes for our application.
"""
from flask import current_app as app

from . import auth
app.register_blueprint(auth.bp)

from . import blog
app.register_blueprint(blog.bp)
