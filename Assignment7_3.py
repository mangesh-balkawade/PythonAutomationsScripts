import threading


def displayAddEven(data):
    isum=0
    data=list(data)
    for i in data:
        if(i%2==0):
            isum=isum+i

    print("The Addition of all the even element sfrom the list is ",isum)


def displayAddOdd(data):
    isum = 0
    data = list(data)
    for i in data:
        if (i % 2 != 0):
            isum = isum + i

    print("The Addition of all the odd element sfrom the list is ", isum)

def main():
    print("________________________________________________________")
    print("How Many Elements You Want")
    isize=int(input())
    data=[]
    print("Enter Elements")
    for i in range(0,isize):
        data.append(int(input()))

    evenlist=threading.Thread(target=displayAddEven,args=(data,))
    oddList=threading.Thread(target=displayAddOdd,args=(data,))

    evenlist.start()
    oddList.start()

    evenlist.join()
    oddList.join()

    print("____________________________________________________________")

if __name__=="__main__":
    main()
