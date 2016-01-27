__author__ = "Alessandra Gherardelli"
__copyright__ = "Copyright 2015, Alessandra Gherardelli"
__license__ = "MIT License"
__version__ = "1.0"
__email__ = "alessandra.gherardelli@gmail.com"
__status__ = "Production"

'''
Takes a text file as input, finds all emails contained in the file and
outputs a csv file with a clean mailing list
'''
#imports required modules
import os, re, csv,getpass

#sets user-defined directory as path
print "\t\t\t\tWELCOME TO EMAIL2CSV!\n"
print "========================================================================\n"



print "This programme will find all emails contained in a txt file and convert them in a csv\n\n"

#get username & default working directory
user = user = getpass.getuser()
path = path = "C:/Users/" + user + "/Documents"

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

'''
print "Press Enter if this is corret\n"
print "If you would like to change the default directory,",
print "Please input the full path where the file is located(e.g. C:\Users\Myfolder)\"

directory = raw_input("Directory:  ")
if not directory:
    os.chdir(path)
else: 
    directory = str(directory)
    os.chdir(directory)
    print "The new working directory is: ", directory
'''
#gets input file name
print "Please the name of the input text file (txt) "
fhandle = raw_input("Input file name:  ")

#checks if user has put extension
if fhandle[-4:] != ".txt":
    fhandle += ".txt"
    

#opens input files and throws error if not found
try:
    fhandle = open(fhandle)
except:
    print "ERROR! File not found"
    raise IOError
    

#initializes two empty lists
lst = list()
l = list()

#looks for emails in text file
for line in fhandle:
    line = line.rstrip()
    emails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(emails) > 0:
        for email in emails:
           lst.append(str(email).lower())

#creates a list of lists
for element in lst:
    l.append([element])

#user-defined output file
print "Please input the name of output file(csv)"
output = raw_input("Output file name: ")

#checks if user has put extension
if output[-4:] == ".csv":
    pass
else:
    output += ".csv"

#writes file as csv and throws error if not found
try:
    with open(output, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter = ',')
        for i in l:
            writer.writerow(i)
except:
    print "ERROR! File not found"
    raise IOError
        
#prints out in terminal full email list
print "\n\nFULL LIST"
print "================\n"
for element in lst:
    print element
print "\n\n"



                


