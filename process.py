import json
from string import punctuation

class Process(object):
    
    
     
    def __init__(self):
        self.ListOfAllTweets = [{}] #Tweets will be stored in the form of dictionaries!
        
        
    def getTweets(self,filename):
        with open(filename,'r') as f:
            for line in f:
                self.python_data = json.loads(line)
                        
    def pos_words(self):
        pos_sent = open("positive.txt").read()
        positive_words=pos_sent.split('\n')
        self.positive_counter = 0
        return positive_words
        
    def neg_words(self):
        neg_sent = open("negative.txt").read()
        negative_words=neg_sent.split('\n')
        self.negative_counter = 0
        return negative_words
             
    def repair(self,string):
        string_l = string.lower()
        for p in list(punctuation):
            string_l = string_l.replace(p,'')    
        return string_l
        
    def format_tweets(self):
        
            
        for tweet in self.python_data["statuses"]:
            print tweet["text"]
            print tweet["entities"]["hashtags"]
            originalTweet = tweet["text"]
            tweetLocation = tweet["user"]["location"]
            repairedTweet = self.repair(tweet["text"])
            link = "http://twitter.com/%s" % tweet["user"]["screen_name"]
            print "\n \n"
            print tweetLocation
            print link
            print repairedTweet
           # list_tweet.append(repairedTweet)
            words = repairedTweet.split(' ')
            print "\n"
            print words
            print repairedTweet
            positive_words = self.pos_words()
            negative_words = self.neg_words()
            for word in words:
                if word in positive_words:
                    self.positive_counter+=1
                elif word in negative_words:
                    self.negative_counter+=1    
            self.p = float(self.positive_counter)/float(len(words))
            self.n = float(self.negative_counter)/float(len(words))
            print self.p
            print self.n
            
            
pro = Process()
pro.getTweets('BJP.json')
pro.format_tweets()
pro2 = Process()
pro2.getTweets('Congress.json')
pro2.format_tweets()                 
                                            
