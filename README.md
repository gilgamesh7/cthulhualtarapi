# cthulhualtarapi
API to for the cthulhualtar to consume

# Links
## Local
- [Check if alive](http://127.0.0.1:8000/api/v1/alive)
## Azure
- [Check if alive](https://cthulhualtar-api-begvgzh8guerb3ba.centralus-01.azurewebsites.net/api/v1/alive)

## Run
- Local & Azure Startup Command : gunicorn -k uvicorn.workers.UvicornWorker -w 4 main:app
