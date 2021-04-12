from flask_sqlalchemy import SQLAlchemy

from settings import app

db = SQLAlchemy(app)


class Feed(db.Model):
    pass
