from fastapi import FastAPI, Body, HTTPException
from mock_data import BOOKS, Book, BookRequest

app = FastAPI()

@app.get('/books')
async def get_all_books():
    return BOOKS

@app.post('/create-book')
async def create_book(book_request: BookRequest):
    try:
        new_book = Book(**book_request.model_dump())
        BOOKS.append(new_book)
        return {'message': 'New book Created!'}
    except AttributeError as e:
        raise HTTPException(status_code=400, detail= f'Bad Request {str(e)}')