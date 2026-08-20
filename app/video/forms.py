from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class UploadVideoForm(FlaskForm):

    title = StringField(
        "Title",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ],
    )

    description = TextAreaField(
        "Description",
        validators=[
            Length(max=1000),
        ],
    )

    category = SelectField(
        "Category",
        choices=[
            ("education", "Education"),
            ("gaming", "Gaming"),
            ("music", "Music"),
            ("technology", "Technology"),
            ("sports", "Sports"),
            ("other", "Other"),
        ],
    )

    visibility = SelectField(
        "Visibility",
        choices=[
            ("public", "Public"),
            ("private", "Private"),
        ],
    )

    video = FileField(
        "Video",
        validators=[
            FileRequired(),
            FileAllowed(
                ["mp4", "mov", "avi", "mkv", "webm"],
                "Only video files are allowed.",
            ),
        ],
    )

    submit = SubmitField("Upload Video")