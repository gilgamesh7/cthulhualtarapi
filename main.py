from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
weather_api_key = os.getenv("WEATHER_API_KEY")  # Retrieve from environment variable
if not weather_api_key:
    raise ValueError("API key is missing. Set WEATHER_API_KEY as an environment variable.")
print(f"API key: {weather_api_key}")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://brave-rock-040a7c310.4.azurestaticapps.net",  # Production frontend
                "http://localhost:3001"  ],  # Local development frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/v1/alive")
def alive():
    return {"message": "Cthulhu F'thagn!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
