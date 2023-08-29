class Library:
    def __init__(self,ListOfBook):
        self.books=ListOfBook

    def displayAvailablebooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print("\t " +book)

    def borrowBooks(self,booksName):
        if booksName in self.books:
            print(f"you have been issued {booksName}.Please keep it and return it within 30 days")
            self.books.remove(booksName)
            return True
        else:
            print("sorry this books is already taken")
            return False
    
    def returnBook(self,booksName):
        self.books.append(booksName)
        print("thanks for return this books,havw a nice day")


class Students:
    def reqBook(self):
        self.book=input(" enter the name of the book you want to  borrow: ")
        return self.book
    def returnBook(self):
        self.book=input("enter the book you have to return: ")
        return self.book

if __name__=="__main__":
    centreLibrary=Library(["1-Algorithm","2-C","3-Python","4-JAVA","5-Django","6-DBMS"])
    student=Students()
    #centreLibrary.displayAvailablebooks()
    while(True):
        WelcomeMSG ='''*** Welcome the Cetral library ***
        Please choose an option:
        1.Listing all the books 
        2.Request a book
        3.Return a book 
        4.exit the library
        '''
    a=int(input("enter the choose: "))
    if a ==1:
        centreLibrary.displayAvailablebooks()
    elif a ==2:
        centreLibrary.borrowBooks()
    elif a ==3:
        centreLibrary.returnBook()
    elif a==4:
        print("thanks for using library")
        exit()
    else:
        print("invalid chocie")
print(WelcomeMSG)
