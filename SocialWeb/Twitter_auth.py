import os, twitter

CONSUMER_KEY = '4wirPXOAaww7zpDhzdmTxAKBV'
CONSUMER_SECRET = 'fxrwZAZkLBR2i12Q6E07ANuoPPSVKR1qmxS4PLFSxjF8sC1s1y'
OAUTH_TOKEN = '2548240448-ttxXZVxXUhZT2ftlWBG9BoF82m9l7Xl6pGhyeiF'
OAUTH_TOKEN_SECRET = 'rTM8Go8a5oaVjxLYPssy22ngHTlWbdtvFdZiTXtn3VBbT' 

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)


