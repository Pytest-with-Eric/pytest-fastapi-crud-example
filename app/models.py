from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy_utils import UUIDType
import uuid

class User(Base):
    __tablename__ = "users"

    # Primary key and GUID type
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)

    # String types with appropriate non-null constraints
    first_name = Column(
        String(255), nullable=False, index=True
    )  # Indexed for faster searches
    last_name = Column(
        String(255), nullable=False, index=True
    )  # Indexed for faster searches
    address = Column(String(255), nullable=True)

    # Boolean type with a default value
    activated = Column(Boolean, nullable=False, default=True)

    # Timestamps with timezone support
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
