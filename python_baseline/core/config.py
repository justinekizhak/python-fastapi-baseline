from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List, Union
import os


class Settings(BaseSettings):
    PRODUCTION_ENV: bool = False
    PROJECT_NAME: str = "Python Baseline"
    DEBUG: bool = True
    VERSION: str = "v0.1.0"
    API_V1_STR: str = "/api/v1"
    API_DOC: str = "/api"
    API_SWAGGER_URL: str = "/api/swagger"
    API_REDOC_URL: str = "/api/redoc"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 5000
    SERVER_RELOAD: bool = True
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def post_init_settings():
    def check_debug():
        if settings.PRODUCTION_ENV:
            return False
        return True

    settings.DEBUG = check_debug()
    settings.SERVER_RELOAD = check_debug()


settings = Settings()
post_init_settings()


def set_env(key: str, value: str):
    os.environ[key] = value
