from sqlalchemy import Column, String

from models.base import BaseModel

from shortuuid import uuid


# Database model for webhook
class Webhook(BaseModel):
    __tablename__ = "webhook"
    oid = Column(String, unique=True)
    token = Column(String, unique=True)  # for authentication
    email = Column(String, unique=True)

    def create(self, email):
        # Generate unique oid and token
        oid = str(uuid.uuid4())
        token = str(uuid.uuid4())

        # Create new webhook entry
        new_entry = Webhook(oid=oid, token=token, email=email)

        # Add entry to database session
        session = BaseModel.db().session
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
