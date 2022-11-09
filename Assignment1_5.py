def displayNoBetween(no1,no2):
    no1=int(no1)
    no2=int(no2)
    for i in range(no1,no2-1,-1):
        print(i)


def main():
    print("Enter starting  no")
    no1=input()
    print("Enter ending no")
    no2=input()
    displayNoBetween(no1,no2)

if __name__=="__main__":
    main()