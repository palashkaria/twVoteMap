import json
import MySQLdb as mdb
from string import punctuation
list_tweet = []
words = []
list_all_tweets = []
con = mdb.connect('localhost', 'root', 'e', 'tweet_db')
print con
with open('BJP.json','r') as f:
    for line in f:
        python_data = json.loads(line)

'''with open('stopwords.txt','r') as f1:
    for words in stopwords:'''
           
pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
print positive_words[:10]
positive_counter = 0
neg_sent = open("negative.txt").read()
negative_words=neg_sent.split('\n')
print negative_words[:10]
negative_counter = 0


def repair(string):
    string = string.lower()
    for p in list(punctuation):
        string = string.replace(p,'')    
    
    return string
    
for tweet in python_data['statuses']:
    print tweet["text"]
    originalTweet = tweet["text"]
    tweetLocation = tweet["user"]["location"]
    repairedTweet = repair(tweet["text"])
    link = "http://twitter.com/%s" % tweet["user"]["screen_name"]
    #print "\n \n"
    print tweetLocation
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
    with con:
        cursor = con.cursor()
        #print "INSERT INTO `tweetdb`.`tweet1`(`LAT`,`LONGI`,`LINK`,`TWEET`,`POLARITY`) VALUES('1','2','"+link+"','"+originalTweet+"','"+polarity+"')"
        cursor.execute("INSERT INTO `tweetdb`.`tweet1`(`LAT`,`LONGI`,`LINK`,`TWEET`,`POLARITY`) VALUES('1','2','"+link+"','"+repairedTweet+"','"+polarity+"','"+tweetLocation+"')")
        '''cursor.execute('INSERT INTO tweet1(`LAT`,`LONGI`,) VALUES(1)')
        cursor.execute('INSERT INTO tweet1(`LONGI`) VALUES(2)')
        cursor.execute('INSERT INTO tweet1(`LINK`) VALUES(`'+link+'`)')
        cursor.execute('INSERT INTO tweet1(`TWEET`) VALUES(`'+originalTweet+'`)')
        cursor.execute('INSERT INTO tweet1(`POLARITY`) VALUES(`'+polarity+'`)')'''
          
        cursor.close()
        print "Import to MySQL is over"            
