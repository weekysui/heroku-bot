# Dependencies
import tweepy
import json
import time

# Twitter API Keys
cconsumer_key = "pJ0X1Xe1QunPyJeOPiASanhGC"
consumer_secret = "0vZ7kikSoggZEBc6FljkfmGVzyqA7HOCt6FXmhKqlwlxmdy6wA"
access_token = "969399183537926144-CQU4oFENko2Sr3VkAjZxI7PsK5nRTkf"
access_token_secret = "tZc00HTy5GeXBrIkx9kbPYaDFr3wqNZwEzZ59JlsoUyDX"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
