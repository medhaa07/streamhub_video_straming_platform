from app.home import home_bp
from app.auth import auth_bp
from app.dashboard import dashboard_bp
from app.video import video_bp
from app.stream import stream_bp
from app.notification.routes import notification_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(stream_bp)
    app.register_blueprint(notification_bp)