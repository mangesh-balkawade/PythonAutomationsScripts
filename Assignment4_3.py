from functools import reduce

def main():
    list1=[]
    print("Enter How Many elements you want")
    size=int(input())
    print("Enter No ")
    for i in range(0,size):
        list1.append(int(input()))

    filterList= list(filter(lambda element:(element>=70) and (element<=90),list1))
    print(filterList)

    mapList=list( map(lambda element:element+10,filterList))
    print(mapList)

    product=int( reduce(lambda element1,element2:element1*element2,mapList))
    print(product)



if __name__=="__main__":
    main()

