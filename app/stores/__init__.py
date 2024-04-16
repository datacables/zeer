from importlib import import_module
from config import zeer_config

def get_store(flask_app):
    store_provider = zeer_config(flask_app, "DEFAULT_STORE")
    store_module = import_module(f"stores.{store_provider}")
    store_config = zeer_config(flask_app, "STORE_CONFIG") or {}
    return store_module.Store(store_config.get(store_provider, {}))