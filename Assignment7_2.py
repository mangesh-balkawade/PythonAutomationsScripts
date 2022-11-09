import threading


def sumOfEvenFactor(no):
    evenFactorSum = 0
    for i in range(1,(int(no/2))+1,1):
        if((no%i==0) and (i%2==0)):
            evenFactorSum=evenFactorSum+i

    print("The Sum OF EVen Factors are ",evenFactorSum)

def sumOfOddFactor(no):
    oddFactorSum = 0
    for i in range(1,(int(no/2))+1,1):
        if ((no % i == 0) and (i % 2 != 0)):
            oddFactorSum=oddFactorSum+i

    print("The Sum OF Odd Factors are ", oddFactorSum)


def main():
    print("Welcome To Multithreading Application By Mangesh")
    print("___________________________________________________")
    print("Enter The No")
    no=int(input())
    evenFactor=threading.Thread(target=sumOfEvenFactor,args=(no,))
    oddFactor = threading.Thread(target=sumOfOddFactor, args=(no,))
    evenFactor.start()
    oddFactor.start()
    evenFactor.join()
    oddFactor.join()
    print("Exit From Main")
    print("___________________________________________________")

if __name__=="__main__":
    main()