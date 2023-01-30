import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: str = Field(..., env="DB_PORT")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_SCHM: str = Field(..., env="DB_SCHM")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PSWD: str = Field(..., env="DB_PSWD")
    DB_URL: str = Field(..., env="DB_URL")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        # env_fname = "local.env"
        env_fname = 'docker.env'
        env_file = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/core/{env_fname}"
        env_file_encoding = "utf-8"


settings = Settings()
