from flask import Blueprint
from flask import render_template

from flask_login import login_required
from flask_login import current_user

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard",
)


@dashboard_bp.route("/")
@login_required
def dashboard():

    videos = current_user.videos

    stats = {
        "videos": len(videos),
        "views": sum(video.views for video in videos),
        "storage": "0 MB",   # We'll calculate this later
    }

    return render_template(
        "dashboard/dashboard.html",
        user=current_user,
        videos=videos,
        stats=stats,
    )