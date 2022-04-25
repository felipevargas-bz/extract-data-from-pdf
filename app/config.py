from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):

    WEB_APP_TITLE: str = Field(...)
    WEB_APP_DESCRIPTION: str = Field(...)
    WEB_APP_VERSION: str = Field(...)

    DATABASE_URL: str = Field(...)


settings = Settings()


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
