#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
'''
Do basic stuff with Twitter data (e.g. prints followers, streams tweets)
'''
from tweepy_preload import *

api = authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# print 10 elements from homepage
print "First 10 Tweets\n"
for status in tweepy.Cursor(api.home_timeline).items(10):
    print status.text

# prints all followers
print "List of followers\n"
getFollowers()

# print "List of all Tweets\n"
getAllTweets()

# tracks keywords with Twitter streaming API
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#SDGs'])

if __main__ == "__main__":
