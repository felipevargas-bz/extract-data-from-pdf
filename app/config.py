from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Settings(BaseSettings):

    WEB_APP_TITLE: str = Field(...)
    WEB_APP_DESCRIPTION: str = """
    Extract information from a pdf, the application makes use of OCR recognition to extract the information from the pdf that is uploaded to the server, this application was built with pytesseract as a library to extract the information from the pdf. pytesseract returns the text to which we subsequently filter the information we need through Regular Expressions, the information to be extracted from the pdf is as follows.

        * Vendor Name
        * Fiscal Number
        * Contract Number
        * Start Date
        * End Date
        * Comments paragraph
    After extracting the information, it is saved in the database in a table called extractions.

    This project makes use of the following libraries to extract and filter the information that you want to obtain.

        * [pdf2image 1.16.0] convert pdf to image
        * [pytesseract 0.3.7] receives an image and returns the text that is recognized in the image.
        * [re] It is used for handling regular expressions in python, it was used to extract the desired information from the text that pytesseract returns.

    Technologies
        * Python
        * PostgreSQL
        * Docker
        * FastApi
        * SQLAlchemy ORM
    """
    WEB_APP_VERSION: str = Field(...)

    DATABASE_URL: str = Field(...)


settings = Settings()


engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
