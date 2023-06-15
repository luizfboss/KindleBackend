from book import Book

class Library(Book): # CHECK IF INHERITANCE IS NECESSARY
    def __init__(self):
        self.books = []
        self.current_book = None

    def Select(self, title):
        try: 
            for book in self.books:
                if book.GetTitle() == title:
                    self.current_book = Book(book.GetTitle(), open(f"{book.GetTitle()}.txt"))
                    # Set values 
                    self.current_book.SetCurrentPage(book.GetCurrentPage())
                    self.current_book.SetPercentageRead(book.GetPercentageRead())
                    print("The book has been selected successfully!")
        except TypeError:
            print("Oops! That was no valid title. Try again.")

    def AddBook(self, title, content):
        self.books.append(Book(title, content))

    def RemoveBook(self, title):
        for book in self.books:
            if book.GetTitle() == title:
                self.books.remove(book)
                print("The Book has been successfully removed!")
        print("This book does not exist in your library.")

    def Home(self):
        print('=-'*20)
        print("\n")
        print("HOME PAGE")


        # Rewriting attributes in Library (array of objects) -> STILL NEEDS TESTING
        if self.current_book:
            for book in self.books:
                if self.current_book.GetTitle() == book.GetTitle():
                    book.SetPercentageRead(self.current_book.GetPercentageRead())
                    book.SetCurrentPage(self.current_book.GetCurrentPage())
                    self.current_book = None # Resetting current book for future use


        if len(self.books) == 0:
            print("Welcome!")
            print("\n")
            print("Your library is empty. Please add a book you would like to read.")
            print("\n")

        else:
            print("Welcome back!")
            print()
            # Display all books and percentage read
            # Template:
            # <BOOK NAME> - <PERCENTAGE READ>

            # Percentage read, current_page
            # if len(self.books) >= 1:
            #     for book in self.books:
            #         if book['Title'] == self.current_book.GetTitle():
            #             book['Percentage_read'] = self.current_book.GetPercentageRead()
            #             book['Current_page'] = self.current_book.GetCurrentPage()

            for book in self.books:
                print(f"{book.GetTitle()} - {book.GetPercentageRead()}%")
            print("\n")
            print('=-'*20) 