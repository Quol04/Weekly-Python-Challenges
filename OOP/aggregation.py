
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)    

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author, ):
        self.title = title
        self.author = author

library = Library("City Library")

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
       

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)     

print(f"Books in {library.name}:")
for book in library.books:
    print(f"{book.title} by {book.author}")

print(library.list_books())    