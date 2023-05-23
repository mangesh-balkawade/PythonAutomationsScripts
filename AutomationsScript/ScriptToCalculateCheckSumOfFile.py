import hashlib
import os
import sys

def hashFile(path,blockSize=1024):
    hasher=hashlib.md5()
    files=open(path,"rb")
    buffer=files.read(blockSize)
    while len(buffer)>0:
        hasher.update(buffer)
        buffer=files.read(blockSize)

    return hasher.hexdigest()

def displayCheckSum(path):
    flag=os.path.abspath(path)
    if flag==False:
        path=os.path.abspath(path)

    extist=os.path.exists(path)

    if extist:
        dupdict = {}

        for (folder, subfolder, files) in os.walk(path):
            for file in files:
                path = os.path.join(folder + file)
                file_hash = hashFile(path)
                if file_hash in dupdict:
                    dupdict[file_hash].append(path)
                else:
                    dupdict[file_hash] = [path]
        return dupdict

    else:
        print("Invalid Path")



def main():
    print("---------------------------Mangesh Balkawade")

    if len(sys.argv)<2:
        print("Insufficient Argumenst")
        exit()

    if(sys.argv[1]=="-h"):
        print("This Scripts and delete all the duplicates Files in The "
              "Directory")
        exit()

    if(sys.argv[1]=='-u'):
        print("Usage : App_name Directory_Name")
        exit()

    try:
        arr=displayCheckSum(sys.argv[1])
        print(arr)

    except ValueError:
        print("Error : Invalid datatype of input ")
    except Exception as e:
        print("Error : INvalid Input ",e)


if __name__=="__main__":
    main()