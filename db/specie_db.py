from flask_sqlalchemy import SQLAlchemy

from db.access_request import AccessToken
from db.animal_db import Animal
from logger.logging import loggers
from settings import app

db = SQLAlchemy(app)


class Specie(db.Model):
    __tablename__ = 'specie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @staticmethod
    def add_specie(request, name, description, price):
        """Adding new specie

        :param request: request of input form
        :param name: name of some specie
        :param description: description of some specie
        :param price: price of some specie
        """
        new_specie = Specie(name=name, description=description, price=price)
        db.session.add(new_specie)
        db.session.commit()
        access = AccessToken.query.order_by(AccessToken.id.desc()).first()
        loggers(request, access.center_id,
                'New specie was added', new_specie.id)

    def json(self, count):
        """Representation of specie and amount of all specie

        :param count: amount of some specie in centers
        :return: names and amount of all animal
        """
        return {'name': self.name, f'amount of "{self.name}"': count}

    def specie_animals(self, animal_object):
        """Represent species, id, names in json format

        :param animal_object: some animal
        :return: representation of specie
        """
        return {'Animal name ': animal_object,
                'Id ': self.id, 'Specie ': self.name}

    @staticmethod
    def get_specie_animals(animal_id):
        """Getting animal by specie

        :param animal_id: some id of animal
        :return: animal in json
        """
        return [Specie.find_animal(animal_id) for _ in Specie.query.all()]

    @staticmethod
    def find_animal(specie_id):
        """Finds some animal

        :param specie_id: id of some specie
        :return: animal
        """
        specie = Specie.query.filter_by(id=specie_id).first()
        return [Specie.specie_animals(specie, animal.name)
                for animal in
                Animal.query.filter_by(species=specie.name).all()]
