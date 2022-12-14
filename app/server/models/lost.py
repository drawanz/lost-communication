from datetime import date

from pydantic import BaseModel, EmailStr, Field


class LostSchema(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    CPF: int = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)
    lavoura: str = Field(...)
    data_colheita: str = Field(...)
    evento: str = Field(...)


class UpdateLostSchema(BaseModel):
    nome: str = Field(...)
    email: EmailStr = Field(...)
    CPF: int = Field(...)
    latitude: float = Field(...)
    longitude: float = Field(...)
    lavoura: str = Field(...)
    data_colheita: str = Field(...)
    evento: str = Field(...)


def ResponseModel(code, data, message):
    return {
        "code": code,
        "data": [data],
        "message": message,
    }
