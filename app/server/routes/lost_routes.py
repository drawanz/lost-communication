from fastapi import APIRouter, Body
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


@router.post("/", response_description="Lost communication added into the dabase")
async def add_lost_data(lost: LostSchema = Body(...)):
    lost_communication = jsonable_encoder(lost)
    new_lost = await add_lost_communication(lost_communication)
    if new_lost:
        return ResponseModel(new_lost, "Lost communication created")
    raise HTTPException(400, "There is something wrong with the body data")