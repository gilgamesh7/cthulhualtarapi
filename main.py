from fastapi import FastAPI
from config import WEATHER_API_KEY
from middleware import setup_middleware
from routers import health

app = FastAPI()
app.include_router(health.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
