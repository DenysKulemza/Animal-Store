from db import db
from logger.logging import loggers


class Centers(db.Model):
    __tablename__ = 'centers'
    name = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String(40), nullable=False, primary_key=True)

    @staticmethod
    def add_center(request, name, city, address):
        """Adding some user

        :param request: of the input form
        :param name: name of some center
        :param city: city of some center
        :param address: address of some center
        :return: nothing
        """

        new_center = Centers(name=name, city=city, address=address)
        db.session.add(new_center)
        db.session.commit()
        loggers(request, new_center.id, 'New center was added', new_center.id)

    def display_centers(self):
        """Display centers with id

        :return: name of centers and id
        """
        return {'Name: ': self.login, 'Id: ': str(self.id)}

    @staticmethod
    def get_all_centers():
        """Getting all centers

        :return: centers
        """
        return [Centers.display_centers(center) for center in Centers.query.all()]
