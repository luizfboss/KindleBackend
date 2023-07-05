"""
-------------------------------------------------------------------------------------------------
PROMPT: Create a reading software, like Kindle. 
Some features must be included, such as:
 - allow the user to go to next/previous pages
 - add and remove books from the library
 - change current book. If the user is reading one book and they are not done but they want to read another book, save the progress of that current book dinamically, and switch the current book.

The content in each page must include: 
 - title, at the top of each page
 - text, in the middle of the page
 - the page number, at the bottom.
-------------------------------------------------------------------------------------------------
All my reasoning and logic behind this project can be found in the "sketch.pdf" file in this repository.
"""

from library import Library
from book import Book

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
# Displaying downloaded books
# print(my_library.books)

# Home function - Displaying books just fine
my_library.Home()

my_library.AddBook("The Story of Lore Ipsum", open("The Story of Lore Ipsum.txt"))

print(my_library.books[0].GetCurrentPage())

my_library.Home()

# Testing Select
my_library.Select("The Story of Lore Ipsum")


# TESTING CURRENT BOOK VARIABLE AND BOOK METHODS TOGETHER
# WORKING PERFECTLY FINE 
# print(my_library.current_book.FormatBook())
# print(my_library.current_book.GetTitle())
# print(my_library.current_book.GetContent())
# print(my_library.current_book.GetCurrentPage())
# print(my_library.current_book.GetNumberOfPages())
# print(my_library.current_book.GetPercentageRead())
# print(my_library.current_book.DisplayPage()

print(my_library.current_book.DisplayPage()) # Page 1
print(my_library.current_book.GetCurrentPage())
print(my_library.current_book.Forward()) # Page 2
print(my_library.current_book.Forward()) # Page 3
print(my_library.current_book.Rewind()) # Page 2

print(my_library.current_book.Forward()) # Page 3 
print(my_library.current_book.Forward()) # Page 4 
print(my_library.current_book.Forward()) # Page 5
print(my_library.current_book.Forward()) # Page 6
print(my_library.current_book.Forward()) # Page 7
print(my_library.current_book.Forward()) # Page 8
print(my_library.current_book.Forward()) # Page 9
print(my_library.current_book.Forward()) # Page 10

# print(my_library.current_book.GetCurrentPage())

my_library.Home()

my_library.Select("The Story of Lore Ipsum")
print(my_library.current_book.Forward()) # Page 11
print(my_library.current_book.Forward()) # Page 12
print(my_library.current_book.Forward()) # Page 13
print(my_library.current_book.Forward()) # Page 14

print(my_library.current_book.GetPercentageRead())
print(my_library.current_book.GetNumberOfPages())

my_library.Home()


my_library.AddBook("The Tides of Destiny", open("The Tides of Destiny.txt"))

my_library.Home()

my_library.Select("The Tides of Destiny")

my_library.current_book.DisplayPage()
my_library.current_book.Forward()
my_library.current_book.Forward()
my_library.current_book.Forward()
my_library.current_book.Forward()

my_library.Home()

my_library.Select("The Tides of Destiny")
my_library.current_book.DisplayPage()
my_library.current_book.Forward()
my_library.current_book.Forward()
my_library.current_book.Forward()
my_library.current_book.Forward()

my_library.Home()