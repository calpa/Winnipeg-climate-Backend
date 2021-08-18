import uvicorn
from fastapi import FastAPI

from routes.weather import router as WeatherRouter

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix="/weather")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
