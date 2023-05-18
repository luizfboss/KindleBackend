class Book:
  def __init__(self, title, content):
      self.title = title
      self.book_file = content.read().strip()
      self.content = [self.book_file[i:i+200].strip() for i in range(0, len(self.book_file), 200)]
      self.number_of_pages = len(self.content)
      self.current_page = 0

  
  def GetTitle(self):
    return self.title
  
  def GetContent(self):
    return self.content
  
  def GetCurrentPage(self):
    return self.current_page
  
  def GetNumberOfPages(self):
    return self.number_of_pages
  
  def DisplayPage(self):
      print("\n")
      print(self.GetTitle())
      print(self.content[self.current_page])
      print(self.GetCurrentPage() + 1)
      return ""


  def Forward(self):
    if self.current_page == self.number_of_pages - 1:
      print("THE END! You've reached the last page of the book!")
    else:
      self.current_page += 1
      self.DisplayPage()

  def Rewind(self):
    if self.current_page == 0:
      print("You've already reached the first page.")
    else:
      self.current_page -= 1
      self.DisplayPage()