import datetime
import smtplib
import time
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psutil
import os
import schedule


def EmailTask(file_name):
    print("Email Sending is on going")
    print(file_name)

    fromaddr = "mangeshbalkawade07@gmail.com"
    toaddr = "ambardhanave00@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Process Information "

    # string to store the body of the mail
    body = "Current Running Process On The System Information  " + time.ctime()

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent

    attachment = open(file_name, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "sidr vsia wcfr tldm")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


def ProcessDisplay(log_dir = "Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-"*80
    log_path =os.path.join(log_dir,"MarvellousLog%s.log"%(str(datetime.datetime.now()).replace(" ","-").replace(":","-")))
    f = open(log_path, mode="w", encoding='utf-8')
    f.write(seperator+"\n")
    f.write("Marvellous Infosystem Process Logger : "+time.ctime()+" \n")
    f.write(seperator+"\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    EmailTask(os.path.abspath(path=log_path))

def TasK():
    ProcessDisplay(sys.argv[1])


def main():
    print("----------- Mangesh Balkawade Automations -----------")

    print("Automation script started with name : ",sys.argv[0])

    if(len(sys.argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
        print("Help : This script is used to log record of running processes")
        exit()

    if((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
        print("Usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        schedule.every(10).seconds.do(TasK)

        while True:
            schedule.run_pending()
            time.sleep(0)


    except ValueError:
        print("Error : Invalid Data Type Input")

    except Exception:
        print("Error :invalid input ")


if __name__ == "__main__":
    main()