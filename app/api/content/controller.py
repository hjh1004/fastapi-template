from fastapi import APIRouter, HTTPException
from .services import get
from .schemas import ContentRequest, ContentResponse

router = APIRouter()


@router.post("/")
async def find_content(request: ContentRequest):
    return get(request)
