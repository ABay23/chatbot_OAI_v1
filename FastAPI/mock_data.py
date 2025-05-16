"""Mock Data for testing purposes"""
from typing import List, Dict
from pydantic import BaseModel, Field
from typing import Optional
'''
BOOKS: List[Dict[str, str]] = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "The Two Towers", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "The Return of the King", "author": "J.R.R. Tolkien", "category": "Fantasy"},
    {"title": "The Silmarillion", "author": "J.R.R. Tolkien", "category": "Mythology"},
    
    {"title": "Harry Potter and the Sorcerer"s Stone", "author": "J.K. Rowling", "category": "Fantasy"},
    {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "category": "Fantasy"},
    {"title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "category": "Fantasy"},
    {"title": "Harry Potter and the Goblet of Fire", "author": "J.K. Rowling", "category": "Fantasy"},
    {"title": "Harry Potter and the Order of the Phoenix", "author": "J.K. Rowling", "category": "Fantasy"},
    
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy"},
    {"title": "A Clash of Kings", "author": "George R.R. Martin", "category": "Fantasy"},
    {"title": "A Storm of Swords", "author": "George R.R. Martin", "category": "Fantasy"},
    {"title": "A Feast for Crows", "author": "George R.R. Martin", "category": "Fantasy"},
    {"title": "A Dance with Dragons", "author": "George R.R. Martin", "category": "Fantasy"}
]

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
'''
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    
    def __init__(self, id:int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(description= 'ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new Book",
                "author": "Alejo",
                "description": "Nice Book",
                "rating": 4
            }
        }
    }
    
    
        
BOOKS = [
    Book(1, "The Hobbit", "J.R.R. Tolkien", "A fantasy adventure about Bilbo Baggins.", 5),
    Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien", "First part of the epic trilogy.", 5),
    Book(3, "The Two Towers", "J.R.R. Tolkien", "Middle chapter of the Lord of the Rings.", 5),
    Book(4, "The Return of the King", "J.R.R. Tolkien", "Final battle for Middle-earth.", 5),
    Book(5, "The Silmarillion", "J.R.R. Tolkien", "Mythic prequel to the Lord of the Rings.", 4),
    
    Book(6, "The Shining", "Stephen King", "A haunted hotel drives a man insane.", 5),
    Book(7, "It", "Stephen King", "A shape-shifting monster terrorizes a town.", 4),
    Book(8, "Misery", "Stephen King", "A fan holds her favorite author hostage.", 5),
    Book(9, "Carrie", "Stephen King", "A bullied girl develops telekinetic powers.", 4),
    Book(10, "Doctor Sleep", "Stephen King", "Sequel to The Shining, following Danny.", 4),

    Book(11, "1984", "George Orwell", "A dystopian society under total surveillance.", 5),
    Book(12, "Animal Farm", "George Orwell", "A satirical tale of revolution and power.", 4),
    
    Book(13, "Dune", "Frank Herbert", "A sci-fi epic about politics and prophecy.", 5),
    Book(14, "Dune Messiah", "Frank Herbert", "The continued struggle of Paul Atreides.", 4),
    
    Book(15, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "The start of a magical journey.", 5),
    Book(16, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Mystery and danger at Hogwarts.", 5),
    Book(17, "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", "A fugitive on the loose.", 5),
    Book(18, "Harry Potter and the Goblet of Fire", "J.K. Rowling", "Triwizard Tournament and dark revelations.", 4),

    Book(19, "A Game of Thrones", "George R.R. Martin", "Noble families battle for the throne.", 5),
    Book(20, "A Clash of Kings", "George R.R. Martin", "The war of five kings begins.", 4),
    Book(21, "A Storm of Swords", "George R.R. Martin", "Betrayals and bloody battles.", 5),

    Book(22, "Brave New World", "Aldous Huxley", "A genetically engineered society.", 4),
    Book(23, "Fahrenheit 451", "Ray Bradbury", "Books are outlawed and burned.", 4),
    
    Book(24, "The Martian", "Andy Weir", "A stranded astronaut survives on Mars.", 5),
    Book(25, "Project Hail Mary", "Andy Weir", "A lone astronaut must save Earth.", 4),

    Book(26, "The Alchemist", "Paulo Coelho", "A boy searches for his personal legend.", 4),
    Book(27, "The Da Vinci Code", "Dan Brown", "A conspiracy hidden in religious symbols.", 4),
    Book(28, "Angels & Demons", "Dan Brown", "A race against time and secret societies.", 4),

    Book(29, "The Road", "Cormac McCarthy", "A bleak journey of father and son.", 5),
    Book(30, "The Power of Now", "Eckhart Tolle", "A spiritual guide to living in the present.", 4),
]
