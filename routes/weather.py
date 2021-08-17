from typing import List
from fastapi import Body, APIRouter
from database.database import weather_collection
from models.weather import WeatherForecast, ResponseModel, ErrorResponseModel
from datetime import datetime, timedelta, date, time

router = APIRouter()


@router.post("/")
async def add_record(data: List[WeatherForecast] = None):
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
async def query_weekly_forestcasts(query_date: date = None, time_interval: str = None):
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
            if not time_interval:
                cursor = weather_collection.find(query)
                async for item in cursor:
                    res.append(WeatherForecast(**item))

            else:
                query["period_string"] = time_interval
                item = await weather_collection.find_one(query)
                res.append(WeatherForecast(**item))
        else:
            cursor = weather_collection.find()
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
