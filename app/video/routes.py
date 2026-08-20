from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from app.notification.services import NotificationService

from flask_login import login_required
from flask_login import current_user

from app.video.forms import UploadVideoForm
from app.video.services import VideoService


video_bp = Blueprint(
    "video",
    __name__,
    url_prefix="/video",
)


@video_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    form = UploadVideoForm()


    if form.validate_on_submit():

        try:

            video = VideoService.save_video(
    file=form.video.data,
    title=form.title.data,
    description=form.description.data,
    category=form.category.data,
    visibility=form.visibility.data,
    owner_id=current_user.id,
)

            NotificationService.create(
    user_id=current_user.id,
    message=f'"{video.title}" uploaded successfully.',
    icon="bi-cloud-upload",
)


            flash(
                "Video uploaded successfully!",
                "success",
            )


            return redirect(
                url_for("dashboard.dashboard")
            )


        except Exception as e:

            flash(
                f"Upload failed: {str(e)}",
                "danger",
            )


    return render_template(
        "video/upload.html",
        form=form,
    )



@video_bp.route("/delete/<video_id>", methods=["POST"])
@login_required
def delete(video_id):

    try:

        VideoService.delete_video(
            video_id=video_id,
            owner_id=current_user.id
        )


        flash(
            "Video deleted successfully!",
            "success"
        )


    except Exception as e:

        flash(
            f"Delete failed: {str(e)}",
            "danger"
        )


    return redirect(
        url_for("dashboard.dashboard")
    )