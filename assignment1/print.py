import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
tweets =  json.load(response)

for tweet in tweets["results"]:
	print tweet["text"]