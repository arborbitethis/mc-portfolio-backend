from fastapi import APIRouter
from ..config import Config

config = Config()
router = APIRouter(tags=["portfolio"], prefix="/portfolio")

@router.get("/test")
def get_test():
    return {"test": "hooray"}

