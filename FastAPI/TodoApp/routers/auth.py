import os
from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter
from pydantic import BaseModel
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm


# app = FastAPI()  #* We don't use FastAPI for endpoints, auth endpoints are created usng router
router = APIRouter()

jwt_key = os.getenv('JWT_SECRET_KEY')
algo = os.getenv('JWT_ALGORYTHM')

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user_validation = db.query(Users).filter(Users.username == username).first()
    if not user_validation:
        return False
    if not bcrypt_context.verify(password, user_validation.hashed_password):
        return False
    return user_validation

'''Create User'''
@router.post('/auth', status_code=status.HTTP_201_CREATED)
async def create_user(
    db : db_dependency,
    create_user_request : CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active = True
        
    )
    
    db.add(create_user_model)
    db.commit()
    return {'message': f'New user ({create_user_model.username}) created'}

'''POST Request'''
@router.post('/token')
async def login_for_access_token(
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
    db : db_dependency):
    user_auth= authenticate_user(form_data.username, form_data.password, db)
    if not user_auth:
        return {'message': 'User not found!'}
    return {'message':f'Welcome {form_data.username}' }