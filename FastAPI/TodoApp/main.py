from fastapi import FastAPI, Depends
import models
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
'''THis is the get all query first test'''
@app.get('/')
async def read_all(db: Annotated[Session, Depends(get_db)]):
    pass
