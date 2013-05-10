import sys
import json
import re


def main():
    sentiments_path = sys.argv[1]
    tweets_path = sys.argv[2]

    tweets = open(tweets_path,'r')
    sentiments = dict()

    for line in open(sentiments_path,'r').readlines():
        sentement = line.split("\t")
        try:
            sentiments[sentement[0]] = int(sentement[1])
        except ValueError:
            sentiments[sentement[0]] = 0

    for line in tweets.readlines():
        tweet = json.loads(line[:-1],encoding='utf-8')
        try:
            text = tweet['text']
        except KeyError:
            text = ""
        text = re.sub('[^A-Za-z0-9 ]+','',text).lower().split(" ")
        print calc_sentiment_score(text,sentiments)

def calc_sentiment_score(text,sentiments):
    score = 0
    for word in text:
        try:
            score += sentiments[word]
        except KeyError:
            score += 0
    return score

if __name__ == '__main__':
    main()