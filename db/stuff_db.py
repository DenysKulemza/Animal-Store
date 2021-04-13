from db import db
from db.access_request import AccessToken
from db.animal_db import Animal
from logger.logging import loggers


class Stuff(db.Model):
    __tablename__ = 'stuff'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    stuff_type_id = db.Column(db.Integer, db.ForeignKey('stuff_type.id', ondelete='CASCADE'), nullable=False)
    description = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @staticmethod
    def add_stuff(request, name, description, price):
        """Adding new specie

        :param request: request of input form
        :param name: name of some specie
        :param description: description of some specie
        :param price: price of some specie
        :return: nothing
        """
        new_specie = Stuff(name=name, description=description, price=price)
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

    def specie_stuff(self, animal_object):
        """Represent species, id, names in json format

        :param animal_object: some animal
        :return: representation of specie
        """
        return {'Animal name ': animal_object,
                'Id ': self.id, 'Specie ': self.name}

    @staticmethod
    def get_stuff(stuff_id):
        """Getting animal by specie

        :param stuff_id: some id of stuff
        :return: animal in json
        """
        return [Stuff.find_stuff(stuff_id) for _ in Stuff.query.all()]

    @staticmethod
    def find_stuff(stuff_id):
        """Finds some animal

        :param stuff_id: id of stuff
        :return: animal
        """
        specie = Stuff.query.filter_by(id=stuff_id).first()
        return [Stuff.specie_animals(specie, animal.name)
                for animal in
                Animal.query.filter_by(species=specie.name).all()]
