from pydantic import AnyHttpUrl
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "BoEnergo Service"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    class Config:
        case_sensitive = True


settings = Settings()

