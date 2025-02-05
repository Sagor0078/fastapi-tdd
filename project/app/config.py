import logging
import os
from functools import lru_cache

from pydantic import AnyUrl  # Import AnyUrl from pydantic
from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = bool(os.getenv("TESTING", 0))  # Convert to bool explicitly
    database_url: AnyUrl = os.environ.get("DATABASE_URL")  # Use AnyUrl from pydantic


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
