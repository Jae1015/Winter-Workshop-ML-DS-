import tweepy
try:
 import json
except ImportError:
 import simplejson as json

from tweepy import OAuthHandler
#User Credentials
access_token="#"
access_secret="##"
consumer_key="##"
consumer_secret="##"

oauth = OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_secret)

api=tweepy.API(oauth)

for friend in tweepy.Cursor(api.friends).items():
 print(json.dumps(friend))
