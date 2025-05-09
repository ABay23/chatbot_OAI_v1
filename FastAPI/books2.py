from fastapi import Body, HTTPException, FastAPI
from mock_data import BOOKS

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS

# * CH Fetch all books by author
@app.get('/books/{book_author}')
async def get_all_books_author(book_author : str):
        books_returned = []
        for book in BOOKS:
            if book.get('author').casefold() == book_author.casefold():
                books_returned.append(book)
        return books_returned


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('/books/')        
async def read_category_by_query(book_category: str):
    books_return = []
    for book in BOOKS:
        if book.get('category').casefold() == book_category.casefold():
            books_return.append(book)
    return books_return


@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_category: str, book_author : str):
    books_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == book_category.casefold():
                books_return.append(book)
    return books_return


# * New Book with POST Request
@app.post('/books/create_book')
async def create_new_book(new_book = Body()):
    if new_book['title'] not in BOOKS:
        BOOKS.append(new_book)
        
# * Update a book with PUT Request
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    try:
        for i in range(len(BOOKS)):
                if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
                    BOOKS[i] = updated_book
                    return {'message': 'Book Updated!'}
        '''Raise exceptions using FastAPI docs'''
        raise HTTPException(status_code=404, detail='Book Not found')
    except AttributeError as e:
        raise HTTPException(status_code=400, detail=f'Bad Request Format: {str(e)}')
    
# * Delete a book with DELETE request
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    try:
        for i in range(len(BOOKS)):
            if BOOKS[i].get('title').casefold() == book_title.casefold():
                BOOKS.pop(i)
                return {'Message': 'Book Successfully deleted!'}
        raise HTTPException(status_code=404, detail = f'Book Not Found')
    except AttributeError as e:
        raise HTTPException(status_code=400, detail = f'Bad Request Format: {str(e)}')
    
