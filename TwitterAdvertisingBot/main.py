from TwitterBot import *
from TwitterClient import *
import pandas

if __name__ == '__main__':
    """
       The main is responsible for executing the program
       
    """
    
    
    def choice1():
        """
        Function that generate plots that show the activity of followers of a twitter account.
        
        """
        client_name = str(input("Enter the customer's name :"))
        df=twitterBot(client_name)
        df.plot2()

        
    def choice2():
       """
        Function that generate csv file that contains the data about followers of a twitter account.
        
        """
       client_name = str(input("Enter the customer's name:"))
       client=TwitterClient(client_name)
       tweets_df=client.get_followers_tweets(10)
       tweets_df.to_csv("test.csv")
      
      
    choice = int(input("Bonjour, put : \n 1  for Statistics about the activity of your followers. \n 2  for a csv file contains data about your followers activity. "))
    
    
    if choice ==1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        print("You should choose option: 1 or 2.")
