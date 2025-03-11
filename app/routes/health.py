from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/alive")
def alive():
    return {"message": "Cthulhu F'thagn!"}