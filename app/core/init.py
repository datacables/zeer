from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flask_app = Flask(__name__)
flask_app.config.from_object("settings")
db = SQLAlchemy(flask_app, session_options={"expire_on_commit": False})
migrate = Migrate(flask_app, db)


def routes_initialize():
    from core.urls import blueprints

    for bp in blueprints:
        flask_app.register_blueprint(bp[0], url_prefix=bp[1])

    return flask_app


# db_initialize()
routes_initialize()
