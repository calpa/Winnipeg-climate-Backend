from typing import Optional

from datetime import date, datetime
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class WeatherForecast(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    date_time_local: datetime
    period_index: int
    period_string: Optional[str]
    cloudprecip: Optional[str]
    visibility_other: Optional[str]
    winds: Optional[str]
    temperatures: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
