from sqlalchemy import Column, String, DateTime, Boolean, Integer, JSON
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True)  # Nullable for OAuth
    full_name = Column(String)

    # OAuth providers
    google_id = Column(String, unique=True, index=True)
    github_id = Column(String, unique=True, index=True)

    # Subscription
    subscription_tier = Column(String, default="free")  # free, starter, creator, pro
    subscription_status = Column(String, default="inactive")
    subscription_id = Column(String)  # Razorpay/Stripe subscription ID
    current_period_end = Column(DateTime)

    # Usage tracking
    monthly_credits_used = Column(Integer, default=0)
    monthly_credits_limit = Column(Integer, default=10)
    total_videos_created = Column(Integer, default=0)
    total_avatars_created = Column(Integer, default=0)

    # Settings
    settings = Column(JSON, default={})

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
