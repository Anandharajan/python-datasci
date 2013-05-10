import sys
import json
import re


def main():
    sentiments_path = sys.argv[1]
    tweets_path = sys.argv[2]


    sentiments = {}

    for line in open(sentiments_path,'r').readlines():
        sentement = line.split("\t")
        sentiments[sentement[0]] = int(sentement[1])

    for line in open(tweets_path,'r').readlines():
        tweet = json.loads(line[:-1],encoding='utf-8')
        text = tweet['text'] if "text" in tweet.keys() else ""
        text = re.sub('[^A-Za-z0-9 ]+','',text).lower().split(" ")
        print calc_sentiment_score(text,sentiments)

def calc_sentiment_score(text,sentiments):
    score = 0
    for word in text:
        delta = sentiments[word.lower()] if word.lower() in sentiments.keys() else 0
        score += delta
    return score

if __name__ == '__main__':
    main()