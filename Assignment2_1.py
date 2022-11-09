import Assignment2_Arithmatic

def main():
    print("ENter first No")
    no1=input()
    print("Eneter second no")
    no2=input()
    ret=Assignment2_Arithmatic.add(no1,no2)
    print("Addition is ",ret)
    ret = Assignment2_Arithmatic.substract(no1, no2)
    print("Substratcion is ", ret)
    ret = Assignment2_Arithmatic.Multiplication(no1, no2)
    print("Multiplication is ", ret)
    ret = Assignment2_Arithmatic.Division(no1, no2)
    print("Division is ", ret)


if __name__=="__main__":
    main()