from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app(config_class="config.DevConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # --- Init extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # --- Register blueprints (to be added later)
    # from blueprints.auth.routes import auth_bp
    # from blueprints.machines.routes import machines_bp
    # from blueprints.api.routes import api_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(machines_bp)
    # app.register_blueprint(api_bp, url_prefix="/api")

    # --- Simple hello route so you can test immediately
    @app.get("/")
    def index():
        return "<h2>Agriculture Machinery Rental – Flask version running!</h2>"

    return app


# --- CLI shortcut: `python app.py`
if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=True)
