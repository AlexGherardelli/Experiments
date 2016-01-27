'''
Downloads a file from a website and writes into a text file
'''

import os, requests

os.chdir('C:/Users/GHERARDELLI/Documents/Scripts/')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
play = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    play.write(chunk)
    
