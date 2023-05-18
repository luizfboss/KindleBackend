"""
PROMPT: Create a reading software, like Kindle, that shows some content on each page, 
the user to move back and forth, add and remove books. 

Split the content in each page, including title at the top of each page, and the page number at the bottom.

------------------------------------------------------------------------
All my reasoning and logic behind this project can be found in the "sketch.pdf" file in this repository.
"""

from book import Book

# Testing 
first_book = Book("lorem ipsum", open("test.txt"))

# print(first_book.title)
# print(first_book.content)

print(first_book.GetNumberOfPages())

print(first_book.DisplayPage())

while first_book.number_of_pages > first_book.current_page+1:
    first_book.Forward()


while first_book.current_page > 0:
    first_book.Rewind()