
#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe python

import os, re, getpass

def get_path():
    user = getpass.getuser()
    path = "C:/Users/" + user + "/Documents"
    return path


def get_emails(infile):
    lst = list()
    for line in infile:
        line = line.rstrip()
        emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
        if len(emails) > 0:
        for email in emails:
           lst.append(str(email).lower())
    return lst







#path = get_path()
#print "The default path is ", str(path)

#try:
#   infile = open("sample.txt")
#except:
#   raise IOError
