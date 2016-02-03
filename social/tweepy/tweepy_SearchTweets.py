#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
# -*- coding: UTF-8 -*-
'''
Search tweets
'''
from tweepy_preload import *

if __name__ == "__main__":
    api = authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    # Search keyword in tweets
    keyword = u'foodsecurity'
    search_results = tweepy.Cursor(api.search, q = keyword).items(10)
    print "LAST TWEETS WITH %S QUERY" % keyword
    print "+++++++++++++++++++\n"
    for result in search_results:
        print unicode(result.text).encode('utf-8')

    # Returns trends
    trends = api.trends_place(1) #1 is worldwide
    print "\n\nWORLD TRENDS\n"
    print "+++++++++++++++++++\n"
    for trend in trends[0]['trends']:
        print unicode(trend['name']).encode('utf-8')
