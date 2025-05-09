"""Mock Data for testing purposes"""
from typing import List, Dict

# BOOKS: List[Dict[str, str]] = [
#     {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
#     {"title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "category": "Fantasy"},
#     {"title": "The Two Towers", "author": "J.R.R. Tolkien", "category": "Fantasy"},
#     {"title": "The Return of the King", "author": "J.R.R. Tolkien", "category": "Fantasy"},
#     {"title": "The Silmarillion", "author": "J.R.R. Tolkien", "category": "Mythology"},
    
#     {"title": "Harry Potter and the Sorcerer"s Stone", "author": "J.K. Rowling", "category": "Fantasy"},
#     {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "category": "Fantasy"},
#     {"title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "category": "Fantasy"},
#     {"title": "Harry Potter and the Goblet of Fire", "author": "J.K. Rowling", "category": "Fantasy"},
#     {"title": "Harry Potter and the Order of the Phoenix", "author": "J.K. Rowling", "category": "Fantasy"},
    
#     {"title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy"},
#     {"title": "A Clash of Kings", "author": "George R.R. Martin", "category": "Fantasy"},
#     {"title": "A Storm of Swords", "author": "George R.R. Martin", "category": "Fantasy"},
#     {"title": "A Feast for Crows", "author": "George R.R. Martin", "category": "Fantasy"},
#     {"title": "A Dance with Dragons", "author": "George R.R. Martin", "category": "Fantasy"}
# ]

BOOKS: list[dict[str, str]] = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "Dune", "author": "Frank Herbert", "category": "Sci-Fi"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "category": "Thriller"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Romance"},
    
    {"title": "The Shining", "author": "Stephen King", "category": "Horror"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classic"},
    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "category": "Fantasy"},
    {"title": "The Martian", "author": "Andy Weir", "category": "Sci-Fi"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "category": "Mystery"},

    {"title": "Becoming", "author": "Michelle Obama", "category": "Biography"},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "category": "Nonfiction"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Spiritual"},
    {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "category": "Thriller"},
    {"title": "Me Before You", "author": "Jojo Moyes", "category": "Romance"},

    {"title": "It", "author": "Stephen King", "category": "Horror"},
    {"title": "Brave New World", "author": "Aldous Huxley", "category": "Dystopian"},
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy"},
    {"title": "Ready Player One", "author": "Ernest Cline", "category": "Sci-Fi"},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "category": "Mystery"},

    {"title": "Educated", "author": "Tara Westover", "category": "Biography"},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Nonfiction"},
    {"title": "Twilight", "author": "Stephenie Meyer", "category": "Romance"},
    {"title": "Dracula", "author": "Bram Stoker", "category": "Horror"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "category": "Dystopian"},

    {"title": "The Road", "author": "Cormac McCarthy", "category": "Post-Apocalyptic"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "category": "Self-Help"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Improvement"},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "category": "Spiritual"},
    {"title": "And Then There Were None", "author": "Agatha Christie", "category": "Mystery"}
]

def categories(books):
    categories = set()
    for book in books:
        if book["category"] not in categories:
            categories.add(book["category"])
    return categories

print(categories(BOOKS))