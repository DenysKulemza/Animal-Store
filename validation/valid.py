import re

from jwt import decode

from db.animal_db import Animal
from db.specie_db import Specie
from db.user_db import User
from logger.warning_log import warning_log


def valid_specie_for_animal(animal_object):
    """Check if specie exists

    :param animal_object: some animal
    :return: boolean
    """
    specie = Specie.query.filter_by(name=animal_object['Species']).first()
    if specie is None:
        warning_log("Specie does not exists. You should add it to database")
        return False
    else:
        return True


def valid_animals(animal_object):
    """Valid animal information

    :param animal_object: some animal
    :return: boolean
    """
    if ('Name' in animal_object
            and age_validation(animal_object)
            and valid_specie_for_animal(animal_object)):
        return True
    else:
        warning_log("Register data of animal are invalid")
        return False


def valid_user(user_object):
    """Valid center information

    :param user_object: some center
    :return: boolean
    """
    if ('Login' in user_object
            and 'Password' in user_object
            and 'Address' in user_object):
        return True
    else:
        warning_log("Register data of center is invalid")
        return False


def valid_species(species_object):
    """Valid specie information

    :param species_object: some specie
    :return: boolean
    """
    if ('Name' in species_object
            and 'Description' in species_object
            and price_validation(species_object)
            and specie_exists(species_object['Name'])):
        return True
    else:
        warning_log("Register data of specie is invalid")
        return False


def price_validation(obj):
    """Check price for correct input

    :param obj: some object
    :return: boolean
    """
    regular_number = re.compile(r'^\d+(?:.\d*)?$')
    if 'Price' in obj and regular_number.match(obj['Price']):
        return True
    else:
        warning_log(f"The price passed incorrect")
        return False


def age_validation(obj):
    """Check age for correct input

    :param obj: some object
    :return: boolean
    """
    regular_number = re.compile(r'^\d+(?:.\d*)?$')
    if 'Age' in obj and regular_number.match(obj['Age']):
        return True
    else:
        warning_log(f"The age passed incorrect")
        return False


def center_exists(login):
    """Check if some center exists

    :param login: login of some center
    :return: boolean
    """
    center = User.query.filter_by(login=login).first()
    if center is not None:
        warning_log(f"Center by this login: {login} is already exists")
        return True
    else:
        return False


def specie_exists(name):
    """Check if some specie exists

    :param name: name of some specie
    :return: boolean
    """
    specie = Specie.query.filter_by(name=name).first()
    if specie is not None:
        warning_log(f"Specie by this name: {name}  exists")
        return False
    else:
        return True


def check_center_before_delete(center_id, animal_id):
    """Check center before delete

        :param center_id: id of some center
        :param animal_id: id of some animal
        :return: boolean
        """
    animal = Animal.query. \
        filter_by(id=animal_id).filter_by(center_id=center_id).first()
    if animal is not None:
        return True
    else:
        warning_log(f"Center by this id: {center_id} "
                    f"does not have animal by this id {animal_id}")
        return False


def valid_token(token, config):
    """Check if token is valid

    :param token: token of center
    :param config: secret config
    :return: if except return boolean
    """
    try:
        decode(token, config)
    except Exception:
        warning_log("Invalid token")
        return True


def valid_login_password(login, password):
    """Valid user login and password

    :param login: login of some center
    :param password: password of some center
    :return: boolean
    """
    user = User.query.filter_by(login=login, password=password).first()
    if user is not None:
        return True
    else:
        return False
