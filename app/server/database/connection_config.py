import motor.motor_asyncio
from decouple import config
# import os


conn_str = config("MONGO_DETAILS")
# conn_str = os.environ.get("MONGO_DETAILS", "mongodb")
print(conn_str)


client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

database = client.lost

lost_collection = database.get_collection("lost_collection")