from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder


from server.database import (
    retrieve_lost_communications,
    add_lost_communication,
    retrieve_lost_communication,
    update_lost_communication,
    delete_lost_communication,
)


from server.models.lost import (
    ResponseModel,
    UpdateLostSchema,
    LostSchema,
)


router = APIRouter()

# Create
@router.post("/", response_description="Lost communication added into the dabase")
async def add_lost_data(lost: LostSchema = Body(...)):
    lost_communication = jsonable_encoder(lost)
    new_lost = await add_lost_communication(lost_communication)
    if new_lost:
        return ResponseModel(200, new_lost, "Lost communication created")
    raise HTTPException(400, "There is something wrong with the body data")


# Read
@router.get("/", response_description="Lost communication read from the dabase")
async def get_all_losts_data():
    losts = await retrieve_lost_communications()
    if losts:
        return ResponseModel(200, losts, "All losts communications in the database")
    raise HTTPException(404, "Not possible to find any data")


@router.get(
    "/{cpf}", response_description="Read data about a specific lost communication"
)
async def get_a_lost_data(cpf: str):
    lost = await retrieve_lost_communication(int(cpf))
    if lost:
        return ResponseModel(
            200, lost, "Lost communication data retrieved successfully"
        )
    raise HTTPException(404, "Lost communication doesn't exist.")


# Update
@router.put(
    "/{cpf}", response_description="Update data about a specific lost communication"
)
async def update_a_lost_data(cpf: str, req: UpdateLostSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_lost = await update_lost_communication(int(cpf), req)
    if update_lost:
        return ResponseModel(
            200, update_lost, f"Lost communication data of CPF:{cpf} updated"
        )
    raise HTTPException(
        404, "Not possible to find CPF or the body request is incompleted"
    )


# Delete
@router.delete(
    "/{cpf", response_description="Lost communication data deleted from the database"
)
async def delete_a_lost_data(cpf: str):
    deleted_lost = await delete_lost_communication(int(cpf))
    if deleted_lost:
        return ResponseModel(
            200, deleted_lost, f"Lost communication data of CPF:{cpf} deleted"
        )
    raise HTTPException(404, "Not possible to find CPF")
