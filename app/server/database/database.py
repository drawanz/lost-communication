from helpers.helpers import lost_communication_helper


from server.database.connection_config import lost_collection


# Retrieve all lost communications in the database
async def retrieve_lost_communications():
    losts = []
    async for lost in lost_collection.find():
        losts.append(lost_communication_helper(lost))
    if losts:
        return losts
    return False


# Add a new lost communication into to the database
async def add_lost_communication(lost_data: dict) -> dict:
    lost = await lost_collection.insert_one(lost_data)
    new_lost = await lost_collection.find_one({"_id": lost.inserted_id})
    if new_lost:
        return lost_communication_helper(new_lost)
    return False


# Retrieve a lost communication with a matching CPF
async def retrieve_lost_communication(CPF: str) -> dict:
    lost = await lost_collection.find_one({"CPF": int(CPF)})
    if lost:
        return lost_communication_helper(lost)
    return False


# Update a lost communication with a matching CPF
async def update_lost_communication(CPF: int, data: dict):
    # if len(data) < 1:
    #     return False
    lost = await lost_collection.find_one({"CPF": int(CPF)})
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
