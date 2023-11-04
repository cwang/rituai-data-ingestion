from motor import motor_asyncio

from app.core.config import MONGODB_URL
from app.models.ingestion import IncomingDataItem

client = motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
collection = client.get_default_database().get_collection("incoming-data")


async def save_data(data: IncomingDataItem):
    result = await collection.insert_one(data.model_dump())
    return result.inserted_id
