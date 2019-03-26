from tweepy import Stream
from stream_tweets import StockListener
import get_old_tweets

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def getTweets(stock_name):
    twitter_stream = Stream(get_old_tweets.auth, StockListener(stock_name))
    twitter_stream.filter(track=[("$"+stock_name)])

    logging.info("Stream for", stock_name, "is active...")

    get_old_tweets.get_past_tweets(stock_name)

    logging.info("Past tweets of", stock_name, "added to db...")
