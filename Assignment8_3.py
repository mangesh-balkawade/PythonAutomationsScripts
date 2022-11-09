def displayPattern(no):
    if(no>0):
        print(no, end="  ")
        displayPattern(no - 1)


def main():
    print("Enter How Many Times You Want To Print")
    no=int(input())
    displayPattern(no)

if __name__=="__main__":
    main()
