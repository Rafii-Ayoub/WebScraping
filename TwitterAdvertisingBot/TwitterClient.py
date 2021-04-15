from TwitterAuthenticater import *
from tweepy import API
from tweepy import Cursor
from TwitterAnalyzer import *
import pandas as pd
import numpy as np
import tweepy
import time

class TwitterClient:
    
    # Constructor
    def __init__(self, twitter_user=None):
        """
        args: twitter_users

        """
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        """
        args: 
             num_tweets (int)
             num_tweets: is the limit of items that we want request from twitter API
             
        returns:
             a list of tweet objects
        """
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
      
        """
        args: 
             num_friends (int)
             num_friends: is the limit of items that we want request from twitter API
             
        returns:
             a list of friend objects 
        """
        
        friend_list = []
        for friend in Cursor(self.twitter_client.friends_ids, id=self.twitter_user).items(num_friends):
             friend_list.append(friend)
        return friend_list
    
    
    def get_followers_list(self, num_followers):
      
         """
        args: 
             num_followers (int)
             num_followers: is the limit of items that we want request from twitter API
             
        returns:
             a list of follower objects 
         """
        
        followers_list = []
        for follower in Cursor(self.twitter_client.followers_ids, id=self.twitter_user).items(num_followers):
            followers_list.append(follower)
        return followers_list
      
      
      
      
      
