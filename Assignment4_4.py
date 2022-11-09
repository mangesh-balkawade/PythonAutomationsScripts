from functools import reduce

def main():
    list1=[]
    print("Enter How Many elements you want")
    size=int(input())
    print("Enter No ")
    for i in range(0,size):
        list1.append(int(input()))

    sum= int( reduce(lambda element1,element2:element1+element2,
                (list(map(lambda element:element*element,
                          (list(filter(lambda element:element%2==0,list1))))))))

    print("Addition of numbers are ",sum)



if __name__=="__main__":
    main()

