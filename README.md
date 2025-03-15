# cthulhualtarapi
API to for the cthulhualtar to consume

# Links
## Local
- [Check if alive](http://127.0.0.1:8000/api/v1/alive)
- [Astronomy Prediction](http://127.0.0.1:8000/api/v1/astroprediction)
## Azure
- [Check if alive](https://cthulhualtar-api-begvgzh8guerb3ba.centralus-01.azurewebsites.net/api/v1/alive)
- [Check if alive](https://cthulhualtar-api-begvgzh8guerb3ba.centralus-01.azurewebsites.net/api/v1/astroprediction)

# Setup
## Local
- Mac/Linux : export WEATHER_API_KEY=your_actual_key

## Azure
- RG : rg-cthulhualtar
- Webapp : cthulhualtar-api
- ASP : ASP-cthulhualtar (F1: 1)
- Location : Central US 
- In the Appservice -> Settings -> Environment variables
    - WEATHER_API_KEY

## Run
- Local & Azure Startup Command : gunicorn -k uvicorn.workers.UvicornWorker -w 4 main:app

## API
- [Weather API](https://www.weatherapi.com/api-explorer.aspx#astronomy)



