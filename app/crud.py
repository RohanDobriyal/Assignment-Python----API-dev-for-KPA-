from sqlalchemy.orm import Session
from . import models, schemas

def create_form_data(db: Session, data: schemas.FormDataBase, file_path: str):
    db_data = models.FormData(**data.dict(), document_path=file_path)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_form_data(db: Session):
    return db.query(models.FormData).all()
