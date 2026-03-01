from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class VideoBase(BaseModel):
    title: str
    description: Optional[str] = None
    script: Optional[str] = None
    style: str = "cinematic"
    aspect_ratio: str = "9:16"
    voice_gender: str = "female"
    voice_accent: str = "american"
    captions_enabled: bool = True
    background_music: Optional[str] = None

class VideoCreate(VideoBase):
    pass

class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class Video(VideoBase):
    id: str
    user_id: str
    status: str
    video_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    audio_url: Optional[str] = None
    duration: Optional[int] = None
    views: int
    likes: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class FacelessVideoRequest(BaseModel):
    script: str
    style: str = "cinematic"
    voice_gender: str = "female"
    voice_accent: str = "american"
    background_music: Optional[str] = None
    captions: bool = True
    aspect_ratio: str = "9:16"
