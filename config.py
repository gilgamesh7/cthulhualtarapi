import os

# Fetch the API key from the environment
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("API key is missing. Set WEATHER_API_KEY as an environment variable.")
