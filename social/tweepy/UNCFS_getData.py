#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
'''
Do basic stuff with Twitter data (e.g. prints followers, streams tweets)
'''
from UNCFS_preload import *

api = authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# print 10 elements from homepage
print "First 10 Tweets\n"
for status in tweepy.Cursor(api.home_timeline).items(10):
    print status.text

# prints all followers
print "List of followers\n"
for friend in tweepy.Cursor(api.friends).items(10):
    print process(friend._json)

# print "List of all Tweets\n"
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     print process(tweet._json)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#SDGs'])
