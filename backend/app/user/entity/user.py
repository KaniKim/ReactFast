from uuid import uuid4

from sqlalchemy import Column, String, Enum, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.user.enums.user import UserStatus
from core import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(length=50), nullable=True, unique=True)
    status = Column(Enum(UserStatus), default=UserStatus.active)
    is_staff = Column(Boolean, nullable=True, default=False)
    is_superuser = Column(Boolean, nullable=True, default=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())

    profile = relationship("Profile", lazy="joined", uselist=False, backref="user")

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(String(length=36), primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String(length=36), ForeignKey("user.id", ondelete="CASCADE"), index=True)
    nick_name = Column(String(length=50), nullable=True, index=True)
    picture_url = Column(String(length=255), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
