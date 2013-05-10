import sys
import json
import re

def main():

    tweets_path = sys.argv[2]
    tweets = []

    print "Parsing tweets and building an array..."
    for line in open(tweets_path,'r').readlines():
        tweet = json.loads(line)
        if "text" in tweet.keys():
            text = tweet["text"].encode('utf-8').lower()
            text = re.sub('[^A-Za-z0-9 ]+','',text)     
            tweets.append(text)


    sentiments_path = sys.argv[1]
    sentiments = {}

    print "Parsing sentiments and building a dictionary ..."
    for line in open(sentiments_path,'r').readlines():
        term, score = line.split("\t") 
        sentiments[term.lower()] = int(score)             


    tweet_sentiments = {}
    term_sentiments = {}

    print "Scoring each tweet and saving it into a dictionary..."
    for tweet in tweets:
        tweet_score = 0
        for word in tweet.split():
            word = word.lower()
            word_score = sentiments[word] if word in sentiments else 0
            tweet_score += word_score

            if word not in term_sentiments.keys():
                term_sentiments[word] = word_score

            tweet_score += word_score

        tweet_sentiments[tweet] = tweet_score


    print "And finally calculating sentiments.."
    for term in term_sentiments:
        if term not in sentiments:

            #print "'%s' not found in the terms dictionary. Calculating...." % term            
            term = term.lower()
            new_score = 0
            frequency = 1

            for tweet in tweet_sentiments:
                if term in tweet:
                    new_score += int(score)
                    frequency += 1

            new_score /= frequency
            term_sentiments[term] = new_score
            print "%s => %s" % (term, new_score)
        #else:
            #print "'%s' found in the terms dictionary '%s' => '%s'" % (term, term, term_sentiments[term])             
        print "%s %s" % (term, term_sentiments[term])
        #print term_sentiments[term]


if __name__ == '__main__':
    main()