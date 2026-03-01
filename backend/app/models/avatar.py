from sqlalchemy import Column, String, DateTime, Integer, JSON, ForeignKey, Text
from sqlalchemy.sql import func
from app.db.base import Base
import uuid

class Avatar(Base):
    __tablename__ = "avatars"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)

    # Avatar details
    name = Column(String)
    description = Column(Text)

    # Images
    original_url = Column(String)
    generated_url = Column(String)
    thumbnail_url = Column(String)

    # Settings
    style = Column(String, default="ghibli")  # ghibli, cyberpunk, etc.
    expression = Column(String, default="neutral")

    # Metadata
    prompt_used = Column(Text)
    negative_prompt = Column(Text)
    generation_params = Column(JSON, default={})

    # Usage
    is_favorite = Column(Boolean, default=False)
    use_count = Column(Integer, default=0)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
