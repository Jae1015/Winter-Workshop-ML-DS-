import tweepy
from tweepy import OAuthHandler
try:
 import json
except ImportError:
 import simplejson as json

from nltk.tokenize import word_tokenize

#User Credentials
access_token="#"
access_secret="##"
consumer_key="##"
consumer_secret="##"

oauth = OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)

api=tweepy.API(oauth)

#home_user timeline
#limit can be skipped in the brackets

for status in tweepy.Cursor(api.home_timeline).items(1):
 print(status.text)

#as a json object
print("as json object")
for status in tweepy.Cursor(api.home_timeline).items(1):
 print(status._json)
#process a single status
#print(status.text)
print "followers"
#home_user friends
for friend in tweepy.Cursor(api.friends).items(1):
    print(friend)

print("list of one's tweets")
for tweet in tweepy.Cursor(api.user_timeline).items():
 print(tweet._json)
