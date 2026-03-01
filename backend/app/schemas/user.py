from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    settings: Optional[dict] = None

class User(UserBase):
    id: str
    subscription_tier: str
    subscription_status: str
    monthly_credits_used: int
    monthly_credits_limit: int
    total_videos_created: int
    total_avatars_created: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

class UserStats(BaseModel):
    videos_created: int
    avatars_created: int
    credits_remaining: int
    credits_total: int
    subscription_plan: str
