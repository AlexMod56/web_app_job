from flask import Flask
from src.logging_config import setup_logging


def create_app():
    app = Flask(__name__)

    setup_logging()

    with app.app_context():
        from src.routes import bp
        app.register_blueprint(bp)

    return app