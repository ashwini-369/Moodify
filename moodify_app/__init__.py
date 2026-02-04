from flask import Flask
from .config import SECRET_KEY

def create_app():
    app = Flask(
        __name__,
        template_folder="../ui/templates",
        static_folder="../ui/static"
    )

    app.secret_key = SECRET_KEY

    from .routes import main
    app.register_blueprint(main)

    return app
