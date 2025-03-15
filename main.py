from fastapi import FastAPI

from middleware import setup_middleware
from routers import health, astronomy_prediction

app = FastAPI()

# Configure middleware
setup_middleware(app)  

# Include routes
app.include_router(health.router)
app.include_router(astronomy_prediction.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
