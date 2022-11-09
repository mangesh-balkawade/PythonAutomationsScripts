class Demo:
    Value=0
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2

    def setters(self,no1,no2):
        self.no1=no1
        self.no2=no2

    def getters(self):
        print("Value of no1 is ",self.no1)
        print("Value of no2 is ",self.no2)


def main():
    print("Enter First Value")
    value1=int(input())
    print("Enter Second Value")
    value2=int(input())

    dobj1 = Demo(value1,value2)
    dobj1.getters()

    print("Enter First Value")
    value1 = int(input())
    print("Enter Second Value")
    value2 = int(input())

    dobj2 = Demo(value1, value2)
    dobj2.getters()

if __name__=="__main__":
    main()


