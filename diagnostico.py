import json
import re
 
def open_data():
    with open("archive/farmers-protest-tweets-2021-03-5.json") as archivo:
        next(archivo)
        yield from archivo

def retweetCount(tweet):
    if tweet == "a":
        return -1
    match_object = re.search(
    r'(?<=retweetCount)(.*)(?=likeCount)', tweet)
    num = re.search(
    r'\d+', match_object.group())
    return int(num.group())

def addtweet(most_retweeted, tweet):
    #print("Nuevo", tweet)
    #print(retweetCount(tweet))
    for i in range(10):
        if retweetCount(most_retweeted[i]) < retweetCount(tweet):
            for j in range(9, i):
                most_retweeted[j] = most_retweeted[j-1]
            most_retweeted[i] = tweet
            return(most_retweeted)
    
def topretweeted():
    data = open_data()
    most_retweeted = {i:"a" for i in range(10)}
    for twe in data:
        tweet = twe
        if retweetCount(most_retweeted[9]) < retweetCount(tweet):
            most_retweeted = addtweet(most_retweeted, tweet) 
            
    print("Most retweeted")
    for i in most_retweeted:
        print("-------------", i+1, "-------------")
        print("retweets:", retweetCount(most_retweeted[i]))
        print(most_retweeted[i])
        

topretweeted()

users = {}

def getUser(tweet):
    match_object = re.search(
    r'(?<=user)(.*)(?=likeCount)', tweet)
    num = re.search(
    r'\d+', match_object.group())
    return int(num.group())

def topusers():
    data = open_data()
    for twe in data:
        tweet = twe