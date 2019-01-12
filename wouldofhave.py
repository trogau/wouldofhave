from time import sleep
from pprint import pprint
import tweepy

tweepy.debug(True)

# Create variables for each key, secret, token
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
#tweet = 'Hello, world!'
#api.update_status(status=tweet)

#for tweet in tweepy.Cursor(api.search, q='"fricklesnapper would of"', lang='en').items():
for tweet in tweepy.Cursor(api.search, q='"would of"', lang='en').items():
	try:

		print('\nTweet by: @' + tweet.user.screen_name)
		#pprint(tweet)
		# https://twitter.com/trawg/status/901093707298066432
		print(tweet.text.encode('utf-8'))
		print("ID: %s"  % tweet.id_str)
		#print(vars(tweet))
		#.encode('utf-8').strip())

		#tweet.retweet()
		#print('Retweeted the tweet')

		#reply = "Hi @" + tweet.user.screen_name + "! Sorry to be annoying, but you probably mean 'would have' :D https://twitter.com/trawg/status/" + tweet.id_str
		#api.update_status(status=reply)

		reply = "@" + tweet.user.screen_name + " Hi @" + tweet.user.screen_name + "! Sorry to be annoying, but you probably mean 'would have' :D https://twitter.com/trawg/status/" + tweet.id_str
		api.update_status(status=reply, in_reply_to_status_id=tweet.id_str)

		break

		#tweet.retweet()

	except tweepy.TweepError as e:
		print(e.reason)

	except StopIteration:
		break
