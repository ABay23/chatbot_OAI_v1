from fastapi import FastAPI
from mock_data import BOOKS

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}