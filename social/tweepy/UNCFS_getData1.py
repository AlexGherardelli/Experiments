#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
from UNCFS_preload import *

# print 10 elements from homepage
def getTweet(number):
    for status in tweepy.Cursor(api.home_timeline).items(number):
        return status.text

def getFollowers():
    for friend in tweepy.Cursor(api.friends).items():
        return process(friend._json)

def getAllTweets():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        return process(tweet._json)

print "First 10 Tweets\n"
tweet = getTweet(10)
print tweet

print "List of all Tweets\n"
all_tweet = getAllTweets
print all_tweet
\
print "List of followers\n"
followers = getFollowers()
print followers
