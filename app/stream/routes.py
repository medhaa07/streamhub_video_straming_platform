from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
    Response,
    send_file,
)

import os

from app.models.video import Video
from flask import send_from_directory


stream_bp = Blueprint(
    "stream",
    __name__,
    url_prefix="/watch",
)

@stream_bp.route("/thumbnail/<filename>")
def thumbnail(filename):
    folder = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        "..",
        "thumbnails",
    )

    return send_from_directory(
        os.path.abspath(folder),
        filename,
    )


@stream_bp.route("/<uuid:video_id>")
def watch(video_id):

    video = Video.query.get_or_404(video_id)

    return render_template(
        "stream/player.html",
        video=video,
    )


@stream_bp.route("/video/<uuid:video_id>")
def stream_video(video_id):

    video = Video.query.get_or_404(video_id)

    filepath = os.path.join(
        current_app.config["UPLOAD_FOLDER"],
        video.filename,
    )

    file_size = os.path.getsize(filepath)

    range_header = request.headers.get("Range")

    if range_header:

        byte1, byte2 = 0, None

        match = range_header.replace(
            "bytes=", ""
        ).split("-")

        if match[0]:
            byte1 = int(match[0])

        if match[1]:
            byte2 = int(match[1])

        length = file_size - byte1

        if byte2 is not None:
            length = byte2 - byte1 + 1

        with open(filepath, "rb") as f:
            f.seek(byte1)
            data = f.read(length)

        response = Response(
            data,
            206,
            mimetype="video/mp4",
            direct_passthrough=True,
        )

        response.headers["Content-Range"] = (
            f"bytes {byte1}-{byte1 + length - 1}/{file_size}"
        )

        response.headers["Accept-Ranges"] = "bytes"

        return response

    return send_file(
        filepath,
        mimetype="video/mp4",
        conditional=True,
    )

    thumbnail_folder = os.path.join(
        current_app.root_path,
        "..",
        "uploads",
        "thumbnails",
    )

    return send_from_directory(
        thumbnail_folder,
        filename,
    )