import sys
import json
import re

def main():

    tweets_path = sys.argv[1]
    tweets = []
    frequency_dict = {}


    for line in open(tweets_path,'r').readlines():
        tweet = json.loads(line)
        if "text" in tweet.keys():
            text = tweet["text"].encode('utf-8').lower()
            text = re.sub('[^A-Za-z0-9 ]+','',text)     
            for word in text.split(' '):
                frequency_dict[word] = (frequency_dict[word] + 1.0) if word in frequency_dict.keys() else 1.0

    for word in frequency_dict:
        print "%s %s" % (word, frequency_dict[word] / sum(frequency_dict.values()))



if __name__ == '__main__':
    main()