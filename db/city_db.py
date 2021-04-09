from flask_sqlalchemy import SQLAlchemy
from settings import app
from logger.logging import loggers

db = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    @staticmethod
    def add_city(request, _login, _password, _address):
        """Adding some user

        :param request: of the input form
        :param _login: login of some center
        :param _password: password of some center
        :param _address: address of some center
        :return: nothing
        """

        new_user = City(login=_login, password=_password, address=_address)
        db.session.add(new_user)
        db.session.commit()
        loggers(request, new_user.id, 'New center was added', new_user.id)

    def display_city(self):
        """Display centers with id

        :return: name of centers and id
        """
        return {'Name: ': self.login, 'Id: ': str(self.id)}

    @staticmethod
    def get_all_cities():
        """Getting all centers

        :return: centers
        """
        return [City.display_centers(user) for user in City.query.all()]
