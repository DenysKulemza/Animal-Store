from db import db
from logger.logging import loggers


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(10), nullable=False)

    @staticmethod
    def add_comment(request, comment, user_name):
        """Adding some user

        :param request: of the input form
        :param comment: comment from customer
        :param user_name: user_name of some user
        """
        new_comment = Review(comment=comment, name=user_name)
        db.session.add(new_comment)
        db.session.commit()
        loggers(request, new_comment.id, 'New comment was added', new_comment.id)

    def display_reviews(self):
        """Display comment

        :return: comment
        """
        return {'Name: ': self.comment}

    @staticmethod
    def get_all_review():
        """Getting all comments

        :return: comments
        """
        return [Review.display_centers(user) for user in Review.query.all()]
