import os

from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity


def create_app(conf_type=None):

    conf_type = conf_type or os.environ["SETTINGS"]

    app = Flask(
        __name__,
        template_folder="../client/dist",
        static_folder="../client/dist/static",
    )
    app.config.from_object("server.config." + conf_type)

    from server.models import db
    from flask_migrate import Migrate

    db.init_app(app)
    migrate = Migrate(app, db)

    from server.models import User

    CORS(app, resources={r"/*": {"origins": "*"}})

    def authenticate(email, password):
        user = User.query.filter_by(email=email).scalar()
        if user and user.check_password(password):
            return user

    def identity(payload):
        user_id = payload["identity"]
        return User.query.get(user_id)

    jwt = JWT(app, authenticate, identity)

    from server.home import home_bp
    from server.auth import auth_bp
    from server.foods import foods_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(foods_bp)

    return app
