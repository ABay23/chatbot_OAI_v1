'''Books ans CRUD '''
from fastapi import FastAPI

app = FastAPI()

'''First Get MethodReques and API endpoint'''
@app.get('/first_endpoint')
async def first_api():
    print({'Name': 'Alejandro'})