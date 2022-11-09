from functools import reduce

def chkPrime(no):
    if no==1 or no==2:
        return  True

    flag=True
    for i in range(2,int((no/2)+1)):
        if no%i==0:
            flag=False
            break

    return flag

def MaxX(no1,no2):
    if no1>no2:
        return no1
    return no2

def main():
    list1=[]
    print("Enter How Many elements you want")
    size=int(input())
    print("Enter No ")
    for i in range(0,size):
        list1.append(int(input()))

    mapList=list( map(lambda element:element*2,list( filter(chkPrime,list1))))

    output=reduce(MaxX,mapList)
    print(output)

if __name__=="__main__":
    main()

