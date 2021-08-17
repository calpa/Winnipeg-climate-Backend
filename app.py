from fastapi import FastAPI

from routes.weather import router as WeatherRouter

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix="/weather")
