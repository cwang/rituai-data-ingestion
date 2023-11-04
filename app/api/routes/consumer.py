from fastapi import APIRouter, Body, HTTPException
from loguru import logger

from app.models.consumption import HealthResponse, IncomingDataItem, ConsumerResponse
from app.services.consuming import save_data

router = APIRouter()


@router.post(
    "/data",
    response_model=ConsumerResponse,
    name="data:consume",
)
async def consume(
    item: IncomingDataItem = Body(...),
) -> ConsumerResponse:
    try:
        logger.debug("Received data: {}", item)
        _id = await save_data(item)
        logger.debug("Saved data with id: {}", _id)
    except Exception as err:
        logger.exception(err)
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return ConsumerResponse(status="ok")


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health() -> HealthResponse:
    try:
        return HealthResponse(status="ok")
    except Exception:
        logger.exception("Health check failed")
        raise HTTPException(status_code=404, detail="Unhealthy")
