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
