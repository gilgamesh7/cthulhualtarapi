from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/alive")
def alive():
    return {"message": "Cthulhu F'thagn!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
