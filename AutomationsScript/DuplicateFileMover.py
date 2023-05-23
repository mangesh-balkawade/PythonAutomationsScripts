import shutil
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sys import *
import os
import hashlib
import time
import datetime

import schedule

def EmailTask(file_name,starttime,noScanFile,dupFile):

    fromaddr = "Please Enter Sender Address"
    toaddr = sys.argv[3]

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Duplicate File Removal Information "

    # string to store the body of the mail
    body = "Scanned Start At Time  :" + str(starttime)+ "\n" + "Total No Of FileScan :" + str(noScanFile)+"\n"+ "NO Of duplicates files are :"+str(dupFile)+" The Files Which Are Duplicates are move to the Path D:\\Duplicates"

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
    s.login(fromaddr, "Enter Password Here")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

def Log_file_Creation(data,starttime,count,noofdupfile):
    seperator = "-" * 80
    log_path = os.path.join(os.getcwd(),
                            "MangeshLog%s.log" % (str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")))
    f = open(log_path, mode="w", encoding='utf-8')
    f.write(seperator + "\n")
    f.write("Mangesh Process Logger : " + time.ctime() + " \n")
    f.write(seperator + "\n")

    for i in data:
        f.write(i)
        f.write("\n")

    f.close()

    EmailTask(os.path.abspath(path=log_path),starttime,count,noofdupfile)

def hashfile(path, blocksize=1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()


def DeleteFiles(dict1,starttime,totalNoOfFiles):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    icnt = 0

    list_file=[]
    noofdupfile=0
    if len(results) > 0:

        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    list_file.append(subresult)
                    noofdupfile+=1
                    src_path=subresult
                    dest_path="D:\\Duplicate"
                    shutil.move(src_path,dest_path)
            icnt = 0
        Log_file_Creation(list_file,starttime,totalNoOfFiles,noofdupfile)
    else:
        print("No duplicate files found.")


def findDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)
    dups = {}
    totalNoOfFiles=0
    if exists:

        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                totalNoOfFiles+=1
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups,totalNoOfFiles
    else:
        print("Invalid Path")


def Task():
    arr = {}
    startTime = datetime.datetime.now()
    arr,totalNoOfFiles = findDup(argv[1])
    DeleteFiles(arr, startTime,totalNoOfFiles)


def main():
    print("-- Mangesh Balkawade Automation-----")

    print("Application name: " + argv[0])

    if (len(argv) != 4):
        print("Error: Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and delete duplicate files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage: Application Name AbsolutePath_of_Directory Extention")
        exit()

    try:
        schedule.every(int(sys.argv[2])).minutes.do(Task)
        while True:
            schedule.run_pending()
            time.sleep(60)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)


if __name__ == "__main__":
    main()
