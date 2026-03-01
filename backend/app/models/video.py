from sqlalchemy import Column, String, DateTime, Integer, JSON, ForeignKey, Text, Enum
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Video(Base):
    __tablename__ = "videos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    # Video details
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="processing")  # processing, completed, failed

    # URLs
    video_url = Column(String)
    thumbnail_url = Column(String)
    audio_url = Column(String)

    # Content
    script = Column(Text)
    style = Column(String, default="cinematic")
    aspect_ratio = Column(String, default="9:16")
    duration = Column(Integer)  # in seconds

    # Faceless video specific
    voice_gender = Column(String, default="female")
    voice_accent = Column(String, default="american")
    captions_enabled = Column(Boolean, default=True)
    background_music = Column(String)

    # Metadata
    metadata = Column(JSON, default={})
    tags = Column(JSON, default=[])

    # Engagement
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    published_at = Column(DateTime(timezone=True))
