from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Database
    database_url: str = Field(..., alias="DATABASE_URL")

    # JWT
    jwt_secret: str = Field(..., alias="JWT_SECRET")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_days: int = Field(default=7, alias="ACCESS_TOKEN_EXPIRE_DAYS")

    # CORS
    frontend_url: str = Field(default="http://localhost:3000", alias="FRONTEND_URL")

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
