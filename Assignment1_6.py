def chkNumber(no):
    no=int(no)
    if no>0:
        print("No is POsitive")
    elif no<0:
        print("NO is negative")
    else:
        print("NO is Zero")

def main():
    print("Enter Number")
    no=input()
    chkNumber(no)

if __name__=="__main__":
    main()
