from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "AnimeForge"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database
    SUPABASE_URL: str
    SUPABASE_KEY: str
    DATABASE_URL: str

    # AI Services
    REPLICATE_API_TOKEN: str
    ANTHROPIC_API_KEY: str

    # Storage
    CLOUDFLARE_R2_ENDPOINT: str
    CLOUDFLARE_R2_ACCESS_KEY: str
    CLOUDFLARE_R2_SECRET_KEY: str
    CLOUDFLARE_R2_BUCKET: str

    # Payments - Razorpay (Primary for India)
    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str
    RAZORPAY_WEBHOOK_SECRET: str

    # Payments - Stripe (International)
    STRIPE_PUBLISHABLE_KEY: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # Feature Flags
    ENABLE_FACELESS_VIDEO: bool = True
    ENABLE_AVATAR_GENERATION: bool = True
    ENABLE_VIDEO_EDITING: bool = True

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
