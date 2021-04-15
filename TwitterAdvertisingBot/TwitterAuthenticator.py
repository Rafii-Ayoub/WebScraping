from tweepy import OAuthHandler



ACCESS_TOKEN = "1099755262527893504-LJEI9nbR3pp9IUA6IyUSjU7OMB4zrT"
ACCESS_TOKEN_SECRET = "lgQddaL2v3ZvnZ7CavHzeFxPZhZbvfUkjU8Cy2N2niuVL"
CONSUMER_KEY = "6wcOsLfkoFsKWR868W4HLaYid"
CONSUMER_SECRET = "aX7QPPS3yYve8yuB0zT5UfVafZsFlfZvtfASk1stxPkCNEWj9c"


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
      
        """ 
        function that able us to connect to twitter API's
        
        """
        
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth
