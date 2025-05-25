from turtle import st
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from models import Todos
from database import SessionLocal
from typing import Annotated, Dict
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description : str = Field(max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete : bool

        
'''THis is the get all query first test'''
@router.get('/')
async def read_all(user: user_dependency, db: db_dependency):
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()

'''Get todo by ID'''
@router.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency , db: db_dependency, todo_id : int = Path(gt=0)):
    if user is None:
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Authenticated')
        
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo Not found')

'''POST on the new DB setting'''
@router.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(
    user: user_dependency,
    db: db_dependency, 
    todo_request: TodoRequest
):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Authenticated')
    new_todo = Todos(**todo_request.model_dump(), owner_id=user.get('id'))
    
    db.add(new_todo)
    db.commit()
    return {'message': f'New Todo Created!!!'}

'''PUT Update a todo'''
@router.put('/todo/{todo_id}')
async def update_todo(
    user: user_dependency,
    db : db_dependency, 
    todo_request : TodoRequest,
    todo_id : int = Path(gt=0) 
    ):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not Authenticated')
    todo_update = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
    if todo_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo not found')
    
    todo_update.title = todo_request.title
    todo_update.description = todo_request.description
    todo_update.priority = todo_request.priority
    todo_update.complete = todo_request.complete
    
    db.add(todo_update)
    db.commit()
    
    return {'message': f'The task: {todo_update.title} was Updated!'}

'''Adding Delete '''
@router.delete('/todo/{todo_id}')
async def delete_todo(
    db: db_dependency,
    todo_id : int = Path(gt=0)
):
    todo_content = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todo_content:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    db.delete(todo_content)
    db.commit()
    return {'message': f'The task ({todo_content.title}) was deleted!'}