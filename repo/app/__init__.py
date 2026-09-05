from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    from app.routes.auth import auth_bp
    from app.routes.booking import booking_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)

    with app.app_context():
        db.create_all()

    return app
