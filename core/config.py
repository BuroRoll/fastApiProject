import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI"
    wsdlLink: str = 'http://192.168.119.187:8080/inv.motiv.ru/InvApiCore?wsdl'
    # SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost:5432/fastapi_db"

    # class Config:
    #     env_file = ".env"


settings = Settings()
