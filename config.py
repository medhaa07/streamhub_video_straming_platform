import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads",
        "videos"
    )

    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "ffmpeg")

    MAX_CONTENT_LENGTH = 500 * 1024 * 1024

    # FFmpeg executable
    FFMPEG_PATH = os.getenv("FFMPEG_PATH", "ffmpeg")