from flask_sqlalchemy import SQLAlchemy

from settings import app

db = SQLAlchemy(app)


class City(db.Model):
    pass
