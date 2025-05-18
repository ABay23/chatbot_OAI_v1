from fastapi import FastAPI, Depends
import models
from models import Todos
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
        
db_dependency = Annotated[Session, Depends(get_db)]
        
'''THis is the get all query first test'''
@app.get('/')
async def read_all(db: db_dependency):
    return db.query(Todos).all()

'''Get todo by ID'''
@app.get('/todo/{tpfp_id}')
async def read_todo(db: db_dependency, todo_id : int):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    return todo_model