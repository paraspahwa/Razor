from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey, Text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Payment(Base):
    __tablename__ = "payments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    # Payment details
    amount = Column(Float, nullable=False)
    currency = Column(String, default="INR")
    status = Column(String, default="pending")  # pending, completed, failed, refunded

    # Gateway info
    gateway = Column(String, default="razorpay")  # razorpay, stripe
    gateway_payment_id = Column(String)
    gateway_order_id = Column(String)
    gateway_signature = Column(String)

    # Subscription info
    subscription_id = Column(String, ForeignKey("subscriptions.id"))
    plan_id = Column(String)

    # Metadata
    metadata = Column(JSON, default={})

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    # Plan details
    plan_id = Column(String, nullable=False)  # starter, creator, pro
    plan_name = Column(String)
    amount = Column(Float)
    currency = Column(String, default="INR")
    interval = Column(String, default="monthly")  # monthly, yearly

    # Gateway info
    gateway = Column(String, default="razorpay")
    gateway_subscription_id = Column(String)

    # Status
    status = Column(String, default="active")  # active, paused, cancelled, expired
    current_period_start = Column(DateTime(timezone=True))
    current_period_end = Column(DateTime(timezone=True))

    # Cancellation
    cancelled_at = Column(DateTime(timezone=True))
    cancellation_reason = Column(Text)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
