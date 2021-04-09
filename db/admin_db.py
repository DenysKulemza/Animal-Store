from flask_sqlalchemy import SQLAlchemy
from settings import app
from logger.logging import loggers

db = SQLAlchemy(app)


class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True)
  #  center_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(10), nullable=False)
  #  description = db.Column(db.String(100))
  #  age = db.Column(db.Integer, nullable=False)
  #  species = db.Column(db.String(15), nullable=False)
  #  price = db.Column(db.Integer)

    def json(self):
        """Represent name of animals in json format

        :return: name of animals
        """
        return {'Name': self.name}

    def current_admin(self):
        """Represent information about current animal in json format

        :return: information about current animal
        """
        return {'Center id': self.center_id, 'Name': self.name,
                'Description': self.description, 'Age': self.age,
                'Species': self.species, 'Price': self.price}

    @staticmethod
    def display_current_admin(_id):
        """Finds an animal in the database by id

        :param _id: id of some animal
        :return: information about this animal
        """
        animal = Admin.query.filter_by(id=_id).first()
        return Admin.current_animal(animal)

    @staticmethod
    def add_admin(request, _center_id, _name,
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
        new_animal = Admin(center_id=_center_id, name=_name,
                            description=_description, age=_age,
                            species=_species, price=_price)
        db.session.add(new_animal)
        db.session.commit()
        loggers(request, _center_id, 'New animal was added', new_animal.id)

    @staticmethod
    def get_id(_name):
        """Getting id of animal by name

        :param _name: name of some animal
        :return: animal id
        """
        animal = Admin.query.filter_by(name=_name).first()
        return animal.id

    @staticmethod
    def update_admin(request, _id, _name):
        """Update information about animal

        :param request: request of input form
        :param _id: id of some animal
        :param _name: name of some animal
        :param _age: age of some animal
        :return: nothing
        """
        animal = Admin.query.filter_by(id=_id).first()
        animal.name = _name
        db.session.commit()
        loggers(request, animal.center_id, 'Animal was updated', animal.id)

    @staticmethod
    def delete_admin(request, _id):
        """Deleting animal by id

        :param request: request of some url
        :param _id: id of some animal
        :return: nothing
        """
        animal = Admin.query.filter_by(id=_id).first()
        Admin.query.filter_by(id=_id).delete()
        db.session.commit()
        loggers(request, animal.center_id, 'Animal was deleted', animal.id)