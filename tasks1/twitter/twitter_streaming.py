try:
 import json
except ImportError:
 import simplejson as json

#Importing methods from twitter package
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

#User Credentials
access_token="#"
access_secret="##"
consumer_key="##"
consumer_secret="##"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

#Initiating the connection with twitter streaming API
twitter_stream = TwitterStream(auth=oauth)

#getting a sample of public data flowing through twitter
iterator = twitter_stream.statuses.sample()
#limiting number of tweets to 1000
#twitter API can collect data for days or even longer
tweet_count=1

for tweet in iterator :
 tweet_count -= 1
 #data is wrappped by twitter python tool as a as a TwitterDictResponse object.
 #and we convet it back into the JSON fromat to print
 print(json.dumps(tweet))
 
 if tweet_count <=0:
  break
