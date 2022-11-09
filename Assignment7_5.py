import threading

lock=threading.Lock()

def displayNormal():
    lock.acquire()
    for i in range(1,51):
        print(i)
    lock.release()

def displayReverse():
    lock.acquire()
    for i in range(50,0,-1):
        print(i)
    lock.release()


def main():
    print("______________________________________")
    thread1=threading.Thread(target=displayNormal)
    thread2=threading.Thread(target=displayReverse)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("_______________________________________")

if __name__=="__main__":
    main()

