import motor.motor_asyncio
from decouple import config


conn_str = "mongodb+srv://drawanz:91683711@cluster0.lyevp6n.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

database = client.lost

lost_collection = database.get_collection("lost_collection")