'''
twitter bot, uses tweepy to interact with the twitter dev API
Requires a twitter dev account.
Current Simple Functions Favourite the latest given # of tweets,
passed to the command line.
Params are subject, number of tweets
'''

import tweepy
import time
import sys

version = 0.1
auth = tweepy.OAuthHandler('nm',
                           'nm')
auth.set_access_token(
    'nm',
    'nm')

api = tweepy.API(auth)
user = api.me()
search_string = sys.argv[1]
numberOfTweets = sys.argv[2]


# Handle Rate Limiting
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


for tweet in tweepy.Cursor(api.search, search_string).items(int(numberOfTweets)):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# generous autofollow bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     # print(follower.name)
#     if follower.name == 'tbd':
#         follower.follow()
#         break
