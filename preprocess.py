import json
import MySQLdb as mdb
from string import punctuation
from geopy import geocoders
list_tweet = []
words = []
list_all_tweets = []
"""
Made the connection to the database implemented by the package MySQLdb
"""
con = mdb.connect('localhost', 'root', 'e', 'tweetdb')
#print con
"""
Opening the file BJP.json in read mode!
f is json object
python_data has same contents as f but its
a python data structure. 
"""
with open('BJP.json','r') as f:
    for line in f:
        python_data = json.loads(line)

'''
To implement stopwords :
with open('stopwords.txt','r') as f1:
    for words in stopwords:
'''
           
pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
print positive_words[:10]
positive_counter = 0
neg_sent = open("negative.txt").read()
negative_words=neg_sent.split('\n')
print negative_words[:10]
negative_counter = 0
def latlong(location):
    g = geocoders.GoogleV3()
    place, (lat, lng) = g.geocode(location)
    return lat,lng

def repair(string):
    string = string.lower()
    for p in list(punctuation):
        string = string.replace(p,'')    
    
    return string
    
for tweet in python_data['statuses']:
    print tweet["text"]
    
    
    print tweet["entities"]["hashtags"]
    originalTweet = tweet["text"]
    tweetLocation = tweet["user"]["location"]
    repairedTweet = repair(tweet["text"])
    link = "http://twitter.com/%s" % tweet["user"]["screen_name"]
    #print "\n \n"
    if("Hyderabad" or "hyderabad" in tweetLocation):
        tweetLocation = "Andhra Pradesh"
    else:
        pass    
    print tweetLocation
    lat, lng = latlong(tweetLocation)
    print lat,lng
    print link
    #print repairedTweet
    list_tweet.append(repairedTweet)
    words = repairedTweet.split(' ')
    print "\n"
    #print words
    print repairedTweet
    for word in words:
        if word in positive_words:
            positive_counter+=1
        elif word in negative_words:
            negative_counter+=1    
    p = float(positive_counter)/float(len(words))
    n = float(negative_counter)/float(len(words))
    
    if p>n:
        polarity = 1
    else: 
        polarity = 0
    
    polarity = str(polarity) 
    '''with con:
        cursor = con.cursor()
        #print "INSERT INTO `tweetdb`.`tweet1`(`LAT`,`LONGI`,`LINK`,`TWEET`,`POLARITY`) VALUES('1','2','"+link+"','"+originalTweet+"','"+polarity+"')"
        cursor.execute("INSERT INTO `tweetdb`.`tweet1`(`LAT`,`LONGI`,`LINK`,`TWEET`,`POLARITY`) VALUES('1','2','"+link+"','"+repairedTweet+"','"+polarity+"','"+tweetLocation+"')")
               
        cursor.close()
        print "Import to MySQL is over"   '''
        
                 
