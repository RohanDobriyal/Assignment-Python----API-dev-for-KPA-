from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("/form/data")
def get_form_data(db: Session = Depends(get_db)):
    return crud.get_form_data(db)
