def pattern1(no):
    no=int(no)

    for i in range(1,no+1):
        for j in range(1,no+1):
            print("*",end="")
        print()

def main():
    print("ENter  No")
    no1=input()
    pattern1(no1)


if __name__=="__main__":
    main()