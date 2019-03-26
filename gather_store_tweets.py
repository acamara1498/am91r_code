from tweepy import Stream
from stream_tweets import StockListener
from get_old_tweets import get_past_tweets

def getTweets(stock_name):
    twitter_stream = Stream(auth, StockListener(stock_name))
    twitter_stream.filter(track=[("$"+stock_name)], async=True)

    print("Stream for", stock_name, "is active...")

    get_past_tweets(stock_name)

    print("Past tweets of", stock_name, "added to db...")
