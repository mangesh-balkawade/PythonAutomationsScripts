def ListAddition(list1):
    list1=list(list1)
    isum=0
    for i in list1:
        isum+=i

    return  isum

def ListMax(list1):
    list1=list(list1)
    imax=list1[0]
    for i in list1:
        if imax<i:
            imax=i

    return  imax


def ListMin(list1):
    list1 = list(list1)
    imin = list1[0]
    for i in list1:
        if imin > i:
            imin = i

    return imin

def FreqNumberList(list1,ino):
    list1=list(list1)
    icnt=0
    for i in list1:
        if i==ino:
            icnt+=1

    return icnt

def chkPrime(ino):
    ino=int(ino)
    if(ino==1 or ino==2):
        return  True

    flag=True

    for i in range(2,(int(ino/2))+1):
        if ino%i==0:
            flag=False
            break

    return  flag



