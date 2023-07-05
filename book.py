class Book:
  def __init__(self, title, content):
      self.__title = title
      self.__book_file = content.read().strip()
      self.__content = [self.__book_file[i:i+200].strip() for i in range(0, len(self.__book_file), 200)]
      self.__number_of_pages = len(self.__content)
      self.__current_page = 1
      self.__percentage_read = 0


  # Getter Functions
  def GetTitle(self):
    return self.__title
  
  def GetContent(self):
    return self.__content
  
  def GetCurrentPage(self):
    return self.__current_page
  
  def GetNumberOfPages(self):
    return self.__number_of_pages
  
  def GetPercentageRead(self):
    # Setting initial percentage read to 0%.
    if self.GetCurrentPage() <= 1:
      return 0 
    else: 
      return int((self.GetCurrentPage() / self.GetNumberOfPages()) * 100)
  
  def DisplayPage(self):
      print("\n")
      print(self.GetTitle())
      print(self.__content[self.GetCurrentPage() - 1])
      print(self.GetCurrentPage())
      return ""


  # Setters
  def SetPercentageRead(self, new_percentage): 
    self.__percentage_read = new_percentage

  # This works with both Rewind and Forward functions 
  def SetCurrentPage(self, action):
    if action == "+":
      self.__current_page += 1
    elif action == "-":
      self.__current_page -= 1
    else:
      self.__current_page = action

  def Forward(self):
    if self.GetCurrentPage() == self.__number_of_pages - 1:
      print("THE END! You've reached the last page of the book!")
    else:
      self.SetCurrentPage("+")
      self.DisplayPage()
    return ""

  def Rewind(self):
    if self.GetCurrentPage() == 0:
      print("You've already reached the first page.")
    else:
      self.SetCurrentPage("-")
      self.DisplayPage()
    return ""


  # The following function was created for testing purposes only. Please ignore it.
  # def FormatBook(self):
  #   return {
  #     "Title": self.GetTitle(),
  #     "Content": self.GetContent(),
  #     "Number_of_pages": self.GetNumberOfPages(),
  #     "Current_page": self.GetCurrentPage(),
  #     "Percentage_read": self.GetPercentageRead()
  #   }
