"""
PROMPT: Create a reading software, like Kindle, that shows some content on each page, 
the user to move back and forth, add and remove books. 

Split the content in each page, including title at the top of each page, and the page number at the bottom.

------------------------------------------------------------------------
All my reasoning and logic behind this project can be found in the "sketch.pdf" file in this repository.
"""

from library import Library
from book import Book

# Testing 
first_book = Book("lorem ipsum", open("test.txt"))

# TESTING ALL ATTRIBUTES IN A BOOK 
# ALL TESTS PASSED - WORKING JUST FINE
# print(first_book.GetNumberOfPages())
# print(first_book.GetTitle())
# print(first_book.DisplayPage())
# print(first_book.FormatBook())
# print(first_book.GetContent())
# print(first_book.GetCurrentPage())
# print(first_book.Forward())
# print(first_book.Forward())
# print(first_book.Rewind())
# print(first_book.GetPercentageRead())

# while first_book.GetNumberOfPages() > first_book.GetCurrentPage()+1:
    # first_book.Forward()
# while first_book.GetCurrentPage() > 0:
    # first_book.Rewind()
# ----------------------------------------------------------------
# TESTING LIBRARY
# ALL TESTS PASSED - WORKING JUST FINE
my_library = Library()
# Downloading books in the Library
my_library.AddBook("Book1", open("The Story of Lore Ipsum.txt"))
my_library.AddBook("Book2", open("The enigmatic Key.txt"))
# Displaying downloaded books
print(my_library.books)

# Home function - Displaying books just fine
# my_library.Home()
# TRANSFER ALL BOOKS TO A FOLDER AND CHANGE DIRECTORY IN open().