from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:Iory.Yagami_3009@db.spnocjpuvmmukiifrqae.supabase.co:5432/postgres'
    DBBaseModel: ClassVar = declarative_base()

    JWT_SECRET: str = '1QFu5t_L-mWF23NseEilDKUWPrD--2fGtCBrwAm_I9I'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    """Enviroment Setings"""
    model_config = SettingsConfigDict(
    env_file=".env", env_file_encoding="utf-8", extra="allow", case_sensitive = True
    )
    
    #class Config:
    #    case_sensitive = True

settings = Settings() 
