import oauth2 as oauth
import json
from string import punctuation

CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_KEY = " "
ACCESS_SECRET = " "

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=BJP&geocode=21,78,998.5mi&lang=en&rpp=5"
response, data = client.request(endpoint)

output  = open('BJP.json', 'w')

data1 = json.loads(data)
output.write(json.dumps(data1))

tweets = data1['statuses']
for tweet in tweets:
	print tweet['text']
