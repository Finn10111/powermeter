from flask import Flask
from flask_smorest import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
ma = Marshmallow()


def create_app(cfg='default'):
    from config import config
    app = Flask(__name__)
    app.config.from_object(config[cfg])
    app.url_map.strict_slashes = False

    config[cfg].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import resources

    api = Api()
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    resources.register_blueprints(api)

    return app
