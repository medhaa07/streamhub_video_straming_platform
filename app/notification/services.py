from extensions import db
from app.models.notification import Notification


class NotificationService:

    @staticmethod
    def create(user_id, message, icon="bi-bell"):

        notification = Notification(
            user_id=user_id,
            message=message,
            icon=icon,
        )

        db.session.add(notification)
        db.session.commit()