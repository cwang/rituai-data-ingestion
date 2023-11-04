from fastapi import APIRouter

from app.api.routes import consumer

router = APIRouter()
router.include_router(consumer.router, tags=["data"], prefix="/v1")
