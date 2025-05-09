from fastapi import FastAPI
from mock_data import BOOKS

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS


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