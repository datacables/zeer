def zeer_config(key):
    from core.app import flask_app

    # Helper function to get configuration values
    return flask_app.config.get(f"ZEER_{key}", None)
