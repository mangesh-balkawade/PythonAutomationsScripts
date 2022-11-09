def displayFirstEven(no):
    no=int(no)
    icnt=2
    for i in range(1,no+1):
        print(icnt)
        icnt+=2

def main():
    print("Enter Number")
    no=input()
    displayFirstEven(no)

if __name__=="__main__":
    main()