import threading

def displayEven():
    for i in range(2,11,2):
        print("Even Number ",i)

def displayOdd():
    for i in range(1,11,2):
        print("Odd Number ",i)


def main():
    print("Welcome To Multithreading Application ")
    even=threading.Thread(target=displayEven,args=())
    odd = threading.Thread(target=displayOdd, args=())
    even.start()
    odd.start()

if __name__=="__main__":
    main()