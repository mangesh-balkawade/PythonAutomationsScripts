class BankAccount:
    RateOfInterest=10.5

    def __init__(self):
        self.name=""
        self.ammount=0
        self.accept()

    def accept(self):
        print("Enter Your Name")
        self.name=input()
        print("Enter The Amount")
        self.ammount=int(input())

    def display(self):
        print("Welcome to the banking appplication ")
        print("_____________________________________")
        print("Your Name is ",self.name)
        print("Your Amount is ",self.ammount)
        print("Standers Rate of interest is ",BankAccount.RateOfInterest)
        print("_____________________________________")

    def withdraw(self):
        print("Enter The Amount You Want to Withdraw")
        cash=int(input())
        self.ammount=self.ammount-cash
        self.displayAmount()

    def displayAmount(self):
        print("_____________________________________")
        print("Your Amount After Transection is ",self.ammount)
        print("_____________________________________")

    def deposite(self):
        print("Enter the amount want to deposite")
        cash=int(input())
        self.ammount=self.ammount+cash
        self.displayAmount()

    def calulateInterest(self):
        print("Enter The Amount For Which You Have to CAlculate ROI")
        value=int(input())
        finalAmount=value+(value/100)*BankAccount.RateOfInterest
        print("Your Final Amount After Calculating the ROI is ",finalAmount)


def main():
    aobj=BankAccount()
    aobj.display()
    aobj.deposite()
    aobj.withdraw()
    aobj.calulateInterest()

if __name__==("__main__"):
    main()




