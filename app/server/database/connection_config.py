import motor.motor_asyncio
from decouple import config


conn_str = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str or 'test', serverSelectionTimeoutMS=5000)

database = client.lost

lost_collection = database.get_collection("lost_collection")