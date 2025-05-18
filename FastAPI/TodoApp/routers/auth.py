from fastapi import FastAPI, APIRouter

# app = FastAPI()  #* We don't use FastAPI for endpoints, auth endpoints are created usng router
router = APIRouter()

'''Get User'''
@router.get('/auth/')
async def get_user():
    return {'message': 'Authenticated'}