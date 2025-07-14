from sqlalchemy import Column, Integer, String
from .database import Base

class FormData(Base):
    __tablename__ = "form_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    document_path = Column(String)
