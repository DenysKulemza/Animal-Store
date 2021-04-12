from flask_sqlalchemy import SQLAlchemy

from logger.logging import loggers
from settings import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(40), nullable=False)

    @staticmethod
    def add_user(request, login, password, address):
        """Adding some user

        :param request: of the input form
        :param login: login of some center
        :param password: password of some center
        :param address: address of some center
        """

        new_user = User(login=login, password=password, address=address)
        db.session.add(new_user)
        db.session.commit()
        loggers(request, new_user.id, 'New user was added', new_user.id)

    def display_user(self):
        """Display user with id

        :return: name of centers and id
        """
        return {'Name: ': self.login, 'Id: ': str(self.id)}

    @staticmethod
    def get_all_users():
        """Getting all users

        :return: centers
        """
        return [User.display_centers(user) for user in User.query.all()]
