#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
'''
Define authentication and other basic functions for Twitter interaction
'''
import twitter, json, os

CONSUMER_KEY = "eygeDOFiZZ66ktbGwVfEMCpxs"
CONSUMER_SECRET = "4VuKManXWaqy9GpV7SHJXWND1xYa2DfmPAveQBPcbso0eMviXs"
ACCESS_TOKEN = "2308433827-p1KKGntTERQzYA9QNEy6Spaf2PYcgk7HBCFU7yG"
ACCESS_SECRET = "74RBgkvgv3Y7GRe1VbUbTlD6Hs0qY28QnMwbf1Kp2hHpm"

def t_auth(consumer_key, consumer_secret, access_token, access_secret):
    auth = twitter.oauth.OAuth(access_token, access_secret,
                               consumer_key, consumer_secret)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def process(tweet):
    print json.dumps(tweet, indent = 2)

t = t_auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
