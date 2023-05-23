from sys import *

import psutil


def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def main():
    print("----------- Mangesh Balkawade Automations -----------")

    print("Automation script started with name : ",argv[0])

    listprocess=ProcessDisplay()

    for element in listprocess:
        print(element)

if __name__ == "__main__":
    main()