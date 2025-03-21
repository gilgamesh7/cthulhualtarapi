import os

# Fetch the API key from the environment
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

if not WEATHER_API_KEY :
    raise ValueError("API key is missing. Set WEATHER_API_KEY as an environment variable.")

if not CHATGPT_API_KEY :
    raise ValueError("API key is missing. Set CHATGPT_API_KEY as an environment variable.")
