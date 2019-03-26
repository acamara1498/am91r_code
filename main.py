import gather_store_tweets as gst

if __name__ == '__main__':
    gst.getTweets("FB")
    print ("DONE gathering tweets for FB......")
    gst.getTweets("GOOG")
    print ("DONE gathering tweets for GOOG......")
