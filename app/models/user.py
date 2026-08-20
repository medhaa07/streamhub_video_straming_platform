from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from extensions import db
from app.models.base import BaseModel


class User(BaseModel, UserMixin):

    __tablename__ = "users"

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    avatar = db.Column(
        db.String(255)
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    videos = db.relationship(
        "Video",
        back_populates="owner",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password_hash,
            password
        )