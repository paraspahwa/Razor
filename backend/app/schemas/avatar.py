from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class AvatarBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    style: str = "ghibli"
    expression: str = "neutral"

class AvatarCreate(AvatarBase):
    original_image_url: str
    prompt: Optional[str] = None

class AvatarUpdate(BaseModel):
    name: Optional[str] = None
    expression: Optional[str] = None
    is_favorite: Optional[bool] = None

class Avatar(AvatarBase):
    id: str
    user_id: str
    original_url: str
    generated_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    prompt_used: Optional[str] = None
    is_favorite: bool
    use_count: int
    created_at: datetime

    class Config:
        from_attributes = True
