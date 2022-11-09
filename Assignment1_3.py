def addition(ino1,ino2):
    ino1=int(ino1)
    ino2=int(ino2)
    return ino1+ino2

def main():
    print("Enter first no")
    no1=input()
    print("Enter Second NO no")
    no2=input()
    ret=addition(no1,no2)
    print("Addition of no is ",ret)

if __name__=="__main__":
    main()