from fastapi import APIRouter
from ..services.mux_service import MuxService
from ..config import Config

config = Config()
router = APIRouter(tags=["timelapses"], prefix="/timelapse")
mux_api = MuxService(config.mux_token_id, config.mux_token_secret)

@router.get("/assets")
def get_assets():
    assets = mux_api.get_assets()
    return {"assets": assets}



    
