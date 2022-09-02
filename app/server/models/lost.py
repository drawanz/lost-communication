from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LostSchema(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    CPF: int = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)
    lavoura: str = Field(...)
    data_colheita: date = Field(...)
    evento: str = Field(...)


class UpdateStudentModel(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    CPF: int = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)
    lavoura: str = Field(...)
    data_colheita: date = Field(...)
    evento: str = Field(...)


def ResponseModel(code, data, message):
    return {
        "code": code,
        "data": [data],
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
