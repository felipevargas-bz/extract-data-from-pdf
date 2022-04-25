from fastapi import FastAPI

from app.api.api import api_router
from app.config import Base, engine, settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    version=settings.WEB_APP_VERSION,
    title=settings.WEB_APP_TITLE,
    description=settings.WEB_APP_DESCRIPTION,
)

app.include_router(api_router, tags=['Extractions'])
