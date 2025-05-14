from fastapi import FastAPI, Body, HTTPException
from mock_data import BOOKS, Book

app = FastAPI()

@app.get('/books')
async def get_all_books():
    return BOOKS

@app.post('/create-book')
async def create_book(book_request = Body()):
    try:
        BOOKS.append(book_request)
        return {'message': 'New book Created!'}
    except AttributeError as e:
        raise HTTPException(status_code=400, detail= f'Bad Request {str(e)}')