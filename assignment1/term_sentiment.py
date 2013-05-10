import sys
import json

def main():
    sentiments_path = sys.argv[1]
    tweets_path = sys.argv[2]

    tweets = []
    for line in open(tweets_path,'r').readlines():
        tweet = json.loads(line)
        if "text" in tweet.keys():
            text = tweet["text"].encode('utf-8')
            tweets.append(text)

    sentiments = {}
    for line in open(sentiments_path,'r').readlines():
        term, score = line.split("\t") 
        sentiments[term] = int(score)             

    calc_sentiments(tweets, sentiments)


def calc_sentiments(tweets, sentiments):

    tweet_sentiments = {}
    term_sentiments = {}

    for tweet in tweets:
        tweet_score = 0

        for word in tweet.split():
            tweet_score += word_score

            if word.lower() in term_sentiments.keys():
                word_score = sentiments[word.lower()]
            else:
                word_score = 0
                term_sentiments[word.lower()] = word_score


        tweet_sentiments[tweet] = tweet_score


    for term in term_sentiments:

        if term not in sentiments:

            new_score = 0
            frequency = 1

            for tweet, score in tweet_sentiments:
                if term in tweet:
                    new_score += score
                    frequency += 1

            new_score /= frequency
            term_sentiments[term.lower()] = new_score

        print "%s %s" % (term, str(float(term_sentiments[term])))


if __name__ == '__main__':
    main()