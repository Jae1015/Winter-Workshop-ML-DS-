import tweepy
import json

# Consumer keys and access tokens, used for OAuth
access_token="#"
access_secret="##"
consumer_key="##"
consumer_secret="##"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

data=[]
for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items(2):
    data.append(status._json)
print(data)

#storing tweets to a json file
with open('user_tweets.json', 'w') as outfile:  
   json.dump(data, outfile)
 
with open('user_tweets.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print
