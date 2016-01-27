#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
'''
Takes pages from webpage
Joins them all together
Remove trailing spaces/new lines on right
Converts them into markdown
'''
import requests, urllib, os
from bs4 import BeautifulSoup

os.chdir("C:/Users/GHERARDELLI/Documents/Scripts")

url = "http://www.jazzwisemagazine.com/pages/jazz-album-reviews/11585-the-100-jazz-albums-that-shook-the-world?showall="
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
filename = "book"


links = soup.find_all("a")
links = links[9:19]

lst = list()
for link in links:
    lst.append(link.get("href"))

for i in range(len(lst)):
    urllib.urlretrieve(lst[i], filename= filename + str(i) + ".txt")
