from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]


    MONGODB_URI_TESTS: str
    MONGODB_DATABASE_TESTS: str

    MONGODB_URL:str
    MONGODB_NAME:str



    SECRET_KEY: str

    CLIENT_GOOGLE_ID: str
    CLIENT_SECRET_KEY: str

    SECRET_KEY_ACCESS: str
    SECRET_KEY_REFRESH: str
    ALGORITHM: str

    ACCESS_TIME_TOKEN: int
    REFRESH_TOKEN_EXPIRATION: int

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()