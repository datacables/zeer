import random
import string
import uuid

from core.init import db
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(db.Model):
    """Generic base model for Flask applications using SQLAlchemy."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    @classmethod
    def _oid(cls):
        return uuid.uuid4()

    @classmethod
    def random_string(cls, length=8, prefix=""):
        source = string.ascii_letters + string.digits
        chars = [random.choice(source) for i in range(length)]
        chars = "".join(chars)
        if prefix:
            prefix_len = len(prefix)
            return f"{prefix}_{chars[:length-prefix_len]}"
        else:
            return chars

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.id})>"
