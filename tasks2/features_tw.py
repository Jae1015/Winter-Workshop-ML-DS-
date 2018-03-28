import tweepy
import json
import csv
from textblob import TextBlob
from datetime import datetime
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

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
twitter_handle="@SrBachchan"

with open(twitter_handle + '.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["length","no_hashtags","no_men", "likes", "retweets", "sentiment_polarity", "time"])
    for tweet in tweepy.Cursor(api.user_timeline, id=twitter_handle, q='to%3ANASA&tweet_mode=extended').items(100): 
        str = (tweet.text.encode("utf-8"))
        if(str[0:2]=="RT"):
            print ("Retweet")
        else:

            an = TextBlob(str)

            a = len(str)
            b = len(tweet._json['entities']['hashtags'])
            c = len(tweet._json['entities']['user_mentions'])
            d = tweet._json['favorite_count']
            e = tweet._json['retweet_count']
            f = an.sentiment.polarity
            created_at = tweet._json['created_at'][0:19]
            g = datetime.strptime(created_at,'%a %b %d %H:%M:%S').strftime('%H')
            outtweets = [a,b,c,d,e,f,g]
        writer.writerow(outtweets)
