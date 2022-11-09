def sumOfDigit(no):
    if(no<=0):
        return 0
    else:
        return ((no%10)+sumOfDigit(int(no/10)))


def main():
    print("Enter No")
    no=int(input())
    ret=sumOfDigit(no)
    print("The Sum Of Digit is ",ret)

if __name__=="__main__":
    main()
