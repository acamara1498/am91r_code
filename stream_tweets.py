from tweepy.streaming import StreamListener
import singleton_db as sdb

class StockListener(StreamListener):
    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.db = sdb.Database()


    def on_data(self, data):
        try:
            self.db.insert(self.stock_name, data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        Print("Stream for", stock_name, "has ended...")
        log(status)
        return True
