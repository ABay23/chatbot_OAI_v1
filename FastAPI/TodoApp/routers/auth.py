from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from TodoApp.database import SessionLocal
from TodoApp.models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt


# app = FastAPI()  #* We don't use FastAPI for endpoints, auth endpoints are created usng router
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

load_dotenv()
jwt_s_key = os.getenv('JWT_SECRET_KEY')
algo_enc = os.getenv('JWT_ALGORITHM')


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/token')

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
    
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

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, jwt_s_key, algorithm=algo_enc)

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, jwt_s_key, algorithms=[algo_enc])
        user_name: str = payload.get('sub')
        user_id : int = payload.get('id')
        user_role: str = payload.get('role')
        
        if user_name is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could Not Validate the User')
        
        return {'username': user_name, 'id': user_id, 'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could Not Validate the User')
    

'''Create User'''
@router.post('/', status_code=status.HTTP_201_CREATED)
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
@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data : Annotated[OAuth2PasswordRequestForm, Depends()],
    db : db_dependency):
    user_auth= authenticate_user(form_data.username, form_data.password, db)
    if not user_auth:
        return {'message': 'User not found!'}
    
    token = create_access_token(user_auth.username, user_auth.id, user_auth.role, timedelta(minutes=20))
    
    return {'access_token': token, 'token_type': 'bearer'}
# {'message':f'Welcome {form_data.username}' }