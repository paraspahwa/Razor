from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class Plan(BaseModel):
    id: str
    name: str
    description: str
    amount: float
    currency: str
    interval: str
    features: List[str]
    credits_per_month: int

class SubscriptionRequest(BaseModel):
    plan_id: str
    interval: str = "monthly"  # monthly, yearly

class PaymentVerify(BaseModel):
    razorpay_payment_id: Optional[str] = None
    razorpay_order_id: Optional[str] = None
    razorpay_signature: Optional[str] = None
    stripe_payment_intent_id: Optional[str] = None

class SubscriptionResponse(BaseModel):
    id: str
    plan_id: str
    status: str
    current_period_end: Optional[datetime]
    gateway: str
