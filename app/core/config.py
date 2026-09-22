from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    ALLOWED_ORIGINS: str = "*"
    MODEL_VERSION: str = "1.0.0"
    DEMO_MODE: bool = True
    PORT: int = 8000
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
