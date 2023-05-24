from book import Book

class Library(Book):
    def __init__(self):
        self.books = []
        self.current_book = None   

    def Home(self):
        print('=-'*20)
        print("\n")
        print("HOME PAGE")
        print("Welcome back!")
        print()
        # Display all books and percentage read
        # Template:
        # <BOOK NAME> - <PERCENTAGE READ>
        for book in self.books:
            print(f"{book['Title']} - {book['Percentage_read']}%")
        print("\n")
        print('=-'*20)

    def Select(self, title):
        for book in self.books:
            if book['title'] == title:
                book['content'][Book.GetCurrentPage()]

    def AddBook(self, title, content):
        self.books.append(Book(title, content).FormatBook())

    def RemoveBook(self, title):
        for book in self.books:
            if book['Title'] == title:
                self.books.remove(book)
                print("The Book has been successfully removed!")
        print("This book does not exist in your library.")
