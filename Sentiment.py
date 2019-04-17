import tweepy
import re
from tweepy import OAuthHandler 
from textblob import TextBlob

#Need to generate these from twitter developer account
api_key 			= 'xxxxx'	
api_secret_key 		= 'xxxxx'
access_token 		= 'xxxxx'
access_token_secret = 'xxxxx'

#Helpful for debugging
def debug_print(temp):
	index = 0
	for i in temp:
		print(str(index + 1) + " >: " + temp[index] + '\n') 
		index = index + 1	

def get_tweets(user):
	auth = OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret) 
	api = tweepy.API(auth) 
	
	tweets = api.search(q = user, count = 100, show_user = 'true') 
	
	endtweet = [tweet.text for tweet in tweets]   

	temp = []
	for j in endtweet: 
		temp.append(j)  
	
	return temp

def parse_tweet(tweet):
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

def get_tweet_sentiment(tweet): 

	analysis = TextBlob(str(tweet)) 

	if analysis.sentiment.polarity > 0: 
		return 'positive'
	elif analysis.sentiment.polarity == 0: 
		return 'neutral'
	else: 
		return 'negative'


if __name__ == '__main__': 
	tweet = get_tweets("Donald Trump")
	
	actual_tweet = []	
	sentiment_tweet = []
	for i in tweet:
		actual_tweet.append(parse_tweet(i))

	for i in actual_tweet:
		sentiment_tweet.append(get_tweet_sentiment(i))

	print("From Trump's 100 mention in twitter, this amount was positive: " + str(sentiment_tweet.count('positive')))
	print("From Trump's 100 mention in twitter, this amount was neutral: " + str(sentiment_tweet.count('neutral')))
	print("From Trump's 100 mention in twitter, this amount was negative: " + str(sentiment_tweet.count('negative')))
	positive_index = sentiment_tweet.index('positive')
	neutral_index = sentiment_tweet.index('neutral')
	negative_index = sentiment_tweet.index('negative')
	print("This is a sample positive tweet: " + actual_tweet[positive_index])
	print("This is a sample neutral tweet: " + actual_tweet[neutral_index])
	print("This is a sample negative tweet: " + actual_tweet[negative_index])
	
	