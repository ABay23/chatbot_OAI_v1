from fastapi import FastAPI
from mock_data import BOOKS

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS