import tweepy
import os

# Hol dir die OAuth1-Authentifizierungsdaten aus den Umgebungsvariablen
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
    raise ValueError("Eine oder mehrere OAuth1-Umgebungsvariablen fehlen.")

# Erstelle den Client für die v1.1 API mit OAuth1
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
client = tweepy.API(auth)

# Definiere den Tweet-Text
tweet = "Hello, world! #ArtikelRoaster"

# Poste den Tweet über die API v1.1
response = client.update_status(status=tweet)
print(response)
