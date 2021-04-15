from TwitterAuthenticater import TwitterAuthenticator
from TwitterListener import TwitterListener
from tweepy import Stream

class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    
    # Constructor
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)



