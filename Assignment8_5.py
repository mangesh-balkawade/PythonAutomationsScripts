def factorial(no):
    if(no<=0):
        return 1
    else:
        return (no*(factorial(no-1)))


def main():
    print("Enter No")
    no=int(input())
    ret=factorial(no)
    print("The factorial of no is  ",ret)

if __name__=="__main__":
    main()
