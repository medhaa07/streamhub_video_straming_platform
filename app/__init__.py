from flask import Flask

from config import Config
from extensions import db, login_manager, migrate

from app.blueprints import register_blueprints


def create_app():
    flask_app = Flask(__name__)

    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    login_manager.init_app(flask_app)
    migrate.init_app(flask_app, db)

    import app.models

    from flask_login import current_user
    from app.models.notification import Notification

    @flask_app.context_processor
    def notification_context():

        if current_user.is_authenticated:

            notifications = (
                Notification.query
                .filter_by(user_id=current_user.id)
                .order_by(Notification.created_at.desc())
                .limit(10)
                .all()
            )

            unread_count = (
                Notification.query
                .filter_by(
                    user_id=current_user.id,
                    is_read=False
                )
                .count()
            )

        else:
            notifications = []
            unread_count = 0

        return dict(
            notifications=notifications,
            unread_count=unread_count
        )

    print(type(flask_app), flask_app)

    register_blueprints(flask_app)

    return flask_app