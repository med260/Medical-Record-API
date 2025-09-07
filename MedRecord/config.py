# DB/config.py
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Field
class Settings(BaseSettings):
    DATABASE_URL: str 
    JWT_SECRET_KEY: str 
    JWT_ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"   # optional

settings = Settings()
