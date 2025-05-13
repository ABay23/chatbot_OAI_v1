'''Books ans CRUD '''
from fastapi import FastAPI
from mock_data import BOOKS

app = FastAPI()

'''First Get MethodReques and API endpoint'''
@app.get('/')
async def first_api():
    return {'Name': 'Alejandro'}

'''Endpoint returning a specific book with dynamic params'''
@app.get('/books/{book_title}')
async def get_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book