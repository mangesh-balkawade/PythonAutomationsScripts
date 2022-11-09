import MarvellousNum
import sys

def additionPrime(list1):
    list1=list(list1)
    isum=0
    for i in list1:
        flag=MarvellousNum.chkPrime(i)
        if flag==True:
            isum+=i

    return  isum


def main():

    print("How many elements you want to store")
    isize=int(input())
    list1=[]
    print("Enter elements")
    for i in range(1,isize+1):
        list1.append(int(input()))

    iret=MarvellousNum.ListAddition(list1)
    print("Addition of numbers are :",iret)

    iret=MarvellousNum.ListMax(list1)
    print("Maximun no from list is :",iret)

    iret=MarvellousNum.ListMin(list1)
    print("Minimum number from list is :",iret)

    iret=MarvellousNum.FreqNumberList(list1,5)
    print("Numbers of elemenst in the list is: ",iret)

    iret=additionPrime(list1)
    print("Addition of prime numbers in list are :",iret)


if __name__=="__main__":
    main()