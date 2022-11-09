def chkNum(no1):
    no1=int(no1)
    if no1%2==0:
        return True
    else:
        return  False

def main():
    print("ENter No")
    no1=input()
    flag=chkNum(int(no1))
    if flag==True:
        print("No is Even")
    else:
        print("No is Odd")


if __name__=="__main__":
    main()