from sqlalchemy.dialects.postgresql import UUID

from extensions import db
from app.models.base import BaseModel


class Video(BaseModel):
    __tablename__ = "videos"

    title = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text)

    filename = db.Column(db.String(255), nullable=False)

    original_filename = db.Column(db.String(255), nullable=False)
    thumbnail_filename = db.Column(
    db.String(255),
    nullable=True
)

    category = db.Column(db.String(50), nullable=False)

    visibility = db.Column(
        db.String(20),
        default="public"
    )

    views = db.Column(
        db.Integer,
        default=0
    )

    owner_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id"),
        nullable=False
    )

    owner = db.relationship(
        "User",
        back_populates="videos"
    )