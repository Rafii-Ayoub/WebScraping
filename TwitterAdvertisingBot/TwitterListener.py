from tweepy.streaming import StreamListener

class TwitterListener(StreamListener):
    """
    This is a listener that  prints received tweets file.
    """
     
    # Constructor 
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        
        """
        args :
                data
        returns:
               boolean
               file with data.
        """  
            
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

