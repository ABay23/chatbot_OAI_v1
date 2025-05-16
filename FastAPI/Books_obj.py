from fastapi import FastAPI, Body, HTTPException
from starlette import status
from mock_data import BOOKS, Book, BookRequest

app = FastAPI()

'''Get All Books'''
@app.get('/books')
async def get_all_books():
    return BOOKS
    
    
'''Get Book by ID'''
@app.get('/books/{get_book_by_id}')
async def get_book_by_id(book_id : int):
    try:
        for book in BOOKS:
            if book.id == book_id:
                return book
    except:
        raise HTTPException(status_code=404,  detail= f'Category not found')
    
'''FEtch Books by Rating'''
@app.get('/books/', status_code=status.HTTP_200_OK)
async def books_by_rating(rating : int):
    try:
        rated_books = []
        for book in BOOKS:
            if book.rating == rating:
                rated_books.append(book)
            # raise HTTPException(status_code= 400, detail= f'Missing argument')
        return rated_books
    except AttributeError as e:
        raise HTTPException(status_code= 404, detail= f'Rating not Found : {str(e)}')
    
def find_book_id(book : Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

'''Create new Book'''
@app.post('/create-book')
async def create_book(book_request: BookRequest):
    try:
        new_book = Book(**book_request.model_dump())
        BOOKS.append(find_book_id(new_book))
        return {'message': 'New book Created!'}
    except AttributeError as e:
        raise HTTPException(status_code=400, detail= f'Bad Request {str(e)}')
    
'''Update  Book'''
@app.put("/books/update_book")
async def update_book( book : BookRequest):
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i] = book
            return {'message': f'Book updated to {book}'}
        
'''Delete Book'''
@app.delete('/books/delete-book')
async def delete_book(book : BookRequest):
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            deleted_book = BOOKS.pop(i)
            return {'message': f'Book {deleted_book.title} Successfully deleted'}
    
