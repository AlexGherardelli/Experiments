#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
'''
Search tweets
'''
from tweepy_preload import *

if __name__ == "__main__":
    api = authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    # streams tweets until told to (Ctrl + C)
    twitter_stream = Stream(auth, TwitterListener())
    try:
        twitter_stream.sample()
    except Exception as e:
        print(e.__doc__)
