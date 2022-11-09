def pattern(no):
    no=int(no)

    for i in range(1,no+1):
        print("* ",end="")

def main():
    print("Enter Number")
    no=input()
    pattern(no)

if __name__=="__main__":
    main()