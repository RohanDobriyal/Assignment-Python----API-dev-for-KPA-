from pydantic import BaseModel

class FormDataBase(BaseModel):
    name: str
    email: str

class FormDataResponse(FormDataBase):
    id: int
    document_path: str

    class Config:
        orm_mode = True
