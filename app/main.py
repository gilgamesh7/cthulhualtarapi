from fastapi import FastAPI
from app.config import WEATHER_API_KEY
from app.middleware import setup_middleware
# from . import health

app = FastAPI()

from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/alive")
def alive():
    return {"message": "Cthulhu F'thagn!"}

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
