from turtle import st
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from TodoApp.models import Todos
from TodoApp.database import SessionLocal
from typing import Annotated, Dict
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get('/todo', status_code=status.HTTP_200_OK)
async def rad_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Authentication Failed')
    return db.query(Todos).all()