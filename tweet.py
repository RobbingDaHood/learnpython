import tweepy
from textblob import TextBlob

consumer_key = 'FNMy7AwgSDQEy8kNs9ITDal3Y' 
consumer_secret = 'ikJKcnBoOdp1xPMbdh0Hx8zKQROiLtGFTE4T3fKIAyfgPNSH31' 

access_token = '857593166895120384-2Xpko2fz5Hj1YoPE3XUSJAFkTKcrlRA'
access_toke_secret = 'BR4Vo1JrwchMJr6aVaqikhmnBiDBKoTDDwWGw48fJQEiL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_toke_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets: 
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)