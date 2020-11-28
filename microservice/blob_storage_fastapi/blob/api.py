import os
import shutil

from fastapi import APIRouter, UploadFile
from fastapi.params import Depends, File
from sqlalchemy.orm import Session
from starlette.responses import FileResponse, JSONResponse

from blob.models import MetaCreate, MetaRead
from blob.service import create, get_by_key
from config import UPLOAD_FOLDER
from data.database import get_db

blob_router = APIRouter()


@blob_router.post("/upload", response_model=MetaRead)
def create_file(*, file: UploadFile = File(...), db_session: Session = Depends(get_db)):
    """
    upload a new file.
    """
    meta_in = MetaCreate()
    meta_in.file_name, meta_in.content_type = file.filename, file.content_type
    meta_read = create(db_session=db_session, meta_in=meta_in)
    if meta_read.id > 0:
        with open(os.path.join(UPLOAD_FOLDER, 'temp', str(meta_read.id)), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return meta_read


@blob_router.get('/download')
def get_file(*, key: str, db_session: Session = Depends(get_db)):
    meta_read = get_by_key(db_session=db_session, meta_key=key)
    if not meta_read.path:
        meta_read.path = os.path.join(UPLOAD_FOLDER, 'temp', str(meta_read.id))

    if meta_read:
        path = os.path.join(UPLOAD_FOLDER, meta_read.path)
        return FileResponse(path, media_type=meta_read.content_type, filename=meta_read.file_name)
    return JSONResponse(status_code=404, content={"message": "Item not found"})
