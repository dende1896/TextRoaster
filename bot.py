import tweepy
import os

# OAuth2 (Bearer Token)
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

# Initialisierung des Clients mit OAuth2 Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Definiere den Tweet-Text
tweet = "Hello, world! #ArtikelRoaster"

# Poste den Tweet über die v2 API
response = client.create_tweet(text=tweet)
print(response)
