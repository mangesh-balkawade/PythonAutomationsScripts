
import time
import sys
import psutil
import schedule

def KillProcess(process_name):
    process_name=str(process_name)
    for proc in psutil.process_iter():
        try:
            if proc.name().lower()==process_name.lower():
                proc.kill()
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


def TasK():
    KillProcess(sys.argv[1])


def main():
    print("----------- Mangesh Balkawade Automations -----------")

    print("Automation script started with name : ",sys.argv[0])

    if(len(sys.argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
        print("Help : This script is used to kill a particular process at a particular time")
        exit()

    if((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
        print("Usage : ApplicationName NameOfProcess")
        exit()

    try:
        schedule.every().day.at("12:00").do(TasK)

        while True:
            schedule.run_pending()
            time.sleep(60)


    except ValueError:
        print("Error : Invalid Data Type Input")

    except Exception:
        print("Error :invalid input ")


if __name__ == "__main__":
    main()