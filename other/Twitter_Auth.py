'''
Uses twitter API to retrieve trending topics
'''

import twitter

CONSUMER_KEY = "4wirPXOAaww7zpDhzdmTxAKBV"
CONSUMER_SECRET = "fxrwZAZkLBR2i12Q6E07ANuoPPSVKR1qmxS4PLFSxjF8sC1s1y"
OAUTH_TOKEN = "2548240448-fpjc3L88R3m9QVF6pjnyTAZbqWPSPy371G7uO4Y"
OAUTH_TOKEN_SECRET = "8xklSSsc2UlrvPCdx1gAwqSxLWgry9exVHs9XJwSnMH0W"


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth = auth)

