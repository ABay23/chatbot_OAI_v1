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
        BOOKS.append(find_book_id(new_book))
        return {'message': 'New book Created!'}
    except AttributeError as e:
        raise HTTPException(status_code=400, detail= f'Bad Request {str(e)}')
    
def find_book_id(book : Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    
    return book

# def find_book_id(book: Book):
#     book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
#     return book

    
    
    
    
    
    
    
    
    
    
    
    # if len(BOOKS) > 0: 
    #     book.id = BOOKS[-1].id +1
    # else:
    #     book.id = 1
        
    # return book