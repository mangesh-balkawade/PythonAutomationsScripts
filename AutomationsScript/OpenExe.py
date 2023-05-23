import os.path
import subprocess
import time
import schedule
import  sys

def openExe():
    path = "C:\Program Fiysimport timeles\Sublime Text 3\sublime_text.exe"
    subprocess.Popen([r"%s" % path])

def Task():
    openExe()

def main():
    print("----------- Mangesh Balkawade Automations -----------")

    print("Automation script started with name : ",sys.argv[0])


    try:
        schedule.every().tuesday.at("17:45").do(Task)

        while True:
            schedule.run_pending()
            time.sleep(0)


    except ValueError:
        print("Error : Invalid Data Type Input")

    except Exception:
        print("Error :invalid input ")


if __name__ == "__main__":
    main()