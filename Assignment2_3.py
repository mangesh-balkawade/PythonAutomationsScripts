def factorial(no):
    no=int(no)
    fact=1
    while no>0:
        fact*=no
        no=no-1

    return fact

def main():
    print("ENter  No")
    no1=input()
    ret=factorial(no1)
    print("Factorial is ",ret)

if __name__=="__main__":
    main()