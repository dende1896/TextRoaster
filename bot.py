import tweepy
import os

# Hol dir den Bearer Token aus den Umgebungsvariablen
bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

# Erstelle den Client für die v2 API
client = tweepy.Client(bearer_token=bearer_token)

# Definiere den Tweet-Text
tweet = "Hello, world! #ArtikelRoaster"

# Poste den Tweet über die API v2
response = client.create_tweet(text=tweet)
print(response)
