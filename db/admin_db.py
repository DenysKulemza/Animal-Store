from flask_sqlalchemy import SQLAlchemy

from settings import app

db = SQLAlchemy(app)


class Admin(db.Model):
    pass
