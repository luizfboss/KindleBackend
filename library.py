from database import all_books

class Library:
    def __init__(self):
        self.books = []
        self.current_book = None