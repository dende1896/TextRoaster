import tweepy
import os

# Hol dir deine API-Keys aus den Umgebungsvariablen
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Überprüfen, ob die Variablen korrekt geladen wurden
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)

# Authentifizierung
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Einen Tweet posten
tweet = "Hello, world! #ArtikelRoaster"
api.update_status(tweet)
