from flask import Blueprint, jsonify
from flask_login import login_required, current_user

from app.models.notification import Notification
from extensions import db

notification_bp = Blueprint(
    "notification",
    __name__,
    url_prefix="/notification",
)


@notification_bp.route("/delete/<notification_id>", methods=["POST"])
@login_required
def delete(notification_id):

    notification = Notification.query.filter_by(
        id=notification_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(notification)
    db.session.commit()

    return jsonify({"success": True})


@notification_bp.route("/clear", methods=["POST"])
@login_required
def clear():

    Notification.query.filter_by(
        user_id=current_user.id
    ).delete()

    db.session.commit()

    return jsonify({"success": True})