from fastapi import FastAPI
from app.routes import api_1, api_2
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Form Assignment API")

app.include_router(api_1.router)
app.include_router(api_2.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the KPA Backend"}