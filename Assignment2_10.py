def sumdigit(no):
    no=int(no)
    isum=0
    while no>0:
        isum=isum+(int(no%10))
        no=int(no/10)
    return isum

def main():
    print("ENter  No")
    no1=input()
    ret=sumdigit(no1)
    print("Sum of Digits are ",ret)

if __name__=="__main__":
    main()