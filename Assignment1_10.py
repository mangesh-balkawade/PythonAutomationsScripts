def length(str1):
    str1=str(str1)
    return len(str1)

def main():
    print("Enter STring")
    str1=input()
    ret=length(str1)
    print("length of string is ",ret)
if __name__=="__main__":
    main()