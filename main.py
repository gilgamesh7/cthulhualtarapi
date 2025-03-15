from fastapi import FastAPI
from app.config import WEATHER_API_KEY
from app.middleware import setup_middleware
from app.routers import health

app = FastAPI()

# Configure middleware
setup_middleware(app)  

# Include routes
app.include_router(health.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
