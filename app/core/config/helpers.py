from core.init import flask_app
def zeer_config(key):
    # Helper function to get configuration values
    return flask_app.config.get(f"ZEER_{key}", None)
