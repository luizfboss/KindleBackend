from book import Book

class Library(Book): # CHECK IF INHERITANCE IS NECESSARY
    def __init__(self):
        self.books = []
        self.current_book = None

    def Select(self, title):
        try: 
            for book in self.books:
                if book['Title'] == title:
                    self.current_book = Book(book['Title'], open(f"{book['Title']}.txt"))
                    # Set values 
                    self.current_book.SetCurrentPage(book['Current_page'])
                    self.current_book.SetPecentageRead(book['Percentage_read'])
                    print("The book has been selected successfully!")
        except TypeError:
            print("Oops! That was no valid title. Try again.")

    def RewriteBook(self):
        pass


    def AddBook(self, title, content):
        self.books.append(Book(title, content).FormatBook())

    def RemoveBook(self, title):
        for book in self.books:
            if book['Title'] == title:
                self.books.remove(book)
                print("The Book has been successfully removed!")
        print("This book does not exist in your library.")

    def Home(self):
        print('=-'*20)
        print("\n")
        print("HOME PAGE")

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
                print(f"{book['Title']} - {book['Percentage_read']}%")
            print("\n")
            print('=-'*20) 