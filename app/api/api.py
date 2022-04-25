from fastapi import APIRouter

from app.api.endpoints import extract_router

api_router = APIRouter()

api_router.include_router(router=extract_router, tags=['Extractions'])
