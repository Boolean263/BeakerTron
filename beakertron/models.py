"""
Data models; aka, the tables and relationships of our app.
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# This object is needed in order for our model to subclass it.
# It needs to be initialized with the current application context
# via `db.init_app(app)` before it will be of use.
db = SQLAlchemy()


class User(db.Model):
    "User account"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    def __repr__(self):
        return '<User #{} "{}">'.format(self.id, self.username)

    @classmethod
    def by_name(cls, uname):
        return cls.query.filter_by(username=uname).first()


class Post(db.Model):
    "Blog post"

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        index=True,
        nullable=False,
    )
    created = db.Column(
        db.DateTime(),
        nullable=False,
        default=datetime.utcnow
    )
    title = db.Column(
        db.Text(),
        nullable=False
    )
    body = db.Column(
        db.Text(),
        nullable=False
    )
    def __repr__(self):
        return '<Post #{} "{}" by {}>'.format(
            self.id,
            self.title,
            self.author_id
        )
