import threading

def countCapital(str1):
    str1=str(str1)
    count=0
    for i in range(0, len(str1)):
        if(str1[i].isupper()):
            count=count+1

    print("Count Of Capital Letters From String is ",count)
    print("Id Of Thread is ", threading.get_ident())
    print("Name Of Thread Is ", threading.current_thread())


def countSmall(str1):
    str1 = str(str1)
    count=0
    for i in range(0, len(str1)):
        if(str1[i].islower()):
            count=count+1

    print("Count Of SmallLetters From String is ",count)
    print("Id Of Thread is ", threading.get_ident())
    print("Name Of Thread Is ", threading.current_thread())

def countDigit(str1):
    str1 = str(str1)
    count=0
    for i in range(0, len(str1)):
        if(str1[i].isdigit()):
            count=count+1

    print("Count Of Digit From String is ",count)
    print("Id Of Thread is ", threading.get_ident())
    print("Name Of Thread Is ", threading.current_thread())

def main():
    print("________________________________________________________")
    print("Enter String")
    str1=input()
    small=threading.Thread(target=countSmall,args=(str1,))
    capital=threading.Thread(target=countCapital,args=(str1,))
    digit=threading.Thread(target=countDigit,args=(str1,))

    small.start()
    capital.start()
    digit.start()

    capital.join()
    small.join()
    digit.join()

    print("____________________________________________________________")

if __name__=="__main__":
    main()
