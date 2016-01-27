#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
'''
Define authentication and other basic functions for Twitter interaction
'''
import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

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

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
