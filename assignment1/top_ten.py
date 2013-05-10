import sys
import json
import re
import operator


def main():

    tweets_path = sys.argv[1]
    frequency_dic = {}

    for line in open(tweets_path,'r').readlines():
        tweet = json.loads(line)
        if "text" in tweet.keys():
            text = tweet["text"].encode('utf-8').lower() 
            hash_tags = {tag.lower() for tag in text.split() if tag.startswith("#")}
            for tag in hash_tags:
                frequency_dic[tag] = (frequency_dic[tag] + 1.0) if tag in frequency_dic.keys() else 1.0

    for tag, frequency in sorted(frequency_dic.iteritems(), key=operator.itemgetter(1)):
        print "%s %s" % (tag, frequency)


if __name__ == '__main__':
    main()