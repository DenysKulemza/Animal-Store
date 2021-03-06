from db.access_request import AccessToken
from db.animal_db import Animal
from db.specie_db import Specie


def get_specie(name):
    """ Get specie by name

    :param name: name of specie
    :return: specific specie by name
    """
    return Specie.query.filter_by(name=name).first()


def get_access():
    """ Return last id by token

    :return: last access id by toke
    """
    return AccessToken.query.order_by(AccessToken.id.desc()).first()


def get_animal_id__by_name_for_logger():
    """Getting animal id by name for logging it

    :return: id of some animal
    """
    animal = Animal.query.order_by(Animal.id.desc()).first()
    return animal.id


def get_specie_by_name_for_logger():
    """Getting specie id by name for logging it

    :return: specie id
    """
    specie = Specie.query.order_by(Specie.id.desc()).first()
    return specie.id
