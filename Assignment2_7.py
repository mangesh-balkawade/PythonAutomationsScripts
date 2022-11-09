def pattern1(col):
    col=int(col)

    for i in range(1,col+1):
        for j in range(1,col+1):
            print(j,end="")
        print()


def main():
    print("ENter  No")
    no1=input()
    pattern1(no1)


if __name__=="__main__":
    main()