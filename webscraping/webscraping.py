import requests, bs4, os

os.chdir('C:/Users/Gherardelli/Documents/Scripts/automation')

# sets up website to parse
res = requests.get('https://www.nostarch.com/arduino')
res.raise_for_status()
# set BeautifulSoup object
w = bs4.BeautifulSoup(res.text, "lxml")
t = w.select('.product-body')
