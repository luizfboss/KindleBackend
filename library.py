from database import all_books
from book import Book

class Library(Book):
    def __init__(self):
        self.books = []
        self.current_book = None   

    def Home(self):
        # Display all books and percentage read
        # Template:
        # <BOOK NAME> - <PERCENTAGE READ>
        for book in self.books:
            print(f"{book['Title']} - {book['percentage_read']}%")

    def Select(self, title):
        for book in self.books:
            if book['title'] == title:
                book['content'][Book.GetCurrentPage()]

    def AddBook(self, title, content):
        self.books.append(Book(title, content))

    def RemoveBook(self, title):
        for book in self.books:
            if book['Title'] == title:
                self.books.remove(book)
                print("The Book has been successfully removed!")
        print("This book does not exist in your library.")


my_library = Library()

my_library.AddBook("elel", "fsdjvbnsfedvhfjdebgnvsdfklgjbnsdfgkldjgbnzlkjdxfnvbdlkjrfnasdlkujdnvlskjanal;uvbjnal;gvabjnka;lskgjnvasdf;gvbklfjanvbdfsl;vkasdnmvdsl;sdknvmkljsfgbnsadfilvujdfnvlakvjsdbnvlksdfjvbnsdflkvsdfnvlksdfjvnsdlkvsdjnvlsdfkjvnsdklvsdfjnvsdfkljvnsdflvksdjnvsdlkjdvnfkvjsdfnvlsdjkvnsd")