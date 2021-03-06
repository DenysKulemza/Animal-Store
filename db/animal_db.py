from db import db
from logger.logging import loggers


class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    center_address = db.Column(db.Integer, db.ForeignKey('centers.address', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100))
    age = db.Column(db.Integer, nullable=False)
    specie_id = db.Column(db.Integer, db.ForeignKey('specie.id', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Integer)

    def json(self):
        """Represent name of animals in json format

        :return: name of animals
        """
        return {'Name': self.name}

    def current_animal(self):
        """Represent information about current animal in json format

        :return: information about current animal
        """
        return {'Center id': self.center_id, 'Name': self.name,
                'Description': self.description, 'Age': self.age,
                'Species': self.species, 'Price': self.price}

    @staticmethod
    def display_current_animal(animal_id):
        """Finds an animal in the database by id

        :param animal_id: id of some animal
        :return: information about this animal
        """
        animal = Animal.query.filter_by(id=animal_id).first()
        return Animal.current_animal(animal)

    @staticmethod
    def add_animal(request, _center_id, _name,
                   _description, _age, _species, _price):
        """Adding animal to the database

        :param request: request of input form
        :param _center_id: id of adding center
        :param _name: name of animal
        :param _description: animal description
        :param _age: age of animal
        :param _species: specie of animal
        :param _price: price of animal
        :return: nothing
        """
        new_animal = Animal(center_id=_center_id, name=_name,
                            description=_description, age=_age,
                            species=_species, price=_price)
        db.session.add(new_animal)
        db.session.commit()
        loggers(request, _center_id, 'New animal was added', new_animal.id)

    def center_animals(self):
        """Represent of animal about some center in json format

        :return: animals in some center
        """
        return {'Animal name ': self.name,
                "Id ": self.center_id,
                "Specie ": self.species}

    @staticmethod
    def get_centers_animals(_center_id):
        """Finding animals in some center

        :param _center_id: id of some center
        :return: animals in some center
        """
        return [Animal.center_animals(animal)
                for animal in
                Animal.query.filter_by(center_id=_center_id).all()]

    @staticmethod
    def get_id(_name):
        """Getting id of animal by name

        :param _name: name of some animal
        :return: animal id
        """
        animal = Animal.query.filter_by(name=_name).first()
        return animal.id

    @staticmethod
    def get_all_animal():
        """Getting all animals

        :return: all animals
        """
        return [Animal.json(animal) for animal in Animal.query.all()]

    @staticmethod
    def update_animal(request, animal_id, name, age):
        """Update information about animal

        :param request: request of input form
        :param animal_id: id of some animal
        :param name: name of some animal
        :param age: age of some animal
        :return: nothing
        """
        animal = Animal.query.filter_by(id=animal_id).first()
        if name is None and age is not None:
            animal.age = age
        elif name is not None and age is None:
            animal.name = name
        else:
            animal.name = name
            animal.age = age
        db.session.commit()
        loggers(request, animal.center_id, 'Animal was updated', animal.id)

    @staticmethod
    def delete_animal(request, animal_id):
        """Deleting animal by id

        :param request: request of some url
        :param animal_id: id of some animal
        :return: nothing
        """
        animal = Animal.query.filter_by(id=animal_id).first()
        Animal.query.filter_by(id=animal_id).delete()
        db.session.commit()
        loggers(request, animal.center_id, 'Animal was deleted', animal.id)

    @staticmethod
    def check_animal_before_delete(animal_id):
        """Check if animal exists

        :param animal_id: id of some animal
        :return: boolean
        """
        animal = Animal.query.filter_by(id=animal_id).first()
        if animal is None:
            return True
        else:
            return False
