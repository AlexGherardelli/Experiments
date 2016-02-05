__author__ = "Alessandra Gherardelli"
__copyright__ = "Copyright 2015, Alessandra Gherardelli"
__license__ = "MIT License"
__version__ = "1.0"
__email__ = "alessandra.gherardelli@gmail.com"
__status__ = "Production"

'''
It returns a clean, ordered list of emails. Input: txt file; Output: txt file.
'''
#imports required modules
import os, re, csv,getpass

#sets user-defined directory as path
print "\t\t\t\tWELCOME TO EMAIL2TEXT!\n"
print "========================================================================\n"



print "This programme will find all emails contained in a txt file and convert them in a csv\n\n"

#get username & default working directory
user = getpass.getuser()
path = "C:/Users/" + user + "/Documents"

print "The default directory is ", path
print "\n"

while True:
    try:
        user_input = raw_input("Would you like to change the directory? Y/N\t")
        user_input = user_input.lower()
        if user_input == "n":
            os.chdir(path)
        elif user_input == "y":
            print "Please input the full path where the file is located(e.g. C:\Users\Myfolder)\n"
            path = raw_input("Directory:  ")
            try:
                os.chdir(path)
            except IOError:
                print "No such file or directory:", path
        else:
            print "Sorry, it look your answer is not valid\n"
            continue
        print "The new working directory is: " + path + "\n"
            
    except ValueError:
        print "Sorry, it look your answer is not valid\n"
        continue
    else:
        break


#gets input file name
print "Please the name of the input text file (txt) "
fhandle = raw_input("Input file name:  ")

#checks if user has put extension
if fhandle[-4:] != ".txt":
    fhandle += ".txt"
    

#opens input files and throws error if not found
try:
    input_file = open(fhandle)
except:
    print "ERROR! File not found"
    raise IOError

try:
    fout = open(str(fhandle) + "_output.txt", "wb")
except:
    print "ERROR! Could not create file"
    raise IOError
    

#initializes two empty lists
lst = list()
l = list()

#looks for emails in text file
for line in input_file:
    line = line.rstrip()
    emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(emails) > 0:
        for email in emails:
           lst.append(str(email).lower())

lst.sort()          

for item in lst:
    fout.write(str(item) + ';\n')
fout.close()


