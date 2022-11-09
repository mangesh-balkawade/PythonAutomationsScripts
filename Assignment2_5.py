def chkPrime(no):
    no=int(no)
    if no==1 or no==2:
        return True

    flag=True
    for i in range(2,int((no/2))+1):
        if (int(no%i)) == 0:
            flag=False
            break

    return  flag


def main():
    print("ENter  No")
    no1=input()
    flag=chkPrime(no1)
    if flag==True:
        print("No is prime")
    else:
        print("No is not prime")


if __name__=="__main__":
    main()