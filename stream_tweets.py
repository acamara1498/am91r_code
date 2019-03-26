from tweepy.streaming import StreamListener
import singleton_db as sdb

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class StockListener(StreamListener):
    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.db = sdb.Database()


    def on_data(self, data):
        try:
            self.db.insert(self.stock_name, data)
        except BaseException as e:
            logger.info("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        logger.info("Stream for", stock_name, "has ended...")
        log(status)
        return True
