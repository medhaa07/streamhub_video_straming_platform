from sqlalchemy import or_

from extensions import db
from app.models.user import User


class AuthService:

    @staticmethod
    def username_exists(username):
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def email_exists(email):
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def create_user(username, email, password):
        user = User(
            username=username,
            email=email
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter_by(email=email).first()

        if user is None:
            return None

        if not user.check_password(password):
            return None

        return user

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()