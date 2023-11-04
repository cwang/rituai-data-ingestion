from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class IngestionResponse(BaseModel):
    status: str


class DataType(str, Enum):
    email = "email"
    feed = "feed"


class IncomingDataItem(BaseModel):
    email_recipient: str
    data_type: DataType
    received_at: datetime | None = datetime.utcnow()
    extracted_content: str
    raw_content: str
    processed_at: datetime | None = None


class IncomingDataCollection(BaseModel):
    data: list[IncomingDataItem]

    def __init__(self, data: list[IncomingDataItem]):
        self.data = data
