from fastapi import APIRouter

from .manga import router as manga_router

router = APIRouter()
router.include_router(manga_router)