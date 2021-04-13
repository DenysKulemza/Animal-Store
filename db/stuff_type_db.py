from db import db

from logger.logging import loggers


class StuffType(db.Model):
    __tablename__ = 'stuff_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    @staticmethod
    def add_stuff_type(request, name):
        """Adding some user

        :param request: of the input form
        :param name: name of stuff type
        """

        new_user = StuffType(name=name)
        db.session.add(new_user)
        db.session.commit()
        loggers(request, new_user.id, 'New stuff type was added', new_user.id)
