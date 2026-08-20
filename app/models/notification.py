import uuid

from sqlalchemy.dialects.postgresql import UUID

from extensions import db
from app.models.base import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    message = db.Column(
        db.String(255),
        nullable=False,
    )

    icon = db.Column(
        db.String(50),
        default="bi-bell",
    )

    is_read = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    user = db.relationship(
        "User",
        backref="notifications",
    )