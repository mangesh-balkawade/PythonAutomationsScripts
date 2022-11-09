def countdigit(no):
    no=int(no)
    icnt=0
    while no>0:
        icnt+=1
        no=int(no/10)

    return icnt
def main():
    print("ENter  No")
    no1=input()
    ret=countdigit(no1)
    print("No of Digits are ",ret)

if __name__=="__main__":
    main()