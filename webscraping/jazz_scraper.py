import requests, os, urllib
from bs4 import BeautifulSoup

os.chdir("C:/Users/GHERARDELLI/Documents/Scripts")

url = "http://gnosis.cx/TPiP/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
filename = "jazz"