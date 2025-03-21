from fastapi import APIRouter, HTTPException
import httpx
from datetime import datetime, timedelta

from .get_eldritch_text import get_eldritch_text


from config import WEATHER_API_KEY

router = APIRouter()

ASTRONOMY_API_URL = "https://api.weatherapi.com/v1/astronomy.json"
ASTRONOMY_API_CITY = "Auckland"
astronomy_prediction_date = f"{(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')}"

@router.get("/api/v1/astroprediction")
async def get_astronomy_prediction():
    params = {
        "key": WEATHER_API_KEY,
        "q": ASTRONOMY_API_CITY,
        "dt": astronomy_prediction_date
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(ASTRONOMY_API_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return get_eldritch_text(response.json())