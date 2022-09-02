import motor.motor_asyncio

from helpers.helpers import lost_communication_helper

conn_str = "mongodb+srv://drawanz:91683711@cluster0.lyevp6n.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)

database = client.lost

lost_collection = database.get_collection("lost_collection")

# Retrieve all lost communications in the database
async def retrieve_lost_communications():
    losts = []
    async for lost in lost_collection.find():
        lost.append(lost_communication_helper(lost))
    if len(losts) < 1:
        return False
    return losts


# Add a new lost communication into to the database
async def add_lost_communication(lost_data: dict) -> dict:
    lost = await lost_collection.insert_one(lost_data)
    new_lost = await lost_collection.find_one({"_id": lost.inserted_id})
    if len(new_lost) < 1:
        return False
    return lost_communication_helper(new_lost)


# Retrieve a lost communication with a matching CPF
async def retrieve_lost_communication(CPF: int) -> dict:
    lost = await lost_collection.find_one({"CPF": (CPF)})
    if len(lost) < 1:
        return False
    return lost_communication_helper(lost)


# Update a lost communication with a matching CPF
async def update_lost_communication(CPF: int, data: dict):
    if len(data) < 1:
        return False
    lost = await lost_collection.find_one({"CPF": (CPF)})
    if lost:
        updated_lost = await lost_collection.update_one({"CPF": (CPF)}, {"$set": data})
        if updated_lost:
            return True
        return False
    return False


# Delete a lost communication from the database
async def delete_lost_communication(CPF: int):
    lost = await lost_collection.find_one({"CPF": (CPF)})
    if lost:
        await lost_collection.delete_one({"CPF": (CPF)})
        return True
    return False
