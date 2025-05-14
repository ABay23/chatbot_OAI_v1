'''Books ans CRUD '''
from fastapi import FastAPI, HTTPException
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
        
'''Get books by Category'''

@app.get('/books/')
async def get_books_by_category(category: str):
    book_category = []
    try:
        for book in BOOKS:
            if book.get('category').casefold() == category.casefold():
                book_category.append(book)
        return book_category
    except ValueError as e:
        raise HTTPException(status_code=404, detail= f'Category not found : {str(e)}')
    
'''Get mixing dynamic Params and Query params'''

@app.get('/books/{book_author}/')
async def get_books_author_and_Category(book_author: str, book_category: str):
    books_return = []
    # try:
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == book_category.casefold():
                books_return.append(book)
                
    return books_return
    # except ValueError as e:
    #     raise HTTPException(status_code=404, detail= f'No match found: {str(e)}')