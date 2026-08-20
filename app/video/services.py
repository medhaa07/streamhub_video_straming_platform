import os
import uuid
import shutil
import subprocess

from flask import current_app
from werkzeug.utils import secure_filename

from extensions import db
from app.models.video import Video
from app.video.validators import allowed_file


class VideoService:

    @staticmethod
    def save_video(
        file,
        title,
        description,
        category,
        visibility,
        owner_id,
    ):

        original_filename = secure_filename(file.filename)

        if not original_filename:
            raise ValueError("Invalid filename.")

        if not allowed_file(original_filename):
            raise ValueError("Unsupported video format.")

        extension = os.path.splitext(original_filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        upload_folder = current_app.config["UPLOAD_FOLDER"]

        thumbnail_folder = os.path.join(
            os.path.dirname(upload_folder),
            "thumbnails",
        )

        os.makedirs(upload_folder, exist_ok=True)
        os.makedirs(thumbnail_folder, exist_ok=True)

        filepath = os.path.join(
            upload_folder,
            filename
        )

        file.save(filepath)

        thumbnail_filename = (
            f"{os.path.splitext(filename)[0]}.jpg"
        )

        thumbnail_path = os.path.join(
            thumbnail_folder,
            thumbnail_filename
        )

        # Find FFmpeg automatically.
        # This works when FFmpeg is installed and added
        # to the system PATH on the user's machine.
        ffmpeg_path = shutil.which("ffmpeg")

        if not ffmpeg_path:
            # Optional fallback for your own development machine.
            configured_ffmpeg = current_app.config.get(
                "FFMPEG_PATH"
            )

            if configured_ffmpeg and os.path.isfile(
                configured_ffmpeg
            ):
                ffmpeg_path = configured_ffmpeg

        if not ffmpeg_path:

            if os.path.exists(filepath):
                os.remove(filepath)

            raise RuntimeError(
                "FFmpeg was not found. "
                "Please install FFmpeg and add it to "
                "the system PATH."
            )

        try:

            subprocess.run(
                [
                    current_app.config["FFMPEG_PATH"],
                    "-y",
                    "-i",
                    filepath,
                    "-ss",
                    "00:00:01",
                    "-vframes",
                    "1",
                    "-vf",
                    (
                        "thumbnail,"
                        "scale=640:360:"
                        "force_original_aspect_ratio=increase,"
                        "crop=640:360"
                    ),
                    thumbnail_path,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True,
            )

        except subprocess.CalledProcessError:

            if os.path.exists(filepath):
                os.remove(filepath)

            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

            raise RuntimeError(
                "FFmpeg could not generate the video thumbnail."
            )

        video = Video(
            title=title,
            description=description,
            filename=filename,
            original_filename=original_filename,
            thumbnail_filename=thumbnail_filename,
            category=category,
            visibility=visibility,
            owner_id=owner_id,
        )

        try:

            db.session.add(video)

            db.session.commit()

            return video

        except Exception:

            db.session.rollback()

            if os.path.exists(filepath):
                os.remove(filepath)

            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

            raise

    @staticmethod
    def delete_video(video_id, owner_id):

        video = Video.query.filter_by(
            id=video_id,
            owner_id=owner_id
        ).first()

        if not video:
            raise ValueError(
                "Video not found or you don't have permission."
            )

        upload_folder = current_app.config[
            "UPLOAD_FOLDER"
        ]

        # Delete actual video file
        if video.filename:

            video_path = os.path.join(
                upload_folder,
                video.filename
            )

            if os.path.exists(video_path):
                os.remove(video_path)

        # Delete thumbnail
        if video.thumbnail_filename:

            thumbnail_folder = os.path.join(
                os.path.dirname(upload_folder),
                "thumbnails"
            )

            thumbnail_path = os.path.join(
                thumbnail_folder,
                video.thumbnail_filename
            )

            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)

        # Delete database entry
        db.session.delete(video)

        db.session.commit()