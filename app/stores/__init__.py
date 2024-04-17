from importlib import import_module
from config import zeer_config
import json


class Store:
    def store(self, data):
        raise NotImplementedError

    def retrieve(self):
        raise NotImplementedError

    def serialize(self, data):
        return json.dumps(data)

    @classmethod
    def get_store(cls, flask_app):
        store_provider = zeer_config(flask_app, "DEFAULT_STORE")
        store_module = import_module(f"stores.{store_provider}")
        store_config = zeer_config(flask_app, "STORE_CONFIG") or {}
        return store_module.Store(store_config.get(store_provider, {}))
