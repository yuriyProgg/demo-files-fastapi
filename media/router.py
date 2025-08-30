from fastapi import APIRouter
from fastapi.responses import FileResponse
from core.settings import MEDIA_ROOT

router = APIRouter(prefix="/media", tags=["media"])


@router.get("/{file_name}")
async def get_file(file_name: str):
    return FileResponse(MEDIA_ROOT / file_name)
