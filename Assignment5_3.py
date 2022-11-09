class Arithmatic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self,ino1,ino2):
        self.value1=ino1
        self.value2=ino2

    def addition(self):
        return self.value1+self.value2

    def substarction(self):
        return self.value1-self.value2

    def multiplication(self):
        return self.value1*self.value2

    def division(self):
        try:
            return self.value1/self.value2
        except:
            print("Second no should be greater than 0")


def main():
    print("Enter First No")
    ino1=int(input())
    print("Enter Second No")
    ino2=int(input())

    aobj1=Arithmatic()
    aobj1.accept(ino1,ino2)
    iret=aobj1.addition()
    print("Addition is ",iret)
    iret=aobj1.substarction()
    print("Substartcion is ",iret)
    iret=aobj1.multiplication()
    print("MUltiplication is",iret)
    iret=aobj1.division()
    print("Division is",iret)

if __name__=="__main__":
    main()


