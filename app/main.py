from core.app import flask_app
from core.urls import blueprints


def initialize():
    # Load config from settings first
    # This will be accessible from `core.config import zeer_config
    flask_app.config.from_object("settings")

    # register blueprints to routes
    for bp in blueprints:
        flask_app.register_blueprint(bp[0], url_prefix=bp[1])


# Flask app
if __name__ == "__main__":
    initialize()
    flask_app.run(debug=True)
