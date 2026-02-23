from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.post("/upload")
async def upload_reports(files: List[UploadFile] = File(...)):
    return {
        "filenames": [file.filename for file in files]
    }