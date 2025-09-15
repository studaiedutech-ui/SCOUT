from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "SCOUT Backend"
    environment: str = "development"
    version: str = "0.1.0"
    debug: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
