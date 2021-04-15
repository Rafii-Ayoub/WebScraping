import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tweepy

from TwitterAnalyzer import TweetAnalyzer
from TwitterClient import TwitterClient
from tweepy import api
from tweepy import Cursor
import time


class twitterBot:
   
    # The constructor
    def __init__(self,user_name):

        self.user_name=user_name

    def getUser_name(self):
       return  self.user_name

    def plot(self):
      """ 
      plot that generates likes and retweets of followers as a function of time (days) 
      
      """
      twitter_client = TwitterClient()
      tweet_analyzer = TweetAnalyzer()

      api = twitter_client.get_twitter_client_api()
      tweets = api.user_timeline(screen_name= self.getUser_name())

      df = tweet_analyzer.tweets_to_data_frame(tweets)
      #df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
      time_likes = pd.Series(data=df['likes'].values, index=df['date'])
      
      time_likes.plot(figsize=(15, 5), label="likes", legend=True)
      time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
      time_retweets.plot(figsize=(15, 5), label="retweets", legend=True)
      plt.show()
    
    def plot1(self):
      """ 
      plot that generates likes and retweets of followers as a function of time (hours) 
      
      """
      twitter_client = TwitterClient()
      tweet_analyzer = TweetAnalyzer()

      api = twitter_client.get_twitter_client_api()
      tweets = api.user_timeline(screen_name= self.getUser_name())

      df = tweet_analyzer.tweets_to_data_frame1(tweets)
      #df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
      time_likes = pd.Series(data=df['likes'].values, index=df['date'])
      time_likes.plot(figsize=(15, 5), label="likes", legend=True)
      time_retweets = pd.Series(data=df['retweets'].values, index=df['date'])
      time_retweets.plot(figsize=(15, 5), label="retweets", legend=True)
      plt.show()
    
    
      
     

    

