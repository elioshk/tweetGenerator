import snscrape
import os
import json
import pandas as pd
from markovchain import JsonStorage
from markovchain.text import MarkovText, ReplyMode

def scrapeTweets(userName):
    os.system("snscrape --jsonl --max-results 500 twitter-search 'from:" + userName + "'> user-tweets.json")

def createSourceText():
    tweetlist = pd.read_json("user-tweets.json", lines=True)
    sourceText = open("sourceText.txt", "w")
    for tweet in tweetlist.content:
        sourceText.write(str(tweet.encode("ascii", "ignore")))

    
def generateTweet(userName):
    scrapeTweets(userName)
    createSourceText()
    markov = MarkovText()
    with open('sourceText.txt') as st:
        markov.data(st.read())
    return markov()
