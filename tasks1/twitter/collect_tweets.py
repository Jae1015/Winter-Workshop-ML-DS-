import twitter
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
t1= Twitter(auth=oauth)

#printing my timeline
my_timeline=t1.statuses.home_timeline()
#print(my_timeline)
print("limited tweets")
#printing some limited tweets
my_timeline=t1.statuses.home_timeline(count=1)
#print(my_timeline)

#printing someone else's timeline
t2=Twitter(auth=oauth)
x_timeline=t2.statuses.user_timeline(screen_name="SrBachchan",count=1)
print(x_timeline)



