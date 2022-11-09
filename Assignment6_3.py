class Numbers:

    def __init__(self):
        self.value=0
        self.accept()

    def accept(self):
        print("Enter Number ")
        self.value=int(input())

    def checkPrime(self):
        if(self.value%2==0):
            return False
        i=0
        for i in range(int(self.value/2),1,-1):
            if(self.value%i==0):
                break

        if i==2:
            return True

    def sumOfFactors(self):
        sum=0
        for i in range(1,int(self.value/2)+1):
            if self.value%i==0:
                sum+=i

        return sum

    def displayFactors(self):
        for i in range(1,int(self.value/2)+1):
            if self.value%i==0:
                print(i)

    def checkPerfect(self):
        if self.value==self.sumOfFactors():
            return True
        else:
            return False


def main():
    print("Welcome To Number Application")
    print("_____________________________")
    obj1=Numbers()
    ret=obj1.checkPrime()
    if(ret==True):
        print("Numbers is Prime")
    else:
        print("Number is not Prime")
    print("_____________________________")
    ret=obj1.sumOfFactors()
    print("Sum OF factors are ",ret)
    print("_____________________________")
    print("Factors of no is ")
    obj1.displayFactors()
    print("_____________________________")
    ret = obj1.checkPerfect()
    if (ret == True):
        print("Numbers is Perfect")
    else:
        print("Number is not Perfect")


if __name__=="__main__":
    main()
