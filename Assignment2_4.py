def additionOfFactors(no):
    no=int(no)
    isum=0
    end=int((no/2)+1)
    for i in range(1,end):
        if (int(no%i))==0:
            isum+=i

    return  isum

def main():
    print("ENter  No")
    no1=input()
    ret=additionOfFactors(no1)
    print("Addition of fatcors is ",ret)

if __name__=="__main__":
    main()