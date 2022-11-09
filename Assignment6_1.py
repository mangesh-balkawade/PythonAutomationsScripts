class BookStore:
    noOfBooks=0

    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.noOfBooks+=1

    def display(self):
        print("The Name of Book is ",self.name)
        print("The Name of author is ",self.author)
        print("Total No of Books are ",BookStore.noOfBooks)


def main():
    print("Welcome to Book Store")
    print("___________________________________________")
    bobj1=BookStore("Linux System Programming ","Robert Love")
    bobj1.display()
    print("___________________________________________")
    bobj2=BookStore("C Programming ","The Dennis Ritchi")
    bobj2.display()

if __name__=="__main__":
    main()