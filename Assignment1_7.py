def divideBy5(no):
    no=int (no)
    if no%5==0:
        return True
    else:
        return  False

def main():
    print("Enter Number")
    no=input()
    flag=divideBy5(no)
    if flag==True:
        print("No is divide by 5")
    else:
        print("No is not divide by 5")

if __name__=="__main__":
    main()