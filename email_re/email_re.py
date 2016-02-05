#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe

import os
import re

os.chdir("C:\Users\GHERARDELLI\Documents\Scripts")
try:
    hand = open('email.txt')
except:
    print "Error!"

for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        for i in x:
            print str(i).lower()
