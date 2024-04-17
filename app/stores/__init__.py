from importlib import import_module
from core.config.helpers import zeer_config

import json


class BaseStore:
    def store(self, data):
        raise NotImplementedError

    def get(self, oid):
        results = self.retrieve({"oid": oid})
        if len(results) > 0:
            raise ValueError(f"Multiple entries found for oid {oid}")
        elif len(results) == 0:
            return ValueError(f"No entry found for oid {oid}")
        return results[0]

    def retrieve(self, filters=None):
        raise NotImplementedError

    def serialize(self, data):
        return json.dumps(data)

    @classmethod
    def get_provider(cls):
        store_provider = zeer_config("DEFAULT_STORE")
        store_module = import_module(f"stores.{store_provider}")

        all_stores_config = zeer_config("STORES_CONFIG") or {}
        store_config = all_stores_config.get(store_provider, {})

        class_name = f"{store_provider.title()}Store"
        store_class = getattr(store_module, class_name)

        return store_class(store_config)
