import uuid

from core.init import db
from models.base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType


# Database model for webhook
class Webhook(BaseModel):
    __tablename__ = "webhook"
    oid = Column(
        UUIDType(binary=True),
        default=uuid.uuid4,
    )
    token = Column(String, unique=True)  # for authentication
    email = Column(String, unique=True)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def create(cls, email):
        # Generate unique oid and token
        token = BaseModel.random_string(15, prefix="wh.tk")
        oid = BaseModel._oid()

        if cls.get_by_email(email):
            return None, "Duplicate Email"

        # Create new webhook entry
        new_entry = Webhook(oid=oid, token=token, email=email)

        # Add entry to database session
        session = db.session()
        try:
            session.add(new_entry)
            session.commit()
            return new_entry, None
        except Exception as e:
            # Handle database errors
            print(f"ERROR !! Webhook Create failed - {e}")
            session.rollback()
        finally:
            session.close()
        return None, "Error registering webhook for the email specified"

