from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
import shutil

router = APIRouter()

@router.post("/form/data/submit")
async def submit_form_data(
    name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    form_data = schemas.FormDataBase(name=name, email=email)
    return crud.create_form_data(db, form_data, file_location)
