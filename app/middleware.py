from fastapi.middleware.cors import CORSMiddleware

def setup_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["https://brave-rock-040a7c310.4.azurestaticapps.net",  # Production frontend
                    "http://localhost:3001"  ],  # Local development frontend
        allow_credentials=True,
        allow_methods=["*"],  # Allow all methods
        allow_headers=["*"],  # Allow all headers
    )