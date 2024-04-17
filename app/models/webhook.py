from sqlalchemy import Column, String

from models.base import BaseModel
from core.init import db

from shortuuid import uuid


# Database model for webhook
class Webhook(BaseModel):
    __tablename__ = "webhook"
    oid = Column(String, unique=True)
    token = Column(String, unique=True)  # for authentication
    email = Column(String, unique=True)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def create(cls, email):
        # Generate unique oid and token
        token = str(uuid())
        oid = str(uuid())

        if cls.get_by_email(email):
            return None

        # Create new webhook entry
        new_entry = Webhook(oid=oid, token=token, email=email)

        # Add entry to database session
        session = db.session
        try:
            session.add(new_entry)
            session.commit()
            return new_entry
        except Exception as e:
            # Handle database errors
            print(f"Error storing data: {e}")
            session.rollback()
            return None
        finally:
            session.close()


# # Create database tables (run only once)
# Base.metadata.create_all(engine)
