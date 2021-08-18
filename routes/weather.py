from typing import List
from fastapi import APIRouter
from database.database import weather_collection
from models.weather import WeatherForecast, ResponseModel, ErrorResponseModel
from datetime import datetime, timedelta, date, time

router = APIRouter()


@router.post("/")
async def add_weather_forecasts(data: List[WeatherForecast] = None):
    if len(data) == 1:
        insertOneResult = await weather_collection.insert_one(dict(data[0]))
        if insertOneResult.inserted_id:
            return ResponseModel(True, "Successfully added a record")
    elif len(data) > 1:
        insertManyResult = await weather_collection.insert_many(list(map(dict, data)))
        if len(insertManyResult.inserted_ids) > 0:
            return ResponseModel(True, "Successfully added %s records" % len(data))
    return ErrorResponseModel("An error occurred", 500, "Cannot create record")


@router.get("/")
async def query_weekly_weather_forecasts(
    query_date: date = None, query_hour: int = None
):
    try:
        query = {}
        cursor = None
        res = []
        if query_date:
            temp_date = datetime.combine(query_date, time.min)
            query["date_time_local"] = {
                "$gte": temp_date,
                "$lt": temp_date + timedelta(days=1),
            }
            if query_hour is not None:
                query["date_time_local"] = temp_date.replace(hour=query_hour)

        cursor = weather_collection.find(query)
        async for item in cursor:
            res.append(WeatherForecast(**item))

        if len(res) > 0:
            return ResponseModel(res, "Weekly Forecasts are available")
        elif len(res) == 0:
            return ResponseModel(res, "Weekly Forecasts are not available")
        return ErrorResponseModel(
            "An error occurred", 404, "Weather forecast are not available"
        )

    except Exception as err:
        print(err)
        return ErrorResponseModel(
            "An error occurred", 404, "Weather forecast are not available"
        )


@router.get("/available_days")
async def get_available_days():
    try:
        cursor = weather_collection.aggregate(
            [
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": "$date_time_local",
                            }
                        }
                    }
                }
            ]
        )
        res = await cursor.to_list(length=None)

        return ResponseModel(res, "Available Dates are returned")
    except Exception as e:
        print(e)
        return ErrorResponseModel("An error occurred", 500, "An error occurred")