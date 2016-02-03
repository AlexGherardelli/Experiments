#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

'''
UNCFS OAuth Data
'''
CONSUMER_KEY = "eygeDOFiZZ66ktbGwVfEMCpxs"
CONSUMER_SECRET = "4VuKManXWaqy9GpV7SHJXWND1xYa2DfmPAveQBPcbso0eMviXs"
ACCESS_TOKEN = "2308433827-p1KKGntTERQzYA9QNEy6Spaf2PYcgk7HBCFU7yG"
ACCESS_SECRET = "74RBgkvgv3Y7GRe1VbUbTlD6Hs0qY28QnMwbf1Kp2hHpm"

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
