import gather_store_tweets as gst
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    gst.getTweets("FB")
    logger.info("DONE gathering tweets for FB......")
    gst.getTweets("GOOG")
    logger.info("DONE gathering tweets for GOOG......")
