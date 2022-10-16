from fastapi import APIRouter
from .content.controller import router as content_router

api_router = APIRouter()
api_router.include_router(content_router, prefix="/content", tags=["content"])
