#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
'''
Define authentication and other basic functions for Twitter interaction
'''
import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from UNCFS_config import *

def authentication(consumer_key, consumer_secret, access_token, access_secret):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def process(tweet):
    print json.dumps(tweet, indent = 2)

def getFollowers():
    for friend in tweepy.Cursor(api.friends).items():
        return process(friend._json)

def getAllTweets():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        return process(tweet._json)

class TwitterListener(StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        print(data["text"])
        return True
    def on_error(self, status):
        print status
