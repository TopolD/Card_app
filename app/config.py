from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    MONGODB_URI: str
    MONGODB_URI_TESTS: str

    MONGODB_DATABASE: str
    MONGODB_DATABASE_TESTS: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()