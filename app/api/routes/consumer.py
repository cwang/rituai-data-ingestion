from fastapi import APIRouter, Body, Depends, Form, HTTPException
from loguru import logger

from app.models.ingestion import HealthResponse, IncomingDataItem, IngestionResponse
from app.services.consuming import save_data

router = APIRouter()


@router.post(
    "/data",
    response_model=IngestionResponse,
    name="data:consume",
)
async def consume(
    item: IncomingDataItem = Body(...),
) -> IngestionResponse:
    try:
        logger.debug("Received data: {}", item)
        _id = await save_data(item)
        logger.debug("Saved data with id: {}", _id)
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Exception: {err}")

    return IngestionResponse(status="ok")


@router.get(
    "/health",
    response_model=HealthResponse,
    name="health:get-data",
)
async def health() -> HealthResponse:
    try:
        return HealthResponse(status="ok")
    except Exception:
        raise HTTPException(status_code=404, detail="Unhealthy")
