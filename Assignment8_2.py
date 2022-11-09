def displayPattern(no):
    if(no>0):
        displayPattern(no-1)
        print(no, end="  ")


def main():
    print("Enter How Many Times You Want To Print")
    no=int(input())
    displayPattern(no)

if __name__=="__main__":
    main()
