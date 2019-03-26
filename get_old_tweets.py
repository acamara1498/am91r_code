import json
import keys
import tweepy
import singleton_db as sdb

def get_past_tweets(stock_name):
    db = sdb.Database()

    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)

    api = tweepy.API(auth)

    results = tweepy.Cursor(api.search,
                           q="$" + str(stock_name),
                           since="2017-03-24",
                           until="2019-03-24",
                           lang="en").items()

    for tweet in results:
        db.insert(stock_name, tweet)
