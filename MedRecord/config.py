# DB/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:1234@localhost:5432/hospital_db"
    JWT_SECRET_KEY: str = "change_me_in_env"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"   # optional

settings = Settings()
