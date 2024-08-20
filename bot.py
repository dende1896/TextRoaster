import tweepy
import os

# Set up the client with bearer token (v2 API)
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
client = tweepy.Client(bearer_token=bearer_token)

# Define the tweet text
tweet = "Hello, world! #ArtikelRoaster"

# Post the tweet using the v2 API
response = client.create_tweet(text=tweet)
print(response)
