from fastapi import FastAPI
from mock_data import BOOKS

app = FastAPI()

@app.get('/')
async def get_all_books():
    return BOOKS