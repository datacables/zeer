from sqlalchemy.orm import declarative_base
from core.init import db

Base = declarative_base()


class BaseModel(db.Model):
    """Generic base model for Flask applications using SQLAlchemy."""

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    deleted_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.id})>"
